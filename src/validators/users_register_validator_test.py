from .users_register_validator import user_register_validator

class MockRequest:
    def __init__(self) -> None:
        self.json = None


def test_validator():

    request = MockRequest()
    request.json = {
        'first_name': '',
        'last_name': '',
        'age': '',
    }

    user_register_validator(request)