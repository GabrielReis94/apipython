from flask import Flask, request, jsonify
from db import db
from flask_sqlalchemy import SQLAlchemy

# Criação da aplicação Flask
app = Flask(__name__)

# Configuração da string de conexão com o banco de dados PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@db:5432/customer_records'
# Desabilita o rastreamento de modificações para economizar recursos
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa o objeto db (SQLAlchemy) com a aplicação Flask
db.init_app(app)

# Modelo Customer, representa a tabela 'customers' no banco de dados
class Customer(db.Model):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True)  # Chave primária
    name = db.Column(db.String(100), nullable=False)  # Nome do cliente
    email = db.Column(db.String(120), nullable=False, unique=True)  # Email único

# Rota para consultar todos os clientes cadastrados
@app.route('/customers', methods=['GET'])
def get_customers():
    """
    Recupera todos os clientes cadastrados no banco de dados e retorna como uma lista de JSON.
    """
    customers = Customer.query.all()  # Busca todos os registros da tabela customers
    result = [{'id': c.id, 'name': c.name, 'email': c.email} for c in customers]
    return jsonify(result)

# Rota para cadastrar um novo cliente
@app.route('/customers', methods=['POST'])
def add_customer():
    """
    Recebe um JSON com os dados do cliente (name e email), cadastra no banco e retorna o id criado.
    Não permite cadastro de clientes com e-mail já existente.
    """
    data = request.json
    # Verifica se já existe um cliente com o mesmo e-mail
    existing_customer = Customer.query.filter_by(email=data['email']).first()
    if existing_customer:
        return jsonify({'error': 'Cliente com este e-mail já cadastrado.'}), 409

    customer = Customer(name=data['name'], email=data['email'])
    db.session.add(customer)  # Adiciona o novo cliente à sessão do banco
    db.session.commit()       # Salva as alterações no banco
    return jsonify({'id': customer.id}), 201  # Retorna o id do novo cliente

# Rota principal para checagem de status da API
@app.route('/')
def index():
    """
    Rota padrão que retorna uma mensagem indicando que a API está rodando.
    """
    return "API Customer Records está rodando!"

# Inicialização da aplicação e criação das tabelas, se não existirem
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Cria as tabelas no banco de dados, se ainda não existirem
    app.run(host='0.0.0.0', port=5000)  # Inicia o servidor Flask acessível externamente