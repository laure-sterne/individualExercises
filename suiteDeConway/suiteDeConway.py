conway = "aabbca"

# Etape 1 : découpage de la chaîne de caractères
def decoupeChaine(str):
    result = ""
    for i in range(len(str)): 
        result += str[i]
        if i < len(str)-1 and str[i] != str[i+1]:
                result += " "
    return result.split()

chaine = decoupeChaine(conway)

# Etape 2 : description de la chaîne
def decritChaine(truc):
    compta = ""
    for i in range(len(truc)):
        compta += str(len(truc[i])) + truc[i][0]
    return compta


# Etape 3 : suite de Conway
def suiteConway(carac, n):
    suite = carac + "\n"
    for i in range(n-1):
        decoupe = decoupeChaine(carac)
        last_line = decritChaine(decoupe)
        suite += last_line + "\n"
        carac = last_line
    print(suite)
    return suite

suiteConway('a', 3)
suiteConway(conway, 5)

# Etape 4 : mise en forme sur un navigateur (à suivre...)