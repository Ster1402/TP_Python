# Hamidou Oumarou
# Matricule : 18A026FS

from Personne import Personne
from Compte import Compte 
from Courant import Courant 
from Epargne import Epargne
from Guichetier import Guichetier
from Controleur import Controleur


class Gestionnaire(Personne):
    
    def __init__(self,matricule = " ",nom = " ",prenom = " "):
        Personne.__init__(self,matricule,nom,prenom);
        
    def ajoutCompte(self, bank ):
        
        bank.nbrCompte = bank.nbrCompte + 1;
        
    def supprimeCompte(self, bank ):
        bank.nbrCompte = bank.nbrCompte - 1;    

    def __str__(self):
        return "\tGestionnaire\n" + Personne.__str__(self)
