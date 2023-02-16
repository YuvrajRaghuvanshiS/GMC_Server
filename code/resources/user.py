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
        data['response'] = json.loads(data["response"])
        try:
            with open("data.json", "w") as outfile:
                json.dump(data, outfile, indent=4)

            return data, 200
        except Exception as e:
            return {"message": f"error {e}"}, 500
            # FIXME: Exception e is an object, might not be a good idea to use in f-string as is.
