#importation des différentes classes

from Banque import Banque
from Compte import Compte
from Client import Client


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
  
