import random as rd
from tkinter import *
import tkinter 

couleurs = ["bleu", "rouge", "jaune", "vert", "rose", "blanc", "violet", "noir"]

codemaker = []
for x in range(4):
    aleatoire = rd.randint(0,7)
    surprise = couleurs[aleatoire]
    codemaker.append(surprise)

codebreaker = []

def couleursChoix():
    global codebreaker

    MsgSympa.set("")

    if len(codebreaker) >= 4:
        MsgSympa.set("Vous avez choisi vos quatre couleurs ! ")
        return

    couleurUne = Texte.get()
    print(couleurUne)
    if couleurUne in couleurs: 
        codebreaker.append(couleurUne)
        Palette.set(Palette.get() + couleurUne + ', ')

    else:
        MsgSympa.set("Ca n'existe pas... Essaie pit-être ces couleurs : bleu, rouge, jaune, vert, rose, blanc, violet, noir")

    Texte.set("")
    return

def testeuh():
    global codebreaker
    solution = []
    ok = 0
    naze = 0
    aVoir = []

    for x in range(4):
        if codemaker[x] == codebreaker[x]:
            ok+=1
        
        else:
            aVoir.append(x)  
    
    for x in aVoir:
        for y in aVoir:
            if codebreaker[x] == codemaker[y]:
                naze+=1
    
    solution.append(ok)
    solution.append(naze)

    codebreaker = []
    Palette.set("")

    Resultat.set("Vous avez trouvé " + str(solution[0]) + " couleurs bien placés ainsi que " + str(solution[1]) + " couleurs mais mal placés.")

    print(solution)

    return 

# Début de l'interface graphique
Mafenetre = Tk()

Mafenetre.title("Mastermind Vie")
Mafenetre.geometry("800x200")

LabelQuestion = Label(Mafenetre, text="Choisissez une couleur siouplai")
LabelQuestion.grid(row = 1, column = 0, padx = 5, pady = 5)

Texte = StringVar()
Champ = Entry(Mafenetre, textvariable = Texte, width="15")
Champ.grid(row=1,column=1, padx = 5, pady = 5)

BoutonLancer = Button(Mafenetre, text ="Valider", command = couleursChoix)
BoutonLancer.grid(row = 2, column = 0, padx = 5, pady = 5)

BoutonTest = Button(Mafenetre, text ="Soumettre", command = testeuh)
BoutonTest.grid(row = 3, column = 0, padx = 5, pady = 5)

Palette = StringVar()
LabelResultat = Label(Mafenetre, textvariable = Palette)
LabelResultat.grid(row = 2, column = 1, padx = 5, pady = 5)

MsgSympa = StringVar()
LabelInfo = Label(Mafenetre, textvariable = MsgSympa)
LabelInfo.grid(row = 3, column = 1, padx = 5, pady = 5)

Resultat = StringVar()
LabelInfo = Label(Mafenetre, textvariable = Resultat)
LabelInfo.grid(row = 5, column = 1, padx = 5, pady = 5)

canvas = tkinter.Canvas(Mafenetre, width=200, height=200, borderwidth=0, highlightthickness=0)
canvas.grid()

def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
tkinter.Canvas.create_circle = _create_circle

def _create_circle_arc(self, x, y, r, **kwargs):
    if "start" in kwargs and "end" in kwargs:
        kwargs["extent"] = kwargs["end"] - kwargs["start"]
        del kwargs["end"]
    return self.create_arc(x-r, y-r, x+r, y+r, **kwargs)
tkinter.Canvas.create_circle_arc = _create_circle_arc

canvas.create_circle(75, 20, 10, fill="red", outline="")
 
Mafenetre.mainloop()