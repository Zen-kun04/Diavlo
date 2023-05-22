from anyio import Path
from flask import Flask, request, abort
import sqlite3
import jwt
from datetime import datetime, timedelta
import base64
from libs.crypt import Crypt
import json
import ast

datetime.time

passphrase = "r8r8Eib)$Z{LwWGvNv~faHk;'H9}OM,~HKQ8XO&n6cj&l]hi4D"

app = Flask(__name__)

def generate_jwt(username: str, password: str):
    now = datetime.utcnow()
    data = {
        "username": username,
        "password": password,
        "exp": (now + timedelta(hours=48)).timestamp(),
    }

    payload = {
        "data": Crypt(str(data), passphrase).encrypt().decode()
    }
    return jwt.encode(payload=payload, key=passphrase, algorithm="HS256")

def decode_jwt(token: str):
    try:
        jwt_decoded = jwt.decode(jwt=token, key=passphrase, algorithms=["HS256"])
        decoded = Crypt(jwt_decoded["data"], passphrase).decrypt().decode()
        return decoded
    except jwt.exceptions.DecodeError:
        return None

@app.route('/login', methods=['GET'])
def login():
    token = generate_jwt("DonBaguette", "XDXDXD123")
    decoded_token = decode_jwt(token)
    return f"""Token: {token}
Decoded: {decoded_token}"""

@app.route('/check-token/<token>')
def check_token(token: str):
    decoded = decode_jwt(token)
    print(type(decoded))
    if(decoded) and decoded.startswith('{') and decoded.endswith('}'):
        json_parsed = ast.literal_eval(decoded)
        if("username" in json_parsed and "password" in json_parsed and "exp" in json_parsed):
            # Check if the token expired
            if datetime.utcnow().timestamp() > json_parsed["exp"]:
                return 0
            
            return 1
    return 0

@app.route('/api/v3/', methods=['GET'])
def api_v3():
    return {"message": "Hello World!"}

app.run()