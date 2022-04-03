# Niveau 1 : comment récupérer en argument le chemin  d'un répertoire

import os

path = input("")



# Niveau 2 : lister les fichiers stp

def listerLesFichiers(chemin) :

    listeFichiers = os.listdir(chemin)

    print("fichiers et répertoires:")
    print(listeFichiers)

    for i in listeFichiers :
        print(i)

fichiers = listerLesFichiers(path)

# Niveau 3 : nombre d'extensions

def donnerNombreExtensions(fichiers):

    print("extensions:")

    allExtensions = []

    for i in os.listdir(fichiers):
        extension = os.path.splitext(i)
        allExtensions.append(extension[1])

    nombreExtensions = [[x, allExtensions.count(x)] for x in set(allExtensions)]

    for i in nombreExtensions :
        if i[0] != '':
            print(i)

donnerNombreExtensions(fichiers)

# Niveau 4 : ajout de raccourci

# if input() == "-l":
#     print(listerLesFichiers(path))
# else:
#     print("la commande -l n'existe pas trop...")

# if input() == "-e":
#     print(donnerNombreExtensions(tousLesFichiers))
# else:
#     print("la commande -e ne fait pas trop d'efforts...")




# Niveau 5 : cf Niveau 3 avec changement du nombre d'extensions par un pourcentage



# Niveau 6 : cf Niveau 5 avec ajout de raccourci + récursivité


# Niveau Bonus : cf Niveau 1, 2 et 6 avec URL à la place du chemin répertoire
