"""
Define os modelos de dados (ORM) usados pela aplicação.
Cada classe representa uma tabela no banco de dados.
"""

from db import db

class Customer(db.Model):
    """
    Modelo que representa a tabela 'customers' no banco de dados.
    """
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True)  # Chave primária
    name = db.Column(db.String(100), nullable=False)  # Nome do cliente
    email = db.Column(db.String(120), nullable=False)  # Email do cliente