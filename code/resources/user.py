import json

from flask_restful import Resource, reqparse


_user_data_parser = reqparse.RequestParser()
_user_data_parser.add_argument(
    "enr_id", type=str, required=True, help="The enrolment ID, required."
)
_user_data_parser.add_argument(
    "response", type=str, required=True, help="Encoded JSON of responses, required."
)


class UserData(Resource):
    def post(self):
        data = _user_data_parser.parse_args()
        try:
            with open("data.json", "w") as outfile:
                json.dump(data, outfile, indent=4)

            print(json.loads(data["response"]))
            return data, 200
        except:
            return {"message": "error"}, 500
