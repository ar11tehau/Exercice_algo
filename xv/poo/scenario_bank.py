from bank import *

p1 = Personne("Martin", "Dupont")
p2 = Personne("Toto", "Dupont")

# c1 = CompteSimple(p1, 25)
# print(c1.solde)
# c2 = CompteSimple(p2, 75)
# print(c2.solde)

# cc1 = CompteCourant(p1, 25)
# cc1.crediter(100)
# cc1.afficher_releve()
# cc2 = CompteCourant(p2, 75)
# cc2.debiter(10)
# cc2.afficher_releve()


b1 = Banque()
b1.ouvrir_compte_courant(p1, 25)
b1.ouvrir_compte_courant(p2, 75)
b1.list_compte[0].crediter(100)
b1.list_compte[1].crediter(-75)

b1.ouvrir_compte_courant(p1, 25)
b1.ouvrir_compte_courant(p2, 75)

b1.list_compte[2].crediter(25)
b1.list_compte[3].crediter(-25)

b1.afficher_releve()