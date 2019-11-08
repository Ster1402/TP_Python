# Na'aiya bourai Nathaniel
# Matricule : 18A911FS

from Personne import Personne

class Controleur(Personne):
    def __init__(self):
        Personne.__init__(self);
        
    def verifier(self,solde,mt):
         if(solde < mt ):
             return 0; #Pour false
         else: 
             return 1; #Pour true

    def __str__(self):
        return "\tControleur\n" + Personne.__str__(self)    
