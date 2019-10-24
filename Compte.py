class Compte: #definition de notre classe Compte
  
  def __init__(self) :   #définition du constructeur
    
    #création des attributs
    self._code = ""
    self._solde = 0.0
    
  def _get_code (self) :
    return self._code
  def _set_code (self , new_code ) :
    self._code = new_code
    
  def _get_solde (self) : 
    return self._solde
  
  def _verser (self, new_solde) :
    self._solde = new_solde
    
  def _set_solde(self, newSolde) :
    self._verser( self,newSolde)
    
 #On signale a python que code et solde pointe vers des propriétés
 #suivant la syntaxe : property( methode_accesseur, methode_mutateur, methode_suppression, methode_aide )
 code = property( _get_code , _set_code )
 solde = property( _get_code , _set_solde )
