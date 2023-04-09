from anyio import Path
from flask import Flask, request, abort
import sqlite3
import jwt
from datetime import datetime, timedelta
import base64
from libs.crypt import Crypt

datetime.time

passphrase = "r8r8Eib)$Z{LwWGvNv~faHk;'H9}OM,~HKQ8XO&n6cj&l]hi4D"

app = Flask(__name__)

def generate_jwt():
    now = datetime.utcnow()
    data = {
        "username": "Baguette",
        "password": "MiContraseña123",
        "exp": (now + timedelta(hours=48)).timestamp(),
    }

    payload = {
        "data": Crypt(str(data), passphrase).encrypt().decode()
    }
    return jwt.encode(payload=payload, key=passphrase, algorithm="HS256")

def decode_jwt(token: str):
    jwt_decoded = jwt.decode(jwt=token, key=passphrase, algorithms=["HS256"])
    decoded = Crypt(jwt_decoded["data"], passphrase).decrypt().decode()
    return decoded

@app.route('/login', methods=['GET'])
def login():
    token = generate_jwt()
    decoded_token = decode_jwt(token)
    return f"""Token: {token}
Decoded: {decoded_token}"""

@app.route('/check-token/<token>')
def check_token(token: str):
    return ''

app.run()