import random as rd
from tkinter import * 

couleurs = ["bleu","rouge","jaune","vert","rose","blanc","violet","noir"]

codemaker = []
for x in range(4):
    aleatoire = rd.randint(0,7)
    surprise = couleurs[aleatoire]
    codemaker.append(surprise)

codebreaker = []

while len(codebreaker) != 4:
    couleurUne = input("Entrez votre couleur :")
    if couleurUne in couleurs: 
        codebreaker.append(couleurUne)

    else:
        print("Ca n'existe pas...")
        print(couleurs)
    

def testeuh(codemaker, codebreaker):
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

    return solution

print(testeuh(codemaker, codebreaker))
print(codemaker)