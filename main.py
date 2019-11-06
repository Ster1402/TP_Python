#importation des différentes classes

from Banque import Banque
from Compte import Compte



#Teste du fonctionnement de la classe Banque()
banq = Banque()

#Grâce à la méthode __str__ on peut faire : 
print(banq) 

#Teste de la classe Compte

#La création d'un compte ce fait normalement lors de la déclaration d'un Client ( ceci est juste un exemple )
c = Compte(156,40000)
print(c)
