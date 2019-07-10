import time as tm
import random as rd
import os
import pickle as pk
import Individu
from tkinter import *


    
def modifier(xy,n):
    return (xy + (rd.randint(1,3) - 2))%n

def random20(nb):
    return nb*(rd.random() * 0,4 + 0,8

def initialisation(listeIndividu,n,nbIndividu,QIMoyen):
    for k in range(nbIndividu):
        
        x = rd.randint(0,xymax)
        y = rd.randint(0,xymax)
        age = 240
        QI = random20(QIMoyen)

        listeIndividu[rd.randint(0,1)].append([x,y,age,QI,0])
        

def deplacement(listeIndividu,n):
    for k in range(2):
        for individu in listeIndividu[k]:
            individu[0] += (rd.randint(1,3) - 2))%n
            individu[1] += (rd.randint(1,3) - 2))%n

def probaReproduction():
    return rd.random()> 0.5

def bebe(femme,homme):
    x = homme[0]
    y = homme[1]
    age = 0
    QI = random20((homme[3] + femme[3])/2)
    moisAvantRepro = 0
    return [x,y,age,QI,moisAvantRepro]

def hommeSurLaCase(femme,listeIndividu):
    listeHomme = listeIndividu[1]
    for homme in listeHomme:
        if homme[0:2] == femme[0:2] and homme[2] > 156 and homme[4] == 0 : #Meme coordonnees et l'homme peut se repoduire
            homme[4] = 1
            femme[4] = 9
            listeIndividu[rd.randint(0,1)].append(bebe(femme,homme))
            return 0
    return 0



def reproduction(listeIndividu):
    indiceFemme = 0
    
    femme = listeIndividu[0][0]
    while femme[2] > 156: #tant que la femme consideree a 13 ans (listeFemme triee par age)
        if probaReprodution(): #Si la proba de repro reussie
            if femme[4] == 0: #Si la femme n'est pas deja enceinte
                hommeSurLaCase(femme,listeIndividu)
        indiceFemme += 1
        femme = listeIndividu[0][indiceFemme]
                    
            
    

#homme = [x,y,age,QI,moisAvantRepro]
#femme = [x,y,age,QI,moisAvantRepro]

def main(n,nbIndividu,QIMoyen):

    xymax = n-1
    listeFemme = []
    listeHomme = []
    listeIndividu = [listeFemme,listeHomme]

    initialisation(listeIndividu,n,nbIndividu,QIMoyen)

    #boucle principale
    while listeIndividu != [[],[]]: #tant qu'il y a des individus
        deplacement(listeIndividu,n)
        reproduction(listeIndividu)
        mort(listeIndividu)
        
            
            
        


