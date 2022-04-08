#testing the claases not the focus on API
#TEST clases indeendendt of api
from animal import Animal
from zoo import Zoo
from enclosure import Enclosure
from employee import Employee

import pytest

@pytest.fixture
def tiger1():
    return Animal("tiger", "TIxi", 12)
@pytest.fixture
def tiger2():
    return Animal("tiger", "IT", 32)

@pytest.fixture
def lion1():
    return Animal('Lion', 'Mamba',6)

@pytest.fixture
def zoo1():
    return Zoo()

@pytest.fixture
def enclosure1():
    return Enclosure("blueCage", 123)


@pytest.fixture
def enclosure2():
    return Enclosure("Redcage", 167)


@pytest.fixture
def caretake1():
    return Employee('Anastasina','Right street')

@pytest.fixture
def caretake2():
    return Employee('Ana','Street')

def test_adding_animal(zoo1, tiger1):
    zoo1.addAnimal(tiger1)
    assert (tiger1 in zoo1.animals)

    zoo1.addAnimal(tiger2)
    assert(len(zoo1.animals)==2)



def test_feedingAnimal(zoo1, tiger1):
    zoo1.addAnimal(tiger1)

    tiger1.feed()

    assert(len(tiger1.feeding_record)==1)

def test_vetAnimal(zoo1,tiger2):
    zoo1.addAnimal(tiger2)
    tiger2.vet()
    tiger2.vet()
    assert (len(tiger2.medical_checkup)==2)

def test_addEnclosure(zoo1):
    zoo1.addEnclosure(enclosure2)

    assert (len(zoo1.zoo_enclosure)==1)

def test_addEmployee(zoo1):

    zoo1.addEmployeer(caretake1)
    zoo1.addEmployeer(caretake2)

    assert(len(zoo1.zoo_employers)==2)

def test_cleanEnclosure(enclosure2):
    enclosure2.clean()

    assert(len(enclosure2.clean_date)==1)

def test_homeToAnimak(tiger1,enclosure2):
    tiger1.AnimalHome(enclosure2.enclosure_id)
    assert(tiger1.enclosure == enclosure2.enclosure_id)
    enclosure2.addAnimal(tiger1)
    assert(len(enclosure2.enclosure_animals)==1)
    assert (enclosure2.enclosure_animals[0]==tiger1)

def test_caretakerAnimal(tiger2,tiger1,caretake1):
    caretake1.assignAnimal(tiger2)
    caretake1.assignAnimal(tiger1)

    tiger2.assignCaretaker(caretake1)
    tiger1.assignCaretaker(caretake1)

    assert (tiger2.care_taker==caretake1)

    assert (tiger1.care_taker == caretake1)

    assert (len(caretake1.Taking_care_of_animals) == 2)
    assert (caretake1.Taking_care_of_animals[0] == tiger2)
    assert (caretake1.Taking_care_of_animals[1] == tiger1)

def test_birthOfAnimal(tiger2,enclosure2, zoo1):
    zoo1.addAnimal(tiger1)
    zoo1.addEnclosure(enclosure2)
    tiger2.AnimalHome(enclosure2.enclosure_id)
    newborn = tiger2.birth()
    zoo1.addAnimal(newborn)

    assert(len(zoo1.animals)==2)
    assert(newborn.enclosure== enclosure2.enclosure_id
           )
