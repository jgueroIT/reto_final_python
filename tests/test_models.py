import pytest
from flask import Flask
from app import db
from app.models import Data  # Asegúrate de que la ruta de importación sea correcta

# Configuración de la app de prueba
@pytest.fixture
def test_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

# Test para creación de instancia del modelo
def test_create_data_instance(test_app):
    with test_app.app_context():
        data = Data(name="Test Name")
        db.session.add(data)
        db.session.commit()

        retrieved = Data.query.first()
        assert retrieved is not None
        assert retrieved.name == "Test Name"
        assert isinstance(retrieved.id, int)

# Test para representación (__repr__)
def test_repr_method(test_app):
    with test_app.app_context():
        data = Data(name="Sample")
        db.session.add(data)
        db.session.commit()

        expected = f"<Data id={data.id} name=Sample>"
        assert repr(data) == expected
