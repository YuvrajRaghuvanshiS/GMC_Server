from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from resources.user import UserData


app: Flask = Flask(__name__)
CORS(app, origins=["https://app.gate.iitk.ac.in"])
# CORS(app, resources={r"/user-data": {"origins": "http://example.com"}})
api: Api = Api(app)


api.add_resource(UserData, "/user-data")

if __name__ == "__main__":
    app.run()
