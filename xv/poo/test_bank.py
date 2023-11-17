from bank import *
import pytest
from unittest.mock import patch, call # non trouvé : pip install unittest

@pytest.fixture 
def p1():
    return Personne("Martin", "Dupont")

@pytest.fixture 
def p2():
    return Personne("Toto", "Dupont")

@pytest.fixture 
def c1():
    return CompteSimple(p1, 25)

@pytest.fixture
def cc1():
    return CompteCourant(p1, 25)

@pytest.fixture
def b1():
    b = Banque()
    b.ouvrir_compte(p1, 25)
    b.ouvrir_compte(p1, 75)
    return b

@pytest.fixture
def b2():
    b = Banque()
    b.ouvrir_compte_courant(p1, 25)
    b.ouvrir_compte_courant(p1, 75)
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

@patch('builtins.print')
def test_comptecourant(mockprint, cc1):
    cc1.crediter(25)
    assert cc1.solde == 50
    cc1.debiter(25)
    assert cc1.solde == 25
    cc1.afficher_releve()
    assert mockprint.mock_calls == [ call("Un entier est attendu.") ]



# def test_editer_relever_compte_courant(capfd,c2):
#     c2.crediter(15)
#     c2.debiter(25)
#     c2.editerreleve()
#     out,  = capfd.readouterr()
#     assert out == "Credit de 15 euros\nDebit de -25 euros\n"

def test_banque_cc(b2):
    b2.frais(10)
    assert b2.list_compte[0].solde == 15
    assert b2.calculer_total() == 80

