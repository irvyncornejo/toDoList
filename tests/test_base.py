from flask_testing import TestCase
from flask import current_app, url_for
from main import app

class MainTest(TestCase):
    
    def create_app(self):
       app.config['TESTING'] = True
       app.config['WTF_CSRF_ENABLED'] = False

       return app

    #validar que la aplicación existe
    def test_app_exists(self):
        self.assertIsNotNone(current_app)
    
    #Validar que la aplicación está en mode de prueba
    def test_app_in_test_mode(self):
        self.assertTrue(current_app.config['TESTING'])
    
    #Que se tienen un redireccionamiento éxitoso
    def test_index_redirects(self):
        response = self.client.get(url_for('index'))
        self.assertRedirects(response, url_for('hello'))
    
    #Hello regresa un estatus code 200
    def test_hello_get(self):
        response = self.client.get(url_for('hello'))

        self.assert200(response)

    def test_hello_post(self):
        fake_form = {
            'user_name': 'fake',
            'password': 'fake',
        }
        response = self.client.post(url_for('hello'), data= fake_form)
        self.assertRedirects(response, url_for('index'))
    
    def test_auth_blueprint_exists(self):
        self.assertIn('auth', self.app.blueprints)

    def test_auth_login_get(self):
        response = self.client.get(url_for('auth.login'))

        self.assert200(response)