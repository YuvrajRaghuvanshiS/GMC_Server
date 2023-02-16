from flask import Flask
from flask_restful import Api

from resources.user import UserData


app: Flask = Flask(__name__)
api: Api = Api(app)


api.add_resource(UserData, "/user-data")

if __name__ == "__main__":
    app.run()
