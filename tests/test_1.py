import cerberus
import requests
import pytest


def test_api_status(base_url_test_1):
    res = requests.get(base_url_test_1 + 'dog-api/')
    assert res.status_code == 200
    assert res.encoding == 'UTF-8'
    assert res.headers['content-type'] == 'text/html; charset=UTF-8'


def test_api_validate_json(base_url_test_1):
    res = requests.get(base_url_test_1 + 'api/breeds/image/random')
    if res.status_code == 200:
        schema = {
            "message": {"type": "string"},
            "status": {"type": "string"}
        }
        v = cerberus.Validator()
        assert v.validate(res.json(), schema)
    else:
        assert False


def test_api_variability_json(base_url_test_1):
    res = requests.get(base_url_test_1 + 'api/breeds/image/random')
    if res.status_code == 200:
        res_1 = dict(res.json())
        res = requests.get(base_url_test_1 + 'api/breeds/image/random')
        res_2 = dict(res.json())
        assert res_1['message'] != res_2['message'] and res_1['status'] == res_2['status']
    else:
        assert False


@pytest.mark.parametrize('dog,breed', [('bulldog', ['boston', 'english', 'french']), ('borzoi', []),
                                       ('bullterrier', ['staffordshire']),
                                       ('retriever', ['chesapeake', 'curly', 'flatcoated', 'golden'])],
                         ids=['bulldog', 'borzoi', 'bullterrier', 'retriever'])
def test_api_content_json(base_url_test_1, dog, breed):
    res = requests.get(base_url_test_1 + 'api/breeds/list/all')
    if res.status_code == 200:
        assert res.json()['message'][dog] == breed
    else:
        assert False


@pytest.mark.parametrize('breed', ['afghan', 'basset', 'blood', 'english', 'ibizan', 'plott', 'walker'],
                         ids=['afghan', 'basset', 'blood', 'english', 'ibizan', 'plott', 'walker'])
def test_api_content_json1(base_url_test_1, breed):
    res = requests.get(base_url_test_1 + 'api/breed/hound/list')
    if res.status_code == 200:
        print(res.json())
        assert breed in res.json()['message']
    else:
        assert False
