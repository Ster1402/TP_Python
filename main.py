#importation des différentes classes

from Banque import Banque
from Compte import Compte
from Client import Client
from Courant import Courant
from Personne import Personne


#Teste du fonctionnement de la classe Banque()
banq = Banque()

#Grâce à la méthode __str__ on peut faire : 
print(banq) 

#Teste de la classe Compte

#La création d'un compte ce fait normalement lors de la déclaration d'un Client ( ceci est juste un exemple )
c = Compte(156,40000)
print(c)


#Le gestionnaire à ici pour role de creer, supprimer un compte dans une instance de Banque

g = Gestionnaire("18A026FS","hmdamiral","amiral")
g.ajoutCompte(banq)
print(banq)
g.ajoutCompte(banq)
g.ajoutCompte(banq)
print(banq)
g.supprimeCompte(banq)
print(banq)

#Le controleur ici à pour rôle de vérifier si le solde du compte est suffisant (pour un retrait)

cont =  Controleur()

#Petit exemple
if( cont.verifier( c.solde , 5000 ) ):
  print( "Votre solde est supérieur à 5000 FCFA ! \n" )
else:
  print( "Votre solde est inférieur à 5000 FCFA ! \n" )

#Création d'un Client

cli = Client("18A887FS","Ulritch","ulritch02")
cli.verser(50000)
cli.verser(70000)
print(cli) #information sur le client
cli.retrait(3000)

print(cli.bank) #Information sur la banque du client    
  
#Grâce à la classe Courant, il est possible d'éffectué des transfert d'argent entre 2 comptes
#EXEMPLE : 
ca = Courant(1,50000)
cb = Courant(2,1500)

ca.transfert(cb , 30000) # On prélève 30000 dans ca pour envoyer à cb
print(ca)
print(cb)

#La classe Personne est la super-classe pour Client, Gestionnaire, Controleur et Guichetier
p = Personne("18A983FS","TNES","Esthy") 

#On peut le spécialiser en Client
p = Client()
#Qui  peut être aussi recruté par la banque pour devenir un Controleur par exemple
p = Controleur()

#La classe Personne se contente de regrouper ensemble les attributs propres aux Guichetier, Controleur et Gestionnaire


#Ici on simule des échanges bancaires entre deux client : client1 et client2

print("\t**************************\n")
print("\t*       Simulation       *\n")
print("\t**************************\n")


client1 = Client("18A029FS","NDE TSAPI","Steve-R.")
client2 = Client("18A887FS","ULRITCH","NZOUFOU")

print("\nLes clients mettent de l'argent dans leur compte\n\n")
client1.verser(80000) #Versement de 80000 dans le compte bancaire
client2.verser(40000) 
print(client1)
print(client2)

print("Le client1 éffectue un emprunt d'argent ! \n\n")
client1.emprunt(40000)
print(client1)

print("Le client1 envoie de l'argent dans le compte du client2 \n\n")
client1.envoyer(client2,7500)
client1.envoyer(client2,9000)
print(client2)

print("Le client2 retire de l'argent dans son compte \n")
client2.retrait(60000)
print(client2)

