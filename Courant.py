#Raoul

from Compte import Compte

class Courant(Compte):
    
    def __init__(self, n = 0 , solde = 0.0):
        Compte.__init__(self,n,solde)
    
    #Grâce aux comptes Courant on peut éffectué des tranferts d'argent à un autre Compte
    def transfert ( self, compt , montant ):
      self._solde -= montant  
      compt.versement(montant)
        
