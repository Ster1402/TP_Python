# Boussa Steve Junior
# Matricule : 18A190FS

import Compte.py

class Guichetier(Personne): #Sous-Classe Guichetier ayant comme classe mere Personne

    # Notre méthode constructeur
    
    def __init__(self):
     
        #Constructeur de notre classe
        # On appelle explicitement le constructeur de Personne :
        Personne.__init__(self)

    def affSolde(self):
        print("Solde disponible est de {0} FCFA ".format(compte.solde))

    def versement(self,compte,mt):
        # Un montant va etre ajouter au compte du client
        compte.versement(mt)
        print("Versement de {0} FCFA ".format(mt))
        self.affSolde(compte)
    
    def retrait(self,compte,mt):
        """ ici, un test va etre effectuer dans la classe Controlleur pour savoir si le solde disponible est suffisant """
        # Si "OUI" ... un retrait est effectuer par le Guichetier avec la permission du Controleur
        compte.retrait(mt)
        print("montant débité de {0} FCFA".format(mt))
        
        self.affSolde()
