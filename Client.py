
# -*- coding: utf-8
import Compte.py
import Personne.py
import Banque.py 

class Client(Personne):
    def __init__(self):
        self.bank=Banque()
        self.compte=Compte()
        self.dettes=0.0
        self.sommerecue=0.0
        self.salaire=240000 #cas d'un enseignent
        
    def envoyer(self,client,montant):
        if (Banque.controleur.verifier(self.compte.solde,montant)):
            Banque.guichetier.verser(client.compte,montant)
        else:
            print("solde insuffisant pour effectuer l'envoie")
    def emprunt(self,salaire,montant):
        if(salaire>=montant):
            Banque.guichetier.verser(self.compte,montant)
        else:
            print("l'emprunt n'est pas possible")
    def verser(self,client,montant):
        Banque.guichetier.verser(client.compte,montant)
    def retrait(self,client,montant):
        if (Banque.controleur.verifier(self.compte.solde,montant)):
            Banque.guichetier.verser(client.compte,montant)
        else:
            print("solde insuffisant pour effectuer le retrait")
            
        
    
    

