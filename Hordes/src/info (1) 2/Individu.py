import FonctionUtiles


class Individu: # Définition de notre classe Personne
    """Classe définissant une personne caractérisée par :
    - son âge en jour
    - x
    - y
    - QI
    - estHomme
    - physiqueGenetique
    """

    
    def __init__(self,age,x,y,QI,estHomme): # Notre méthode constructeur
        self.age = age
        self.x = x
        self.y = y
        self.QI = QI
        self.estHomme = estHomme
        #self.physiqueGenetique = physiqueGenetique

    def enfant(homme,femme):
        return Individu(0,homme.x,homme.y,FonctionUtiles.random20(homme.QI + femme.QI),rd.randint(0,1))

        
