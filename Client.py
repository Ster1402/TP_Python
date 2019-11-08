
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
        self.sommerecue=0.0 #Lors d'un emprunt
        self.salaire=240000 #par exemple juste
        
    def envoyer(self,client,montant):
        
        if (self.bank.controleur.verifier(self.compte.solde,montant)):
            self.bank.guichetier.versement(client.compte,montant)
            self.compte.solde -= montant
            print("__Envoie de {2} à {0} {1} éffectué avec succès !__ \n".format(client.nom,client.prenom,montant))
        else:
            print("_Solde insuffisant pour effectuer l'envoie_")
          
    def emprunt(self,montant):
        
        if (self.dettes == 0):
            if( ( ((self.bank).controleur).verifier(self.salaire,montant) ) ): #On vérifie que le salaire qu'il touche est suffisant
                self.bank.guichetier.preter(self.sommerecue,montant) #Le guichetier de la banque lui remet alors l'argent
                self.dettes = montant
                print("{0} {1} Somme preçu {2} FCFA ! \n".format(self.nom,self.prenom,montant))
            else:
                print("Vous avez des dettes à rembourser ou bien votre salaire est insuffisant pour votre emprunter cette somme !\n")
            
            
    def verser(self,montant):
        self.bank.guichetier.versement(self.compte,montant)
        
    def retrait(self,montant):
        if (self.bank.controleur.verifier(self.compte.solde,montant)):
            self.bank.guichetier.retrait(self.compte,montant)
            self.sommerecue = montant
        else:
            print("Solde insuffisant pour effectuer le retrait ! \n")
            
    def passerAuCompteEpargne(self):
        self.compte = Epargne()
    
    def passerAuCompteCourant(self):
        self.compte = Courant()
    
    def __str__(self):
        return "\t__Client__\n\n" + Personne.__str__(self) + "\nCapital : {0} FCFA\n\n".format(self.compte.solde)

