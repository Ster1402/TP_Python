# Boussa Steve Junior
# Matricule : 18A190FS

from Compte import Compte
from Personne import Personne

class Guichetier(Personne): #Sous-Classe Guichetier ayant comme classe mere Personne

    # Notre méthode constructeur
    
    def __init__(self,mat = " ",nom = " ", prenom =" "):
     
        #Constructeur de notre classe
        # On appelle explicitement le constructeur de Personne :
        Personne.__init__(self,mat,nom,prenom)

    def affSolde(self,compte):
        print("Solde disponible est de {0} FCFA ".format(compte.solde))

    def versement(self,compte = Compte(),mt = 0.0):
        # Un montant va etre ajouter au compte du client
        compte.versement(mt)
    
    def retrait(self,compte,mt):
        """ ici, un test va etre effectuer dans la classe Controlleur pour savoir si le solde disponible est suffisant """
        # Si "OUI" ... un retrait est effectuer par le Guichetier avec la permission du Controleur
        compte.retrait(mt)

    def __str__(self):
        return "\tGuichetier\n" + Personne.__str__(self)
        
