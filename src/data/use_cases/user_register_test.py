from src.infra.db.tests.users_repository import UsersRepositorySpy
from .user_register import UserRegister

def test_register():
    first_name = 'first'
    last_name = 'last'
    age = 34

    repo = UsersRepositorySpy()
    user_register = UserRegister(repo)

    response = user_register.register(first_name, last_name, age)

    assert response['type'] == 'Users'
    assert response['count'] == 1
    assert response['attributes']

    assert repo.insert_user_attributes == response['attributes']

def test_register_first_name_error():
    first_name = 'first12312'
    last_name = 'last'
    age = 34
    repo = UsersRepositorySpy()
    user_register = UserRegister(repo)

    try:
        user_register.register(first_name, last_name, age)
        assert False
    except Exception as exception:
        assert str(exception) == 'Nome invalido para a busca'

def test_register_last_name_error():
    first_name = 'first'
    last_name = 'last12345'
    age = 34

    repo = UsersRepositorySpy()
    user_register = UserRegister(repo)

    try:
        user_register.register(first_name, last_name, age)
        assert False
    except Exception as exception:
        assert str(exception) == 'Nome invalido para a busca'
