import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app  # Importa sua aplicação Flask

def test_flask_app_creation():
    """Testa se a aplicação Flask é criada corretamente"""
    assert app is not None
    assert app.name == 'app'

def test_home_page():
    """Testa se a página inicial retorna status 200"""
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200

def test_classification_endpoint():
    """Testa o endpoint de classificação"""
    with app.test_client() as client:
        test_data = {'text': 'gostaria de saber o status da minha solicitação'}
        response = client.post('/classify', json=test_data)
        assert response.status_code == 200
        assert 'prediction' in response.json