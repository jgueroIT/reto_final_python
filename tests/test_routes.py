import pytest
from flask import Flask
from app import db
from app.routes import data_routes
from app.models import Data


@pytest.fixture
def test_app():
    app = Flask(__name__)
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    app.register_blueprint(data_routes)

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(test_app):
    return test_app.test_client()


def test_insert_data_success(client):
    response = client.post("/data", json={"name": "Test Entry"})
    assert response.status_code == 200
    assert response.get_json()["message"] == "Data inserted successfully"


def test_insert_duplicate_data(client):
    client.post("/data", json={"name": "Duplicate Entry"})
    response = client.post("/data", json={"name": "Duplicate Entry"})
    assert response.status_code == 409
    assert response.get_json()["message"] == "Data already exists"


def test_get_all_data(client):
    client.post("/data", json={"name": "Item1"})
    client.post("/data", json={"name": "Item2"})
    response = client.get("/data")
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) == 2


def test_delete_existing_data(client):
    # Crear y luego eliminar
    client.post("/data", json={"name": "ToDelete"})
    data_id = Data.query.filter_by(name="ToDelete").first().id
    response = client.delete(f"/data/{data_id}")
    assert response.status_code == 200
    assert response.get_json()["message"] == "Data deleted successfully"


def test_delete_nonexistent_data(client):
    response = client.delete("/data/9999")
    assert response.status_code == 404
    assert response.get_json()["message"] == "Data not found"
