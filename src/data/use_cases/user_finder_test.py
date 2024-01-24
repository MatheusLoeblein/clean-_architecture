from src.infra.db.tests.users_repository import UsersRepositorySpy
from .user_finder import UserFinder

def test_find():
    first_name = 'Matheus'
    repo = UsersRepositorySpy()
    user_finder = UserFinder(repo)

    response = user_finder.find(first_name)

    assert response['type'] == 'Users'
    assert response['count'] == len(response['attributes'])
    assert isinstance(response['attributes'], list)
    assert response['attributes'] != []

    assert repo.select_user_attributes['first_name'] == first_name

def test_find_error_in_valid_name():
    first_name = 'Matheus123'
    repo = UsersRepositorySpy()
    user_finder = UserFinder(repo)

    try:
        user_finder.find(first_name)
        assert False
    except Exception as exception:
        assert str(exception) == 'Nome invalido para a busca'

def test_find_error_in_too_long_name():
    first_name = 'MatheusEduardoLoeblein'
    repo = UsersRepositorySpy()
    user_finder = UserFinder(repo)

    try:
        user_finder.find(first_name)
        assert False
    except Exception as exception:
        assert str(exception) == 'Nome muito grande para a busca'

def test_find_error_user_not_found():

    first_name = 'Matheus'
    repo = UsersRepositorySpy(return_empty_list=True)
    user_finder = UserFinder(repo)

    try:
        user_finder.find(first_name)
        assert False
    except Exception as exception:
        assert str(exception) == 'Usuário não encontrado'
