
# Nzoufou Ndouanla Ulritch 
# Matriucle : 18A887FS

from Personne import Personne
from Compte import Compte 
from Banque import Banque
from Courant import Courant 
from Epargne import Epargne
from Gestionnaire import Gestionnaire 
from Guichetier import Guichetier
from Controleur import Controleur
 


class Client(Personne):
    def __init__(self,matricule = " " ,nom = " ",prenom = " "):
        Personne.__init__(self,matricule,nom,prenom) #Appel du constructeur de la classe mère
        
        self.bank=Banque()
        self.compte=Courant()
        
        #Le gestionnaire ajoute un compte lors de la création d'un client
        self.bank.gestionnaire.ajoutCompte( self.bank )
        
        self.dettes=0.0
        self.sommerecue=0.0
        self.salaire=240000 #cas d'un enseignent
        
    def envoyer(self,client,montant):
        if (Banque.controleur.verifier(self.compte.solde,montant)):
            Banque.guichetier.verser(client.compte,montant)
        else:
            print("solde insuffisant pour effectuer l'envoie")
    
    def emprunt(self,montant):
        
        if (self.dettes == 0):
            if( ( ((self.bank).controleur).verifier(self.salaire,montant) ) ): #On vérifie que le salaire qu'il touche est suffisant
                self.bank.guichetier.verser(self.sommerecue,montant) #Le guichetier de la banque lui remet alors l'argent
                self.dettes = montant
            else:
                print("l'emprunt n'est pas possible")
            
    def verser(self,montant):
        self.bank.guichetier.versement(self.compte,montant)
        
    def retrait(self,montant):
        if (self.bank.controleur.verifier(self.compte.solde,montant)):
            self.bank.guichetier.retrait(self.compte,montant)
            self.sommerecue += montant
        else:
            print("solde insuffisant pour effectuer le retrait")
            
    def passerAuCompteEpargne(self):
        self.compte = Epargne()
    
    def passerAuCompteCourant(self):
        self.compte = Courant()
    
    def __str__(self):
        return "\tClient\n" + Personne.__str__(self)

