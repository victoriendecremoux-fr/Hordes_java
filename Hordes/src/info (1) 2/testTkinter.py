from tkinter import *

main = Tk()
main.geometry("500x400+600+400")




def fonctionBouton1():
    texte['text'] = contenu.get()

contenu = StringVar()


texte = Label(main)
texte.pack()

entree = Entry(main,textvariable = contenu).pack()

bouton1 = Button(main,text = "appuyer pour afficher l'entree",command = fonctionBouton1)
bouton1.pack()

