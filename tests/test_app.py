import pytest
from app import app
@pytest.fixture
def client():
	with app.test_client() as client:
		yield client
def test_home(client):
	response = client.get('/')
	assert response.status_code == 200
	assert response.data == b'Hello, Docker CI/CD!'

def test_home_page_content_type(client):
	response = client.get('/')
	assert response.content_type = 'text/html; charset=utf-8'

def test_post_method_not_allowed(client):
	response = client.post('/')
	assert response.status_code == 405