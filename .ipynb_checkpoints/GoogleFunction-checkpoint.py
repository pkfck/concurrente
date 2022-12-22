import requests
import pyrebase
import pandas as pd
import datetime as dt

timestamp = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def getdata_update():
    url = "https://sedeaplicaciones.minetur.gob.es/ServiciosRESTCarburantes/PreciosCarburantes/EstacionesTerrestres/"
    response = requests.get(url)
    response.json()
    data = response.json()
    df = pd.json_normalize(data)
    print(df)

    firebaseConfig = {
         "apiKey": "AIzaSyBl0kiFaZe8w8ojx8JEqx44jBoh_GlOS_k",
        "authDomain": "ue-22169594.firebaseapp.com",
        "databaseURL": "https://ue-22169594-default-rtdb.firebaseio.com",
        "projectId": "ue-22169594",
        "storageBucket": "ue-22169594.appspot.com",
        "messagingSenderId": "720509673217",
        "appId": "1:720509673217:web:bdf098f4aa4de2343f4500",
        "measurementId": "G-2PH1N6JKZ4"
    }

    firebase = pyrebase.initialize_app(firebaseConfig)
    storage = firebase.storage()
    storage.child("data.json").put("firebaseConfig")