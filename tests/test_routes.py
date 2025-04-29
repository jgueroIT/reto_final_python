import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    with app.test_client() as client:
        yield client

def test_get_tasks():
    app = create_app('testing')
    client = app.test_client()
    response = client.get('/tasks')
    assert response.status_code == 200

def test_create_task(client):
    app = create_app('testing')
    response = client.post('/tasks', json={'title': 'New Task', 'description': 'New Description'})
    assert response.status_code == 201
    data = response.get_json()
    assert 'id' in data

def test_get_task_by_id(client):
    app = create_app('testing')
    # First, create a task
    response = client.post('/tasks', json={'title': 'Task', 'description': 'Description'})
    task_id = response.get_json()['id']
    # Now, get the task
    response = client.get(f'/tasks/{task_id}')
    assert response.status_code == 200
    data = response.get_json()
    assert data['title'] == 'Task'
    assert data['description'] == 'Description'

def test_delete_task(client):
    app = create_app('testing')
    # First, create a task
    response = client.post('/tasks', json={'title': 'Task to Delete', 'description': 'To be deleted'})
    task_id = response.get_json()['id']
    # Now, delete the task
    response = client.delete(f'/tasks/{task_id}')
    assert response.status_code == 200
    # Verify deletion
    response = client.get(f'/tasks/{task_id}')
    assert response.status_code == 404
