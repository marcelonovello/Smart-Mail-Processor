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
    # PRODUTIVOS (classe 1) - Emails que requerem ação/resposta
    "Preciso do status atualizado do pedido #45678 solicitado na semana passada",
    "Solicito informações técnicas sobre a integração com o sistema de pagamentos",
    "Estamos com problemas críticos no sistema interno de gestão de pedidos",
    "Urgente: necessito de acesso ao painel administrativo para finalizar o relatório",
    "Consulta sobre o processo de aprovação de requisitos para o novo projeto",
    "Relatório financeiro trimestral necessário para auditoria externa na próxima semana",
    "Documento contratual urgente para assinatura antes do fechamento do negócio",
    "Suporte técnico necessário para instalação do software de gestão na nova filial",
    "Relatório de performance do último trimestre com análise de métricas principais",
    "Erro no sistema de login após atualização desta manhã, usuários não conseguem acessar",
    "Preciso do documento de especificações técnicas para dar andamento ao desenvolvimento",
    "Informação financeira necessária para processamento dos pagamentos deste mês",
    "Solicito análise do meu processo de reembolso de despesas com urgência",
    "Requisito de documentos adicionais para conclusão do cadastro no sistema",
    "Problema com a fatura do último mês, valor divergente do combinado",
    "Necessito agendar uma reunião para discutir os detalhes do projeto Orion",
    "Acesso necessário à base de dados para extração de relatórios customizados",
    "Problema de performance na API de integração, resposta com latência alta",
    "Solicitação de orçamento para implementação do novo módulo de segurança",
    "Dúvidas sobre o processo de deploy em produção do sistema atualizado",
    "Problema com entrega do último sprint, necessitamos realinhar prazos",
    "Documentação incompleta para procedimento de compliance, preciso dos arquivos faltantes",
    "Falha no sistema de backup, necessária intervenção urgente da equipe técnica",
    "Relatório de bugs críticos identificados durante testes de qualidade",
    "Solicitação de equipe adicional para cumprimento dos prazos do projeto",
    
    # IMPRODUTIVOS (classe 0) - Emails que não requerem ação imediata
    "Feliz Natal e um próspero Ano Novo para toda a equipe e suas famílias",
    "Parabéns pelo excelente trabalho no último trimestre, resultados impressionantes",
    "Obrigado pela ajuda prestada durante a implementação do novo sistema",
    "Agradeço pelo atendimento de qualidade e prestativo de toda a equipe",
    "Boas festas e muitas felicidades para todos os colegas de trabalho",
    "Desejo um ótimo fim de semana para toda a equipe do departamento",
    "Sucesso para a empresa neste novo ano de desafios e conquistas",
    "Cumprimentos à equipe pelo esforço e dedicação no projeto finalizado",
    "Reconhecimento pelo bom serviço prestado durante todo o ano anterior",
    "Saudações aos colegas do setor de tecnologia pelo trabalho exemplar",
    "Oferta especial imperdível apenas para clientes selecionados como você",
    "Dados bancários para transferência de valores de prêmio conquistado",
    "Sua conta foi bloqueada por medidas de segurança, necessário verificação",
    "Regularize seu cadastro imediatamente para evitar suspensão de serviços",
    "Você ganhou um prêmio exclusivo da nossa promoção de aniversário",
    "Benefício disponível para resgate imediato através do nosso aplicativo",
    "Promoção limitada apenas hoje com descontos especiais para clientes fiéis",
    "Confirme seus dados para receber o kit exclusivo de boas-vindas",
    "Feliz aniversário! Desejamos muita saúde e sucesso em seu dia especial",
    "Comunicado sobre o feriado prolongado da próxima semana",
    "Convite para happy hour de confraternização de final de ano",
    "Newsletter mensal com novidades e tendências do nosso setor",
    "Comunicado sobre mudança no estacionamento da empresa",
    "Lembrete sobre o programa de vacinação disponível para todos os colaboradores",
    "Convite para palestra sobre inovação e tecnologia na próxima quinta-feira"
]

    train_labels = [1] * 25 + [0] * 25
    
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