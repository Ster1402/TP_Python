import Compte.py
import Controleur.py

class Guichetier(Personne): #Sous-Classe Guichetier ayant comme classe mere Personne

    # Notre méthode constructeur
    
     def __init__(self):
     
        #Constructeur de notre classe

        self._Personne = Personne();

    def affSolde(self):
        print("Solde disponible est de {0} FCFA : Protected".format(compte.solde))

    def versement(self,compte,15000):
        # Un montant de 15000 va etre retirer
        print("Versement de {0} : Protected".format(mt))
        self.affSolde(compte)
    
    def retrait(self,Compte,7000):
        """ ici, un test va etre effectuer dans la classe Controlleur pour savoir si le solde disponible est suffisant """
        # Si "OUI" ... un retrait de 7000 par exemple est effectuer
        print("montant débité de {0} FCFA: Protected".format(mt))
        
        self.affSolde()
