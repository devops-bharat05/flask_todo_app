# tests/test_app.py

import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200

def test_add_task(client):
    response = client.post('/addtask', data={'newtask': 'Test Task'})
    assert response.status_code == 200

def test_clear_list(client):
    response = client.get('/clear')
    assert response.status_code == 200
