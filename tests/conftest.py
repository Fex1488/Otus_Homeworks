import pytest


# Test API: https://dog.ceo/
@pytest.fixture(scope='session')
def base_url_test_1(request):
    return request.config.getoption('--url', default='https://dog.ceo/')


# Test API: https://www.openbrewerydb.org/
@pytest.fixture(scope='session')
def base_url_test_2(request):
    return request.config.getoption('--url', default='https://api.openbrewerydb.org/')


# Test API: https://jsonplaceholder.typicode.com/
@pytest.fixture(scope='session')
def base_url_test_3(request):
    return request.config.getoption('--url', default='https://jsonplaceholder.typicode.com/')