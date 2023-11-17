from bank import *
import pytest

@pytest.fixture 
def p1():
    return Personne("Martin", "Dupont")

@pytest.fixture 
def p2():
    return Personne("Toto", "Dupont")

@pytest.fixture 
def c1():
    return CompteSimple( p1,25)

@pytest.fixture
def b1():
    b = Banque()
    b.ouvrir_compte(p1, 25)
    b.ouvrir_compte(p1, 75)
    return b

def test_crediter(c1):
    c1.crediter(15)
    assert c1.solde == 40

def test_debiter(c1):
    c1.debiter(15)
    assert c1.solde == 10

def test_negatif(c1):
    c1.debiter(35)
    assert c1.solde == -10

def test_banque_creer_compte(b1):
    assert b1.list_compte[0].solde == 25

def test_total(b1):
    b1.calculer_total() == 100

def test_frais(b1):
    b1.frais(10)
    assert b1.list_compte[0].solde == 15
    assert b1.calculer_total() == 80

# def test_longueur(b1):
#     assert len(b1) == 2