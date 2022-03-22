#testing the claases not the focus on API
#TEST clases indeendendt of api
from animal import Animal
from zoo import Zoo
import pytest

@pytest.fixture
def tiger1():
    return Animal("tiger", "TI", 12)
@pytest.fixture
def tiger2():
    return Animal("tiger", "IT", 32)

@pytest.fixture
def zoo1():
    return Zoo()



def test_adding_animal(zoo1, tiger1):
    zoo1.addAnimal(tiger1)
    assert (tiger1 in zoo1.animals)

    zoo1.addAnimal(tiger2)
    assert(len(zoo1.animals)==2)


def test_feedingAnimal(zoo1, tiger1):
    zoo1.addAnimal(tiger1)

    tiger1.feed()

    assert(len(tiger1.feeding_record)==1)
