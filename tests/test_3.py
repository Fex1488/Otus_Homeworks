import cerberus
import requests
import pytest


def test_api_status(base_url_test_3):
    res = requests.get(base_url_test_3)
    assert res.status_code == 200
    assert res.encoding == 'UTF-8'
    assert res.headers['content-type'] == 'text/html; charset=UTF-8'


def test_api_json_schema(base_url_test_3):
    res = requests.get(base_url_test_3 + "todos/1")
    if res.status_code == 200:
        schema = {
            "id": {"type": "number"},
            "userId": {"type": "number"},
            "title": {"type": "string"},
            "completed": {"type": "boolean"}
        }
        v = cerberus.Validator()

    assert v.validate(res.json(), schema)


@pytest.mark.parametrize('input_id, output_id', [(5, '5'), (-10, '-10'), (0.5, '0.5')])
@pytest.mark.parametrize('input_title, output_title', [('t123', 't123'), ('_', '_'), ('qwr', 'qwr'), ('&', '&')])
def test_api_post_request_1(base_url_test_3, input_id, output_id, input_title, output_title):
    res = requests.post(base_url_test_3 + "posts", data={'title': input_title, 'body': 'bar', 'userId': input_id})
    res_json = res.json()

    assert res_json['title'] == output_title and res_json['body'] == 'bar' and res_json['userId'] == output_id


@pytest.mark.parametrize('input_id, output_id', [(1, '1'), (-10, '-10'), (0.5, '0.5')])
@pytest.mark.parametrize('input_title, output_title', [('foo', 'foo'), ('_', '_'), ('qwr', 'qwr'), ('&', '&')])
def test_api_post_request_2(base_url_test_3, input_id, output_id, input_title, output_title):
    res = requests.put(base_url_test_3 + "posts/1", data={'title': input_title, 'body': 'bar', 'userId': input_id})
    res_json = res.json()

    assert res_json['title'] == output_title and res_json['body'] == 'bar' and res_json['userId'] == output_id


@pytest.mark.parametrize('userId', [-1, 0, 'a', 65432348989898989567])
def test_api_empty_response(base_url_test_3, userId):
    res = requests.get(base_url_test_3 + "posts", params={'userId': userId})

    assert not res.json()
