`En français`

# Pimp my ride

## Introduction

La crise du Covid est terminée, la demande en déplacement aérien repart à la hausse, mais toutes les companies ont été laminées et plus personne ne fait tourner d'avion.
Vous vous décidez de vous lancer dans le business avec le Tupolev-114 de votre grand-mère.

Vos clients vous communiquent, en plus de leur nom, des heures de départs, des durées de trajet et le montant payé pour faire ce trajet.
Ces informations sont stockées sous forme d'une chaîne de caractères, par lignes composées de mots représentant, dans l'ordre :

1. le nom du client
2. l'heure de départ du vol
3. la durée du vol
4. le prix

Par exemple, pour une journée, cette chaîne de caractère peut être :

```
Roger 0 5 10
Pongo 3 7 14
Perdita 8 10 8
Anita 16 3 7
```

... la 3e ligne signifiant que la cliente Perdita veut partir à 8h pour un vol de 10h (donc arrivée à 18h) et paiera 8.

Pour optimiser vos journées, vous décidez d'écrire un code calculant l'enchaînement de clients le plus intéressant financièrement.
Il ne faut évidemment pas que l'heure d'arrivée d'un trajet chevauche l'heure de départ d'un autre ! Votre client en retard ne vous paiera pas.

Avec l'exemple précédent, la meilleur combinaison est Pongo (3h -> 10h) et Anita (18h -> 21h) car 14 + 7 = 21.

## Étape 1 - Parsing

Créez une fonction `A` qui prend une ligne du même format que les lignes de l'exemple, la décompose en mot (séparés par un espace) puis range ces mots dans une structure `voyages` que vous déterminerez.

Par exemple - et ce n'est qu'un exemple -, vous pouvez décider de représenter une ligne par un dictionnaire de la forme :
```
{'client': <value>,
 'start': <value>,
 'duration': <value>,
 'price': <value>}
```

Utilisez cette fonction `A` dans une autre fonction `B` prenant en entrée une journée complète (donc plusieurs lignes) et retournant une liste de structures `voyages` définies précédemment.

Pour reprendre le texte d'exemple, et la structure proposée précédemment, le résultat de cette fonction serait :

```
[ {'client': 'Roger', 'start': 0, 'duration': 5, 'price: 10},
  {'client': 'Pongo', 'start': 3, 'duration': 7, 'price: 14},
  {'client': 'Perdita', 'start': 8, 'duration': 10, 'price: 8},
  {'client': 'Anita', 'start': 16, 'duration': 3, 'price: 7} ]
```

Vous aurez donc à ce niveau ce qu'on appelle un parser, recevant en entrée une chaîne de caractères représentant une journée de vols, et donnant en sortie une représentation structurée de ces données, vous permettant de travailler plus simplement avec.

## Étape 2 - Prix

Créez une fonction `C` qui accepte en argument une liste de `voyages` et retourne la somme des prix de ces `voyages`.

Par exemple, `C([ {'client': 'Roger', 'start': 0, 'duration': 5, 'price: 10}, {'client': 'Pongo', 'start': 3, 'duration': 7, 'price: 14} ])` retourne *10 + 14 = 24*.

## Étape 3 - Compatibilité

Créez une fonction `D` qui comparent deux structures `voyages` et retourne un booléen déterminant si les structures sont compatibles ou non.

Il s'agit de déterminer si un vol (représenté par une structure `voyages`) n'empiète pas sur les horaires d'un autre.

Par exemple, `D({'client': 'Roger', 'start': 0, 'duration': 5, 'price: 10}, {'client': 'Pongo', 'start': 3, 'duration': 7, 'price: 14})` doit retourner **faux** : en effet, le premier vol n'atterrit qu'à 5h, ce qui est incompatible avec le départ du second à 3h.

En revanche, `D({'client': 'Roger', 'start': 0, 'duration': 5, 'price: 10}, {'client': 'Perdita', 'start': 8, 'duration': 10, 'price: 8})` retourne **vrai**.

## Étape 4 - Lister les possibilités

Développez une fonction `E` qui retourne, à partir d'une liste de `voyages`, **tous** les ensembles de `voyages` compatibles les uns avec les autres.

En partant de l'exemple original, cette fonction `E` retournerait alors :

```
[
  [ {'client': 'Roger', 'start': 0, 'duration': 5, 'price: 10} ], // chaque voyage est compatible avec lui-même
  [ {'client': 'Pongo', 'start': 3, 'duration': 7, 'price: 14} ],
  [ {'client': 'Perdita', 'start': 8, 'duration': 10, 'price: 8} ],
  [ {'client': 'Anita', 'start': 16, 'duration': 3, 'price: 7} ],
  [ {'client': 'Roger', 'start': 0, 'duration': 5, 'price: 10}, {'client': 'Perdita', 'start': 8, 'duration': 10, 'price: 8} ],
  [ {'client': 'Roger', 'start': 0, 'duration': 5, 'price: 10}, {'client': 'Anita', 'start': 16, 'duration': 3, 'price: 7} ],
  [ {'client': 'Pongo', 'start': 3, 'duration': 7, 'price: 14}, {'client': 'Anita', 'start': 16, 'duration': 3, 'price: 7} ],
]
```

La fonction `D` vous sera bien utile !

## Étape 5 - Le choix final

Développez une dernière fonction qui, à partir du résultat de la fonction `E`, et en utilisant la fonction `C`, détermine l'ensemble de `voyages` optimal du point de vue financier.

Vous avez alors tous les outils pour déterminer, à partir d'une chaîne de caractères des vols d'une journée, la liste optimale des clients à transporter, les horaires de leurs vols, ainsi que votre gain !

`In english`

# Pimp my ride

## Introduction

The Covid crisis is over, the demand for air travel is on the rise again, but all the companies have been wiped out and no one is running a plane anymore.
You decide to go into business with your grandmother's Tupolev-114.

Your customers communicate to you, in addition to their name, departure times, journey times and the amount paid for this journey.
This information is stored in the form of a character string, in lines made up of words representing, in order:

1. customer name
2. flight departure time
3. the duration of the flight
4. the price

For example, for a day, this character string can be:

```
Roger 0 5 10
pongo 3 7 14
Lost 8 10 8
Anita 16 3 7
```

... the 3rd line meaning that the client Perdita wants to leave at 8 a.m. for a 10 a.m. flight (therefore arriving at 6 p.m.) and will pay 8.

To optimize your days, you decide to write a code calculating the most financially interesting sequence of customers.
Of course, the arrival time of one trip must not overlap the departure time of another! Your late client will not pay you.

With the previous example, the best combination is Pongo (3 a.m. -> 10 a.m.) and Anita (6 p.m. -> 9 p.m.) because 14 + 7 = 21.

## Step 1 - Parsing

Create an `A` function that takes a line of the same format as the lines in the example, breaks it down into words (separated by a space) and then stores these words in a `trips` structure that you determine.

For example - and this is just one example - you can decide to represent a line by a dictionary of the form:
```
{'customer': <value>,
 'start': <value>,
 'duration': <value>,
 'price': <value>}
```

Use this `A` function inside another `B` function taking as input a full day (so several rows) and returning a list of previously defined `trips` structures.

To use the example text, and the structure proposed above, the result of this function would be:

```
[ {'customer': 'Roger', 'start': 0, 'duration': 5, 'price: 10},
  {'customer': 'Pongo', 'start': 3, 'duration': 7, 'price: 14},
  {'customer': 'Perdita', 'start': 8, 'duration': 10, 'price: 8},
  {'customer': 'Anita', 'start': 16, 'duration': 3, 'price: 7} ]
```

You will therefore have at this level what is called a parser, receiving as input a character string representing a day of flights, and giving as output a structured representation of this data, allowing you to work with it more simply.

## Step 2 - Price

Create a `C` function that accepts a list of `trips` as an argument and returns the sum of the prices of these `trips`.

For example, `C([ {'customer': 'Roger', 'start': 0, 'duration': 5, 'price: 10}, {'customer': 'Pongo', 'start': 3, ' duration': 7, 'price: 14} ])` returns *10 + 14 = 24*.

## Step 3 - Compatibility

Create a `D` function that compares two `trips` structures and returns a boolean determining whether the structures are compatible or not.

This is to determine if one flight (represented by a `trips` structure) does not encroach on the schedules of another.

For example, `D({'client': 'Roger', 'start': 0, 'duration': 5, 'price: 10}, {'client': 'Pongo', 'start': 3, 'duration ': 7, 'price: 14})` must return **false**: indeed, the first flight only lands at 5am, which is incompatible with the departure of the second at 3am.

In contrast, `D({'client': 'Roger', 'start': 0, 'duration': 5, 'price: 10}, {'client': 'Perdita', 'start': 8, 'duration ': 10, 'price: 8})` returns **true**.

## Step 4 - List the possibilities

Develop a function `E` that returns, from a list of `trips`, **all** sets of `trips` compatible with each other.

Starting from the original example, this `E` function would then return:

```
[
  [ {'client': 'Roger', 'start': 0, 'duration': 5, 'price: 10} ], // chaque voyage est compatible avec lui-même
  [ {'client': 'Pongo', 'start': 3, 'duration': 7, 'price: 14} ],
  [ {'client': 'Perdita', 'start': 8, 'duration': 10, 'price: 8} ],
  [ {'client': 'Anita', 'start': 16, 'duration': 3, 'price: 7} ],
  [ {'client': 'Roger', 'start': 0, 'duration': 5, 'price: 10}, {'client': 'Perdita', 'start': 8, 'duration': 10, 'price: 8} ],
  [ {'client': 'Roger', 'start': 0, 'duration': 5, 'price: 10}, {'client': 'Anita', 'start': 16, 'duration': 3, 'price: 7} ],
  [ {'client': 'Pongo', 'start': 3, 'duration': 7, 'price: 14}, {'client': 'Anita', 'start': 16, 'duration': 3, 'price: 7} ],
]
```

The `D` function will be very useful to you!

## Step 5 - The final choice

Develop a final function which, from the result of the `E` function, and using the `C` function, determines the financially optimal set of `trips`.

You then have all the tools to determine, from a string of one-day flights, the optimal list of customers to transport, the times of their flights, as well as your profit!