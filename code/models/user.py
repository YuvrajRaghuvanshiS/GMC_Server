class UserModel:
    enr_id:str = ""
    response:str = ""

    def __init__(self, enr_id, response) -> None:
        self.enr_id: str = enr_id
        self.response: str = response

    def json(self) -> dict[str, str]:
        return { "enr_id": self.enr_id, "response": self.response}
