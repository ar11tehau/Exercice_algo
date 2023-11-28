from monnaie import *
import pytest

@pytest.fixture
def m1():
    return Monnaie(5, "€")

@pytest.fixture
def m2():
    return Monnaie(2, "€")


def test_ajout(m1, m2):
    m1.ajouter(m2)
    assert m1.valeur == 7

def test_retrancher(m1, m2):
    m1.retrancher(m2)
    assert m1.valeur == 3

def test_devise_error(m1):
    with pytest.raises(DeviseError):
        m1.ajouter(Monnaie(7, "$"))
    
def test_add(m1, m2):
    assert m1 + m2 == 7

def test_mul(m1):
    assert m1 * 3 == 15