from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address


app = Flask(__name__)
limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"],
    storage_uri="memory://",
)

app.config['JWT_SECRET_KEY'] = '=B,^0Y$F59,nEwMC&F|xz0Vv5Hj5lS'  # Change this to a random secret key

jwt = JWTManager(app)

# Mock user
USER_DATA = {
    "username": "test",
    "password": "test"
}

@app.route('/')
@limiter.limit("10 per minute")
def index():
    return "Welcome to the API!"

@app.route('/hello')
def home():
    return "Hello World!"

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    
    if username != USER_DATA['username'] or password != USER_DATA['password']:
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200

@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

if __name__ == '__main__':
    app.run(debug=True)