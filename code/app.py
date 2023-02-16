from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager

from db import db
from resources.user import UserData


app: Flask = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PROPAGATE_EXCEPTIONS"] = True
app.secret_key = "yuvraj"  # could do app.config['JWT_SECRET_KEY'] if we prefer
api: Api = Api(app)


@app.before_first_request
def create_tables() -> None:
    db.create_all()


jwt: JWTManager = JWTManager(app)

api.add_resource(UserData, "/user-data")

if __name__ == "__main__":
    db.init_app(app)
    app.run()
