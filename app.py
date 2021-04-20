from flask_jwt_extended import create_access_token, JWTManager
from flask import Flask, jsonify, request
from products import products
app = Flask(__name__)




app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
#jwt = JWTManager(app)

jwt = JWTManager(app)
#Retora todos los productos
@app.route('/products', methods=['GET'])
def getProducts():
    return jsonify(products)

#Retorna un producto en especifico segun el nombre
@app.route('/products/<product_name>', methods=['GET'])
def getProductsName(product_name):
    for product in products:
        if product['name'] == product_name:
            return jsonify(product)

    return jsonify({"message": "El producto no se encuentra"})


#Insertar un nuevo producto
@app.route('/products', methods=['POST'])
def insertProduct():
    newProduct = {
        "name": request.json['name'],
        "price":request.json['price'],
        "qunatity":request.json['qunatity']
    }
    products.append(newProduct)
    return jsonify({"message": "El producto se ha insertado correctamente", "products": products})


userData = {
    "id": 1,
    "username": "juanest",
    "password": "escarface"
}
@app.route("/token", methods=["POST"])
def create_access_tokenD():
    username = request.json['username']
    password = request.json['password']
    if username == userData['username'] and password == userData['password']:
        access_token = create_access_token(identity=userData['id'])
        return jsonify({"token": access_token, "user_id":userData['id'] })
    return jsonify({"meessage": "Usuario y contraseña incorrectos" })
if __name__ == '__main__':
    app.run(debug=True, port=4000)
