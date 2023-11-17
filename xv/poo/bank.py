class Personne:
    '''
    Personne avec un nom et un prenom
    '''

    def __init__(self, user_nom: str, user_prenom: str):
        self.nom = user_nom
        self.prenom = user_prenom
    
    def __str__(self):
        return f"{self.nom} {self.prenom}"

class CompteSimple:
    '''
    CompteSimple avec un titulaire et un solde
    '''

    def __init__(self, titulaire: Personne, solde:int = 0):
        self.__solde = solde
        self.titulaire = titulaire
    
    @property
    def solde(self):
        return self.__solde
    
    def crediter(self, somme: int):
        self.__solde += somme
    
    def debiter(self, somme: int):
        self.__solde -= somme
    
    def __str__(self):
        return f"Le solde de {self.titulaire} est de : {self.solde}"

class CompteCourant(CompteSimple):
    pass

class Banque:
    '''
    Créer un compte, Calcul du total de l'argent de la banque
    '''

    def __init__(self):
        self.__list_compte = list()
    
    def ouvrir_compte(self, client: Personne, solde: int):
        compte = CompteSimple(client, solde)
        self.__list_compte.append(compte)
        return compte
    
    @property
    def list_compte(self):
        return self.__list_compte
    
    def calculer_total(self):
        total = 0
        for compte in self.__list_compte:
            total += compte.solde
        return total
    
    def frais(self, somme: int):
        for compte in self.__list_compte:
            compte.debiter(somme)

