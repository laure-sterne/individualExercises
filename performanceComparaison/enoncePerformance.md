`En français`

# Comparaison de performances de langages

## Introduction

Un élément (mais rarement le seul) qui peut influer le choix d'un langage
informatique est sa performance en temps d'exécution.

Nous allons essayer dans cet exercice d'évaluer ce genre de problématique, puis
de comparer deux langages de programmation différents : un compilé (le `C`), un
autre interprété (le `Python`).

## Étape 1 - Évaluer un temps d'exécution

Écrivez en Python une fonction très simple ; par exemple qui fait la somme de
deux arguments entiers.

Créer maintenant une autre fonction pour calculer le temps d'exécution de votre
première fonction. par exemple, votre code peut avoir la forme :

```
def sum(arg1, arg2):
    return arg1 + arg2

def calculate_time():
    start = <... get_current_time>
    sum(2, 3)
    print("Spent time: " + <... get_current_time> - start)
```

Le but est de pouvoir calculer précisément le temps pris par votre fonction.
**Précisément** car il est probable que le temps d'exécution ne soit que de
quelques millisecondes voir microsecondes. Un temps en secondes est donc trop
grossier. Il faudra donc se renseigner, langage par langage, sur le (les ?)
moyen(s) de calculer un temps avec une bonne précision.

## Étape 2 - Fonction lente

Développez maintenant une fonction délibérément complexe, qui va produire
beaucoup de calculs. Le résultat de cette fonction n'a aucun intérêt, il s'agit
simplement de forcer le code à durer un peu plus longtemps.

Par exemple, on peut choisir, à partir d'un entier `N`, de calculer le produit
de chaque entier de 1 jusqu'à `N` avec tous les entiers de 1 jusqu'à `N` :

```
def complex():
    N = 2345
    for i in range(N):
        for j in range(N):
            storage = i * j
```

Remplacer la première fonction très simple développée à l'étape 1 par votre
nouvelle fonction, et modifier la valeur de `number` pour avoir une durée
d'exécution qui soit de l'ordre de quelques secondes (2-3, pas besoin de plus).

## Étape 3 - Équivalent en `C`

Développer maintenant **le même** algorithme en `C`, en utilisant la même
valeur de `number`.

Comparez les résultats. Vous devriez avoir une différence très nette.

## Étape 4 - Autres langages

Essayez d'autres langages : `PHP`, `JavaScript`, ... Vous pourriez être surpris
des résultats, notamment pour ce dernier langage.

`In english`

# Language performance comparison

## Introduction

An element (but rarely the only one) that can influence the choice of a language
computer is its runtime performance.

We are going to try in this exercise to evaluate this kind of problem, then
to compare two different programming languages: a compiled one (the `C`), a
another interpreted (the `Python`).

## Step 1 - Evaluate an execution time

Write a very simple function in Python; for example which is the sum of
two integer arguments.

Now create another function to calculate the execution time of your
first function. for example, your code might look like:

```
def sum(arg1, arg2):
    return arg1 + arg2

def calculate_time():
    start = <... get_current_time>
    sum(2, 3)
    print("Spent time: " + <... get_current_time> - start)
```

The goal is to be able to accurately calculate the time taken by your function.
**Precisely** because the execution time is likely to be only
a few milliseconds or even microseconds. A time in seconds is therefore too much
coarse. It will therefore be necessary to find out, language by language, about the (the?)
means(s) of calculating a time with good precision.

## Step 2 - Slow Function

Now develop a deliberately complex function, which will produce
a lot of calculations. The result of this function is of no interest, it is
just to force the code to last a bit longer.

For example, we can choose, from an integer `N`, to calculate the product
from each integer from 1 to `N` with all integers from 1 to `N`:

```
def complex():
    N = 2345
    for i in range(N):
        for j in range(N):
            storage = i * j
```

Replace the first very simple function developed in step 1 with your
new function, and modify the value of `number` to have a duration
of execution which is of the order of a few seconds (2-3, no need more).

## Step 3 - Equivalent in `C`

Now develop **the same** algorithm in `C`, using the same
value of `number`.

Compare the results. You should have a very clear difference.

## Step 4 - Other languages

Try other languages: `PHP`, `JavaScript`, ... You might be surprised
results, especially for the latter language.