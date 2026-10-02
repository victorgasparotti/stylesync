from flask import Blueprint, jsonify, request
from app.models.user import LoginPayLoad
from pydantic import ValidationError
from app import db
from bson import ObjectId

main_bp = Blueprint('main', __name__)

# RF: O sistema deve permitir que um usuário se autentique para obter um token
@main_bp.route('/login', methods=['POST'])
def login():
    try: 
        row_data=request.get_json()
        user_data=LoginPayLoad(**row_data)
    except ValidationError as e:
        return jsonify({'error': e.errors()}), 400
    except Exception as e:
        jsonify({'error': 'Erro durante a requisição do dado'}), 500

    if user_data.username == 'admin' and user_data.password == '123':
        return jsonify({'message': f'Login bem sucedido!'})
    else:
        return jsonify({'message': 'Usuário ou senha inválidos!'})

# RF: O sistema deve permitir listagem de todos os produtos 
@main_bp.route('/products', methods=['GET'])
def get_products():
    products_cursor = db.products.find({})
    products_list = []
    for products in products_cursor:
        products['_id'] = str(products['_id'])
        products_list.append(products)
    return jsonify(products_list)

# RF: O sistema deve permitir a criação de um novo produto
@main_bp.route('/products', methods=['POST'])
def create_product():
    return jsonify({'message': 'Esta é a rota de criação de um novo produto'})

# RF: O sistema deve permitir a visualização e detalhes de um unico produto
@main_bp.route('/product/<int:product_id>', methods=['GET'])
def get_products_by_id(product_id):
    return jsonify({'message': f'Está é a rota de visualização do id do produto: {product_id}'})

# RF: O sistema deve permitir a atualização de um produto e produto existente
@main_bp.route('/product/<int:product_id>', methods=['PUT'])
def update_products(product_id):
    return jsonify({'message': f'Está é a rota de atualização do id do produto: {product_id}'})

# RF: O sistema deve permitir a deleção de um produto e produto existente
@main_bp.route('/product/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    return jsonify({'message': f'Está é a rota de deleção do id do produto: {product_id}'})
# RF: O sistema deve permitir a importação de vendas através de um arquivo
@main_bp.route('/sales/upload', methods=['POST'])
def upload_sales():
    return jsonify({'message': 'Está é a rota de upload de vendas'})



