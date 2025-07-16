"""
Módulo responsável pela configuração e inicialização do banco de dados usando Flask-SQLAlchemy.
"""

from flask_sqlalchemy import SQLAlchemy
import os
from flask import Flask

# Cria a instância do Flask (usada apenas para configuração inicial)
app = Flask(__name__)

# Configura a URI do banco de dados a partir da variável de ambiente ou valor padrão
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
    'DATABASE_URL',
    'postgresql://user:password@db:5432/customer_records'
)
# Desabilita o rastreamento de modificações para economizar recursos
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Instancia o objeto SQLAlchemy, que será usado para interagir com o banco de dados
db = SQLAlchemy(app)

def connect_db():
    """
    Cria todas as tabelas no banco de dados, caso ainda não existam.
    Útil para inicializar o banco na primeira execução.
    """
    try:
        db.create_all()
        print("Database connected and initialized.")
    except Exception as e:
        print(f"Error connecting to the database: {e}")

def execute_query(query, params=None):
    """
    Executa uma query SQL diretamente no banco de dados.
    Útil para comandos personalizados fora do ORM.
    """
    try:
        if params:
            result = db.session.execute(query, params)
        else:
            result = db.session.execute(query)
        db.session.commit()
        return result
    except Exception as e:
        db.session.rollback()
        print(f"Error executing query: {e}")
        return None