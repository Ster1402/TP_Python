# Na'aiya bourai Nathaniel
# Matricule : 18A911FS

from personne import personne
class controleur(personne):
    def__init__(self):
        personne.__init__(self);
        def verifier(self,solde,mt):
            if(solde<=mt):
                return 0;#si la somme demandée est superieur au solde 
            else:
                return 1;#si la somme est inferieur au solde
            
            def__str__(self):
                return "\tcontroleur\n" + personne.__str__(self)
