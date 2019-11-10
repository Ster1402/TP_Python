# DJOUDA TCHOUNDA CABREL
# Matricule : 18A043FS

from Compte import Compte

class Epargne(Compte):
  def __init__(self,n = 0, mt = 0.0):
    Compte.__init__(self,n,mt)
  
  def consulterEpargne(self):
    print("Votre épargne s'élève à {0} FCFA".format(self._solde))
  
  def __str__(self):
    return "\tCompte Epargne\n" + Compte.__str__(self)
