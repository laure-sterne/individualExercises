# Etape 1 : fonction a & fonction b
from operator import index
from collections import Counter

texte = "généralement, on utilise un texte en faux latin ( le texte ne veut rien dire, il a été modifié ), le lorem ipsum ou lipsum, qui permet donc de faire office de texte d'attente. l'avantage de le mettre en latin est que l'opérateur sait au premier coup d'oeil que la page contenant ces lignes n'est pas valide, et surtout l'attention du client n'est pas dérangée par le contenu, il demeure concentré seulement sur l'aspect graphique. ce texte a pour autre avantage d'utiliser des mots de longueur variable, essayant de simuler une occupation normale. la méthode simpliste consistant à copier-coller un court texte plusieurs fois ( « ceci est un faux-texte ceci est un faux-texte ceci est un faux-texte ceci est un faux-texte ceci est un faux-texte » ) a l'inconvénient de ne pas permettre une juste appréciation typographique du résultat final. il circule des centaines de versions différentes du lorem ipsum, mais ce texte aurait originellement été tiré de l'ouvrage de cicéron, de finibus bonorum et malorum ( liber primus ), texte populaire à cette époque, dont l'une des premières phrases est : « neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit... » ( « il n'existe personne qui aime la souffrance pour elle-même, ni qui la recherche ni qui la veuille pour ce qu'elle est... » ). expert en utilisabilité des sites web et des logiciels, jakob nielsen souligne que l'une des limites de l'utilisation du faux-texte dans la conception de sites web est que ce texte n'étant jamais lu, il ne permet pas de vérifier sa lisibilité effective. la lecture à l'écran étant plus difficile, cet aspect est pourtant essentiel. nielsen préconise donc l'utilisation de textes représentatifs plutôt que du lorem ipsum. on peut aussi faire remarquer que les formules conçues avec du faux-texte ont tendance à sous-estimer l'espace nécessaire à une titraille immédiatement intelligible, ce qui oblige les rédactions à formuler ensuite des titres simplificateurs, voire inexacts, pour ne pas dépasser l'espace imparti. contrairement à une idée répandue, le faux-texte ne donne même pas un aperçu réaliste du gris typographique, en particulier dans le cas des textes justifiés : en effet, les mots fictifs employés dans le faux-texte ne faisant évidemment pas partie des dictionnaires des logiciels de pao, les programmes de césure ne peuvent pas effectuer leur travail habituel sur de tels textes. par conséquent, l'interlettrage du faux-texte sera toujours quelque peu supérieur à ce qu'il aurait été avec un texte réel, qui présentera donc un aspect plus sombre et moins lisible que le faux-texte avec lequel le graphiste a effectué ses essais. un vrai texte pose aussi des problèmes de lisibilité spécifiques ( noms propres, numéros de téléphone, retours à la ligne fréquents, composition des citations en italiques, intertitres de plus de deux lignes ... ) qu'on n'observe jamais dans le faux-texte."

def a(aruf):
    return aruf.split()

# print(a(texte))    

jointure = ["coucou", "je", "suis", "un", "texte", "restitué", "!"]

def b(ecrit):
    return ' '.join(ecrit)

# print(b(jointure))

# Etape 2 : fonction c
dictionnaire = {'texte': '1',
 'lorem': '2',
 'qui': '3',
 'donc': '4',
 'est': '5',
 'que': '6',
 'pour': '7',
 'ceci': '8',
 'faux-texte': '9',
 'dans': '10',
 'plus': '11',
 'avec': '12'}

mots = ["mais", "ceci", "est", "un", "faux-texte"]

def c(listeMots, dico):
    changement = []
    for mot in listeMots:
        valeur = dico.get(mot)
        if dico.get(mot) == None:
            changement.append(mot)
        else:
            changement.append(valeur)
    return changement

# print(c(mots, dictionnaire))

# Etape 3 : inverser la clé et la valeur du dictionnaire
def cInverse(tupleuh):
    tupleuh = { valeur : cle for cle, valeur in tupleuh.items() }
    return tupleuh

# print(cInverse(dictionnaire))

# Etape 4 : fonction d et e
texteuh = ['ceci', 'est', 'un', 'faux-texte', 'ceci', 'est']

# newDico = Counter(texteuh)
# print(newDico)

# aSet = set(texteuh)
# print(aSet)

def d(newTxt):
    nouveauDico = {}
    aSet = set(newTxt)
    for s in aSet:
        compter = newTxt.count(s)
        nouveauDico[s] = compter
    return nouveauDico

# print(d(texteuh))

# fonction qui va appeler les autres fonctions pour faire la compression / decompression en un seul clic
def compression(roman):
    separation = a(roman)
    dicotocus = d(separation)
    return dicotocus

print(compression(texte))
