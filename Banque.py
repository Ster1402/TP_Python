
#TSAGUE SONIA JANE
#Matricule : 18A030FS

#Utilise des instances de classe Controleur, Gestionnaire et Guichetier

#Importation des differentes classes

from Personne import Personne
from Compte import Compte 
from Courant import Courant 
from Epargne import Epargne
from Gestionnaire import Gestionnaire 
from Guichetier import Guichetier
from Controleur import Controleur


class Banque : 
    
    def __init__(self):
        self.nom = "BEAC"; #Par exemple
        self.codeB = 111;
        self.controleur = Controleur();
        self.gestionnaire = Gestionnaire();
        self.guichetier = Guichetier();
        self.caisse = 10000000; # Montant présent dans la caisse de la banque
        self.nbrCompte = 0; # Nombre de compte bancaire créé
        self.capital = 10000000000; # Capital de la banque
        
    def __str__(self):
        return "\t {0} code : {1}\nCapital : {2} FCFA\nNombre de Compte : {3}\n\n".format(self.nom,self.codeB,self.capital,self.nbrCompte);
