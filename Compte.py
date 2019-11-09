#  NDE TSAPI STEVE-ROLAND
#  Matricule : 18A029FS

class Compte: #création classe mère Compte bancaire
    
    """Classe représentant le compte d'une personne"""
    def __init__(self,n = 0,solde = 0.0):
        self._numero = n
        self._solde = solde
        
    def __str__(self):
        """Méthode appelée lors d'une conversion de l'objet en chaîne"""
        
        return "\t__Compte__\n\nCode compte : {0} \nSolde : {1}\n".format(self._numero, self._solde)
    
    def _get_numero(self):
        print("\t__Compte__\n\nVotre numéro de compte est : {0} \n".format(self._numero))
        return self._numero
    
    def _get_solde(self):
        print("\t__Compte__\n\nVotre solde est de {0} FCFA \n".format(self._solde))
        return self._solde
    
    def _set_solde(self,new_solde):
        print("\t__Compte__\n\nVotre nouveau solde est de {0} FCFA \n".format(new_solde))
        self._solde = new_solde
    
    def infoSolde(self):
        print("\t__Compte__\n\nVotre solde est de {0} FCFA ! \n".format(self._solde))

    def versement(self,add):
        self._solde += add
        print("\t__Compte__\n\nVersement de {0} FCFA éffectué ! \n".format(add))
        self.infoSolde()
    
    def retrait(self,moins):
        self._solde -= moins
        print("\t__Compte__\n\nLe montant débité est de {0} FCFA\n".format(moins))
        self.infoSolde()
    
    solde = property(_get_solde, _set_solde)    
    numero = property(_get_numero)



