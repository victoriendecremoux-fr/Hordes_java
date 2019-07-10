import time as tm
import random as rd
import os
import pickle as pk
import Individu
from tkinter import *


def arrondi(nb,pourcentage):
    return int(nb*pourcentage)/pourcentage

def matrice(n):
    L=[[[]for k in range(n)]for k in range(n)]
    for i in range(n):
        for j in range(n):
            L[i][j] = arrondi(rd.random(),10)
    return L


def afficher(matriceListe):
    n = len(matriceListe)
    for i in range(n):
        print(matriceListe[i])

def fonctionExecuterBoutton():
    print("fonctionExecuterBoutton()")
    

def afficherVariableDansLaquelleOnStockeLEntree():
    texte1 = variableDansLaquelleOnStockeLEntree.get()

afficher(matrice(10))


main = Tk()
main.geometry("500x400+600+400") #"largeur x hauteur + decalage abscisse + decalage ordonnee"
main.title("Ceci est un titre")
main['bg'] = 'blue' #changer la couleur du background

#.pack() pour centrer
#.pack(side = RIGHT)
#.pack(side = LEFT)
#.pack(side = RIGHT, padx=100) pour placer a 100 pixel du bord droit
#.place(x='100', y='100') pour placer en x y

texte1 = Label(main).pack() #Creer un texte
bouton1 = Button(main,text="Ceci est un bouton",command = fonctionExecuterBoutton).pack() #Creer un boutton


variableDansLaquelleOnStockeLEntree = StringVar() #initialisation de la variable de stockage
texte2 = Entry(main,textvariable = variableDansLaquelleOnStockeLEntree).pack()


##http://effbot.org/tkinterbook/button.htm
#activeforeground/anchor/bitmap/compound(image+texte)/font/foreground/justify/relief/takefocus/underline
bouton = Button(main)
bouton['text'] = "texte"    #texte du bouton
bouton['bg'] = 'red'        #couleur du bouton
bouton['command'] = afficherVariableDansLaquelleOnStockeLEntree #fonction a execute losqu'on appuie sur le bouton
bouton['activebackground'] = 'yellow'   #couleur du bouton lorsqu'on appuie dessus
bouton['bd'] = 1   #largeur du contour du bouton
bouton['cursor'] = 'circle' #https://www.tutorialspoint.com/python/tk_cursors.htm
bouton['disabledforeground'] = 'grey' #couleur du bouton quand il est desactive
bouton['height'] = 2 # hauteur du bouton
bouton['width'] = 5 #largeur du bouton
#bouton['image'] =
#bouton['padx'] =
#bouton['pady'] =
bouton['repeatdelay'] = 200000  #pas compris comment ca marche
bouton['repeatinterval'] = 20000 #pas compris comment ca marche
bouton['state'] = 'normal' #NORMAL, ACTIVE or DISABLED.


#bouton['textvariable'] = textvariable #pas compris
#bouton.flash()

#bouton[''] = 
bouton.pack()

#Une fois qu'un bouton est place, on ne peux plus rien changer



