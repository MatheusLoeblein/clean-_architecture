from typing import Dict

class UserRegisterSpy:
    def __init__(self) -> None:
        self.find_atttributes = {}

    def register(self, first_name: str, last_name: str, age: int) -> Dict:
        self.find_atttributes['first_name'] = first_name
        self.find_atttributes['last_name'] = last_name
        self.find_atttributes['age'] = age

        return {
            "type": "Users",
            "count": 1,
            "attributes": self.find_atttributes
        }
