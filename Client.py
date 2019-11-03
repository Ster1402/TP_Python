
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
        self.sommerecue=0.0 #somme que reçoit le client en main propre (recevoir un chèque par exemple)
        self.salaire=240000 #juste par exemple 
        
    def envoyer(self,client = Client() ,montant):
        if (Banque.controleur.verifier(self.compte.solde,montant)):
            Banque.guichetier.versersement(client.compte,montant)
        else:
            print("solde insuffisant pour effectuer l'envoie")
    
    def emprunt(self,salaire,montant):
        if( ( self.bank.controleur.verifier(self.salaire,montant) ) && self.dettes == 0): #On vérifie que le salaire qu'il touche est suffisant
            self.bank.guichetier.verser(self.sommerecue,montant) #Le guichetier de la banque lui remet alors l'argent
            self.dettes = montant
        else:
            print("l'emprunt n'est pas possible")
            
    def verser(self,client = Client(),montant):
        self.bank.guichetier.versersement(client.compte,montant)
        
    def retrait(self,client = Client(),montant):
        if (self.bank.controleur.verifier(self.compte.solde,montant)):
            self.bank.guichetier.verser(client.compte,montant)
        else:
            print("solde insuffisant pour effectuer le retrait")
            
    def passerAuCompteEpargne(self):
        self.compte = Epargne()
    
    def passerAuCompteCourant(self):
        self.compte = Courant()
    
    

