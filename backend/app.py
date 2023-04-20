from anyio import Path
from flask import Flask, request, Response
import sqlite3
import jwt
from datetime import datetime, timedelta
import base64
from libs.crypt import Crypt
import json
import ast

from datetime import timezone
datetime.time

passphrase = "r8r8Eib)$Z{LwWGvNv~faHk;'H9}OM,~HKQ8XO&n6cj&l]hi4D"

app = Flask(__name__)

def username_exists(username: str):
    """
    This function checks whenever a username exists in the database or not.
    
    This is useful to check the validity of a token and the login form.
    """
    db = sqlite3.connect("backend/database.sql")
    cur = db.cursor()
    return any(cur.execute('SELECT username FROM customers WHERE username = ?', (username,)).fetchone())

def get_columns_from_username(username: str, columns: list):
    if username_exists(username) and bool(columns):
        db = sqlite3.connect("backend/database.sql")
        cur = db.cursor()
        data_retrieved = {}
        for column in columns:
            data = cur.execute("SELECT ? FROM customers WHERE username = ?", (column, username)).fetchone()
            data_retrieved[column] = data[0]
        return data_retrieved

def correct_credentials(username: str, password: str):
    """
    This function checks if there's an existing username with the forwarded password.

    Important function for the token and login form.
    """
    db = sqlite3.connect("backend/database.sql")
    cur = db.cursor()
    return bool(cur.execute('SELECT username FROM customers WHERE username = ? AND password = ?', (username, password)).fetchone())


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
    if request.remote_addr not in ['localhost', '127.0.0.1', '51.68.71.119']:
        return 'bad request'
    request_data = request.form
    if(correct_credentials(request_data.get('username'), request_data.get('password'))):
        token = generate_jwt("DonBaguette", "XDXDXD123")
        decoded_token = decode_jwt(token)
        return f"""Token: {token}
    Decoded: {decoded_token}"""
    return 'bad credentials'

@app.route('/check-token/<token>')
def check_token(token: str):
    decoded = decode_jwt(token)
    print(type(decoded))
    if (decoded) and decoded.startswith('{') and decoded.endswith('}'):
        json_parsed = ast.literal_eval(decoded)
        if ("username" in json_parsed and "password" in json_parsed and "exp" in json_parsed):
            # Return a bad response if the token expired or if the credentials are wrong 
            if datetime.now(timezone.utc).timestamp() > json_parsed[
                "exp"
            ] or not correct_credentials(
                json_parsed["username"], json_parsed["password"]
            ):
                return Response("Invalid token", 401)

            return 1
    return Response("Invalid token", 401)

app.run()