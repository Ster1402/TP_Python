# TCHOUOMKEM NGOUOMOUE ESTHER SORELLE 
# Matricule : 18A983FS

class Personne:
    def __init__(self,matricule = " ",nom = " ",prenom = " "):
        self._matricule = matricule
        self._nom = nom
        self._prenom = prenom
        
    def __str__(self): 
        return "Matricule : " + self._matricule + "\nNom : " + self._nom + "\nPrenom : " + self._prenom
    
    def _get_matricule(self):
        return self._matricule
    def _set_matricule(self,m):
        self._matricule = m
    matricule = property(_get_matricule,_set_matricule)

    def _get_nom(self):
        return self._nom
    def _set_nom(self,n):
        self._nom = n
    nom = property(_get_nom,_set_nom)
    
    def _get_prenom(self):
        return self._prenom
    def _set_prenom(self,p):
        self._prenom = p
    prenom = property(_get_prenom,_set_prenom)
    
