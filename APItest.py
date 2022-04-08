import pytest
import requests
import json

@pytest.fixture
def baseURL():
    return "http://127.0.0.1:7890/"


@pytest.fixture
def zooWithOneAnimal(baseURL):
    requests.post(baseURL +"/animal", {"species":"tiger", "name":"TI", "age":12})
    response = requests.get(baseURL + "/animals")
    return response.content

def test_zoo(zooWithOneAnimal):
    jo = json.loads(zooWithOneAnimal)


    assert (len(jo)==1)
    assert jo[0]["name"]=="TI"