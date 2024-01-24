from typing import List
from src.domain.models.users import Users


class UsersRepositorySpy:

    def __init__(self, return_empty_list: bool = False) -> None:
        self.insert_user_attributes = {}
        self.select_user_attributes = {}
        self.__return_empty_list = return_empty_list

    def insert_user(self, first_name: str, last_name: str, age: int) -> None:
        self.insert_user_attributes = {
            'first_name': first_name, 
            'last_name':last_name, 
            'age':age
            }
        return

    def select_user(self, first_name: str) -> List[Users]:
        self.select_user_attributes = {'first_name': first_name}

        if self.__return_empty_list:
            return []

        return [
            Users(23, first_name, 'Teste', 37),
            Users(23, first_name, 'Teste2', 38),
            Users(23, first_name, 'Teste3', 39)
            ]
