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
    suivi_numero = 10000

    def __init__(self, titulaire: Personne, solde:int = 0):
        self.__solde = solde
        self.titulaire = titulaire
        CompteSimple.suivi_numero += 1
        self.__numero = CompteSimple.suivi_numero
    
    @property
    def solde(self):
        return self.__solde
    
    def crediter(self, montant: int):
        self.__solde += montant
    
    def debiter(self, montant: int):
        self.__solde -= montant

    def __str__(self):
        return f"Le solde de {self.titulaire} est de : {self.solde}"


class CompteCourant(CompteSimple):
    def __init__(self, titulaire: Personne, solde:int = 0):
        super().__init__(titulaire, solde)
        self.__list_releve = list()
    
    def crediter(self, somme: int):
        super().crediter(somme)
        self.__list_releve.append(somme)
    
    def debiter(self, somme: int):
        super().debiter(somme)
        self.__list_releve.append(f"Somme debité : -{somme}")
    
    def afficher_releve(self):
        if len(self.__list_releve) > 0:
            print(f"Relevé du compte {self.numero}:")
            for operation in self.__list_releve:
                print(4*"-" + ">",operation)
            print()
        else:
            print(f"Relevé du compte {self.numero}: Pas de d'opération")

class Banque:
    '''
    Créer un compte, Calcul du total de l'argent de la banque
    '''

    def __init__(self):
        self.__list_compte = list()
    
    def ouvrir_compte(self, client: Personne, solde: int):
        compte = CompteSimple(client, solde)
        self.__list_compte.append(compte)
        self.client_exist(client)
    
    def ouvrir_compte_courant(self, client: Personne, solde: int):
        compte = CompteCourant(client, solde)
        self.__list_compte.append(compte)
        
    @property
    def calculer_total(self):
        total = 0
        for compte in self.__list_compte:
            total += compte.solde
        return total
    
    def frais(self, somme: int):
        for compte in self.__list_compte:
            compte.debiter(somme)
    
    def afficher_releve(self):
        for compte in self.__list_compte:
            try:
                compte.afficher_releve()
            except AttributeError:
                pass


