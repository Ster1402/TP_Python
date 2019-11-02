
# Nzoufou Ndouanla Ulritch 
# Matriucle : 18A887FS

import Compte.py
import Personne.py
import Banque.py 

class Client(Personne):
    def __init__(self):
        self.bank=Banque()
        self.compte=Compte()
        #Le gestionnaire créé un compte lors de la création d'un client
        self.bank.gestionnaire.ajoutCompte()
        self.dettes=0.0
        self.sommerecue=0.0
        self.salaire=240000 #cas d'un enseignent
        
    def envoyer(self,client,montant):
        if (Banque.controleur.verifier(self.compte.solde,montant)):
            Banque.guichetier.verser(client.compte,montant)
        else:
            print("solde insuffisant pour effectuer l'envoie")
    
    def emprunt(self,salaire,montant):
        if( ( self.bank.controleur.verifier(self.salaire,montant) ) && self.dettes == 0): #On vérifie que le salaire qu'il touche est suffisant
            self.bank.guichetier.verser(self.sommerecue,montant) #Le guichetier de la banque lui remet alors l'argent
            self.dettes = montant
        else:
            print("l'emprunt n'est pas possible")
            
    def verser(self,client,montant):
        self.bank.guichetier.verser(client.compte,montant)
        
    def retrait(self,client,montant):
        if (self.bank.controleur.verifier(self.compte.solde,montant)):
            self.bank.guichetier.verser(client.compte,montant)
        else:
            print("solde insuffisant pour effectuer le retrait")
            
    def passerAuCompteEpargne(self):
        self.compte = Epargne()
    
    def passerAuCompteCourant(self):
        self.compte = Courant()
    
    

