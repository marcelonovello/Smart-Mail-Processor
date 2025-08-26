from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

app = Flask(__name__)
CORS(app)

# Configurações
classifier = None

def generate_response(category):
    """Gera resposta automática baseada na categoria do email"""
    if category == 'productive':
        return "Olá, agradecemos seu contato. Sua solicitação está em análise e retornaremos em breve com mais informações."
    else:
        return "Olá, agradecemos sua mensagem! Desejamos um ótimo dia para você."

def keyword_based_classifier(email_text):
    """Classificador baseado em palavras-chave como fallback"""
    productive_keywords = ['status', 'pedido', 'solicitação', 'problema', 'urgente', 
                          'ajuda', 'suporte', 'erro', 'dúvida', 'consulta', 'relatório',
                          'documento', 'financeiro', 'fatura', 'pagamento', 'necessário',
                          'preciso', 'requisito', 'analise', 'processo']
    
    unproductive_keywords = ['feliz', 'parabéns', 'obrigado', 'agradeço', 'boas', 'ótimo',
                            'sucesso', 'cumprimentos', 'reconhecimento', 'saudações', 'natal',
                            'ano novo', 'festas', 'feriado', 'fim de semana', 'cumprimento']
    
    email_lower = email_text.lower()
    
    productive_count = sum(1 for word in productive_keywords if word in email_lower)
    unproductive_count = sum(1 for word in unproductive_keywords if word in email_lower)
    
    if productive_count > unproductive_count:
        return 'productive', 0.7 + (productive_count * 0.05)
    elif unproductive_count > productive_count:
        return 'unproductive', 0.7 + (unproductive_count * 0.05)
    else:
        return 'unproductive', 0.5  # Empate -> considera improdutivo por padrão

def setup_classifier():
    global classifier
    
    # Usar lista simples de stopwords para evitar problemas com NLTK
    stop_words = ['o', 'a', 'os', 'as', 'um', 'uma', 'de', 'do', 'da', 'em', 'no', 'na', 
                 'por', 'para', 'com', 'que', 'e', 'ou', 'mas', 'se', 'como', 'quando']
    
    # Classificador simples com scikit-learn
    classifier = Pipeline([
        ('tfidf', TfidfVectorizer(stop_words=stop_words, max_features=1000)),
        ('clf', LogisticRegression(random_state=42))
    ])
    
    # Dados de treinamento SIMPLES e CLAROS
    train_texts = [
    # PRODUTIVOS (classe 1) - Palavras-chave: status, pedido, solicitação, problema, urgente, relatório, documento, suporte
    "status do pedido atualizado",
    "solicitação de informação técnica",
    "problema com o sistema interno",
    "urgente preciso de ajuda com acesso",
    "consulta sobre processo administrativo",
    "relatório necessário para auditoria",
    "documento urgente para assinatura",
    "suporte técnico necessário para instalação",
    "dúvida sobre fatura emitida",
    "erro no sistema de login",
    "preciso de um documento de contrato",
    "informação financeira necessária para pagamento",
    "análise do meu processo de reembolso",
    "requisito de documentos para cadastro",

    # IMPRODUTIVOS (classe 0) - Palavras-chave: feliz, parabéns, obrigado, prêmio, oferta, bloqueado, benefício
    "feliz natal e próspero ano novo",
    "parabéns pelo excelente trabalho",
    "obrigado pela ajuda prestada",
    "agradeço o atendimento de vocês",
    "boas festas e felicidades",
    "ótimo fim de semana para todos",
    "sucesso para a empresa neste ano",
    "cumprimentos à equipe pelo esforço",
    "reconhecimento pelo bom serviço",
    "saudações aos colegas do setor",
    "oferta especial imperdível para você",
    "dados bancários para transferência",
    "conta bloqueada por segurança",
    "regularize seu cadastro imediatamente",
    "você ganhou um prêmio exclusivo",
    "benefício disponível para resgate",
    "promoção limitada apenas hoje",
    "confirme seus dados para receber"
]

    train_labels = [1] * 16 + [0] * 16
    
    # Treinar o classificador
    classifier.fit(train_texts, train_labels)
    print("Classifier treinado com dados simplificados!")
    
    # Testar com exemplos conhecidos
    test_texts = [
        "gostaria de saber o status da minha solicitação",
        "feliz natal para todos"
    ]
    
    for text in test_texts:
        pred = classifier.predict([text])[0]
        proba = classifier.predict_proba([text])[0]
        print(f"Teste: '{text}' -> {pred} (proba: {proba})")

# Rota principal para a interface web
@app.route('/')
def index():
    return render_template('index.html')

# Rota para classificar email
@app.route('/classify', methods=['POST'])
def classify_email():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Dados JSON inválidos'}), 400
        
    email_text = data.get('text', '')
    
    if not email_text:
        return jsonify({'error': 'Texto do email não fornecido'}), 400
    
    try:
        # Primeiro tenta usar o modelo ML
        prediction = classifier.predict([email_text])[0]
        confidence = classifier.predict_proba([email_text])[0].max()
        
        # Se a confiança for baixa ou classificação parece errada, usa fallback
        if confidence < 0.6:  # Confiança baixa
            category_fallback, confidence_fallback = keyword_based_classifier(email_text)
            return jsonify({
                'category': category_fallback,
                'confidence': float(confidence_fallback),
                'suggested_response': generate_response(category_fallback),
                'method': 'keyword_fallback'
            })
        
        category = 'productive' if prediction == 1 else 'unproductive'
        
        return jsonify({
            'category': category,
            'confidence': float(confidence),
            'suggested_response': generate_response(category),
            'method': 'ml_model'
        })
        
    except Exception as e:
        # Se houver erro no modelo ML, usa classificador por palavras-chave
        category, confidence = keyword_based_classifier(email_text)
        return jsonify({
            'category': category,
            'confidence': float(confidence),
            'suggested_response': generate_response(category),
            'method': 'keyword_fallback_error',
            'error': str(e)
        })

if __name__ == '__main__':
    setup_classifier()
    app.run(debug=True, port=5000)