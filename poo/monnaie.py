class MonnaieError(Exception):
    pass

class DeviseError(MonnaieError):
    pass

class Monnaie:
    '''
    une monnaie est defini par sa devise et sa valeur
    '''

    def __init__(self, valeur: int, devise: str,) -> None:
        self.devise = devise
        self.valeur = valeur

    def verif_devise(self, other):
        if self.devise != other.devise:
            raise DeviseError
    
    def ajouter(self, other):
        self.verif_devise(self.devise, other.devise)
        self.valeur += other.valeur
 
    def retrancher(self, other):
        self.verif_devise(self.devise, other.devise)
        self.valeur -= other.valeur
           
    def __add__(self, other):
        self.verif_devise(self.devise, other.devise)
        return self.valeur + other.valeur
    
    def __mul__(self, other):
        self.verif_devise(self.devise, other.devise)
        return self.valeur * other