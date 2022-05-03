import cerberus
import requests
import pytest


def test_api_status(base_url_test_2):
    res = requests.get(base_url_test_2)
    assert res.status_code == 200
    assert res.encoding == 'UTF-8'
    assert res.headers['content-type'] == 'text/html; charset=UTF-8'


@pytest.mark.parametrize('key', ['id', 'name', 'brewery_type', 'street', 'address_2', 'address_3', 'city', 'state',
                                 'county_province', 'postal_code', 'country', 'longitude', 'latitude', 'phone',
                                 'website_url', 'updated_at', 'created_at'],
                         ids=['id', 'name', 'brewery_type', 'street', 'address_2', 'address_3', 'city', 'state',
                              'county_province', 'postal_code', 'country', 'longitude', 'latitude', 'phone',
                              'website_url', 'updated_at', 'created_at'])
def test_api_validate_json_check_keys(base_url_test_2, key):
    res = requests.get(base_url_test_2 + 'breweries')
    cnt1 = len(res.json())
    cnt2 = 0
    if res.status_code == 200:
        for i_rec in res.json():
            if key in i_rec:
                cnt2 += 1

    assert cnt2 == cnt1


def test_api_validate_json(base_url_test_2):
    res = requests.get(base_url_test_2 + 'breweries/autocomplete?query=dog')
    cnt1 = len(res.json())
    cnt2 = 0
    if res.status_code == 200:
        schema = {
            'id': {'type': 'string'},
            'name': {'type': 'string'}
        }
        for i_rec in res.json():
            v = cerberus.Validator()
            if v.validate(i_rec, schema):
                cnt2 += 1

    assert cnt2 == cnt1


@pytest.mark.parametrize('key', ['id', 'name'], ids=['id', 'name'])
def test_api_variability_keys(base_url_test_2, key):
    res = requests.get(base_url_test_2 + 'breweries?by_dist=38.8977,77.0365')
    cnt1 = len(res.json())
    id_list = set()
    if res.status_code == 200:
        for i_res in res.json():
            id_list.add(i_res[key])

    assert len(id_list) == cnt1


@pytest.mark.parametrize('key', ['address_2', 'address_3'], ids=['address_2', 'address_3'])
def test_api_field_validation(base_url_test_2, key):
    res = requests.get(base_url_test_2 + 'breweries?by_type=micro')
    cnt1 = len(res.json())
    cnt2 = 0
    if res.status_code == 200:
        for i_res in res.json():
            if not i_res[key]:
                cnt2 += 1

    assert cnt2 == cnt1
