from db import db


class UserModel:
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    enr_id = db.Column(db.String(80))

    def __init__(self, name, enr_id) -> None:
        self.name: str = name
        self.enr_id: str = enr_id

    def json(self) -> dict[str, str]:
        return {"id": self.id, "name": self.name, "enr_id": self.enr_id}

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, enr_id):
        return cls.query.filter_by(enr_id=enr_id).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
