from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
import mysql.connector

import os
import time

from dotenv import load_dotenv

load_dotenv()

db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_database = os.getenv('DB_DATABASE')

cnx = mysql.connector.connect(
    user= db_user,
    password= db_password,
    host= db_host,
    database= db_database
)

serverIP = {
    'Akarcraft': 'mc.akarcraft.es',
    'Battlelandia': 'play.battleland.eu',
    'Borkland': 'mc.borkland.es',
    'BuildPlay': 'buildplay.cz',
    'CashMC': 'cashmc.eu',
    'Cotecraft': 'cotecraft.su',
    'Dynamicpvp': 'dynamicpvp.net',
    'Ecuacraft': 'mc.ecuacraft.com',
    'ExcaliburCraft': 'excalibur-craft.ru',
    'FourCraft': 'mcr.fourcraft.ru',
    'FunCraft': 'funcraft.net',
    'Gamesmadeinpola': 'mc.gamesmadeinpola.com',
    'GeoBlock': 'geoblock.es',
    'HyCraft': 'mc.hycraft.us',
    'HyCraft_Sep_2022':'mc.hycraft.us',
    'HydraCraft': 'mc.hydracraft.es',
    'Hypermine': 'mc.hypermine.net',
    'Jogarhappy': 'jogarhappy.com',
    'Latinplay': 'latinplay.net',
    'Librecraft': 'mc.librecraft.com',
    'Lokapsos': 'mc.lokapsos.es',
    'MagicCraft': 'magicraft.es',
    'MasedWorld': 'mc.masedworld.net',
    'Mooncraft': 'mooncraft.es',
    'MultyPlay': 'fun.multyplay.ro',
    'MyCraft': 'server.mycraft.es',
    'Nemerya': 'play.nemerya.fr',
    'Omegacraft': 'mc.omegacraft.cl',
    'OnlyMC': 'play.onlymc.net',
    'OpDex': 'OpDex.ru',
    'PixelmonFR': 'play.pixelmonrealms.com',
    'Prolatino': 'proyectolatino.online',
    'RedeLegit': 'jogar.redelegit.com.br',
    'Royalgaming': 'N/A',
    'SCraft': 'N/A',
    'SkyCraft': 'SkyCraft.es',
    'TecnoCraft': 'mc.tecnocraft.it',
    'Unknown_Server1': 'N/A',
    'VyperCraft': 'mc.vypercraft.es'
}

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
jwt = JWTManager(app)

dbCursor = cnx.cursor()
dbCursor.execute("show tables")
dbTables = [server[0] for server in dbCursor.fetchall()]

print("[+] Connected Succesfully to Diavlo Database")

def queryData(current_user: str, user: str, server: str):
    if server is None:        
        datos = []
        def get_info(victima, table):
            cur = cnx.cursor()
            cur.execute(f"SELECT * FROM {table} WHERE username LIKE %s", (f"%{victima}%",))
            info = cur.fetchall()
            if info:
                datos.append({
                    table: [{
                    'username': result[0],
                    'serverIP': serverIP[result[6]],
                    'passwordDecrypted': result[3],
                    'hash':result[1],
                    'salt': result[2],
                    'userIP': result[4],
                    'email': result[5]
                } for result in info]})

        for database in dbTables:
            get_info(user, database)

        return {
            'search_author': current_user,
            'search_date': int(time.time()),
            'results': datos
        }

    

@app.route('/api/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    
    # You can implement your own logic here to validate the username and password
    
    # For demonstration purposes, we'll use a hardcoded username and password
    if username == 'admin' and password == 'password':
        access_token = create_access_token(identity=username)
        return jsonify({'access_token': access_token, 'rank' : 'Lucifer', 'extended': 0}), 200
    else:
        return jsonify({'error': 'Invalid username or password'}), 401


@app.route('/api/v3/mc/<user>', methods=['GET'])
@jwt_required()
def MCSeacrch(user):
    current_user = get_jwt_identity()
    timestamp = int(time.time())
    
    # Check if the request timestamp is within an acceptable range (e.g., 1 request per second)
    last_request_timestamp = request.headers.get('X-Last-Request-Timestamp')
    if last_request_timestamp:
        last_request_timestamp = int(last_request_timestamp)
        time_difference = timestamp - last_request_timestamp
        if time_difference < 1:  # Adjust this value as per your desired rate limit
            return jsonify({'error': 'Too many requests. Please wait a moment.'}), 429
    else:
        return jsonify({'error': 'Invalid Request.'}), 401
    
        
    if user:
        response = jsonify(queryData(current_user=current_user, user=user,server=None))
        
        print(response)

        # Update the timestamp in the response headers
        response.headers['X-Last-Request-Timestamp'] = str(timestamp)
        return response,200
    
    else:
        return {"Error": "Invalid Username"}, 400



if __name__ == '__main__':
    app.run(debug=True)

