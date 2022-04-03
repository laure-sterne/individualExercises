`En français`

Pour cet exercice, le choix du langage est libre. 

### Présentation de l'exercice :

L'exercice consiste à "décrire" des chaînes de caractères selon le principe suivant :

<ul>
<li>Prenons la chaîne de caractères "a". Celle-ci est composée d'une (1) occurrence du caractère 'a'. Nous pouvons donc décrire la chaîne "a" par la chaîne "1a".
<li>Prenons désormais la nouvelle chaîne "1a". Celle-ci est composée d'un (1) caractère '1' puis d'un (1) caractère 'a'. Nous pouvons donc la décrire par "111a".
<li>De même, la chaîne "111a" est composée de 3 caractères consécutifs '1' puis d'un (1) caractère 'a'. Nous pouvons donc la décrire comme "311a"
<li>et ainsi de suite...
</ul>

Si on représente les chaînes successives verticalement, où chaque chaîne décrit la précédente, nous obtenons : 
<br/>a
<br/>1a
<br/>111a
<br/>311a
<br/>13211a
<br/>111312211a
<br/>...

Une telle suite s'appelle [Suite de Conway] (https://fr.wikipedia.org/wiki/Suite_de_Conway) ou suite "audioactive".

L'objectif de l'exercice est de réaliser un générateur de suites de Conway.


### Etape 1:
Créer une fonction `decoupeChaine` qui prend en paramètre une string et renvoie la même string dans laquelle les caractères successifs non identiques sont séparés par un espace.

Ex :

    decoupeChaine("ab")     // renvoie "a b"
    decoupeChaine("aabbca") // renvoie "aa bb c a"

### Etape 2:
Créer une fonction `decritChaine`, inspirée de `decoupeChaine`, qui prend en paramètre une string et renvoie une string qui décrit, tel qu'expliqué ci-dessus, les caractères qui constituent la chaîne en paramètre.

Ex:

    decritChaine("ab")      // renvoie "1a1b"
    decritChaine("aabbca")  // renvoie "2a2b1c1a"

### Etape 3:
Créer une fonction `suiteConway` qui donne les `n` premiers termes de la suite qui commence par le caractère `carac`. `n` et `carac` sont passés en paramètres de la fonction.

Ex:

    suiteConway('a', 3)  
    a
    1a
    111a

    suiteConway('1', 3)  
    1
    11
    21
    
### Etape 4:
Afficher la suite de Conway générée dans un navigateur. Utiliser un texte centré pour l'afficher sous forme de pyramide.

`In english`

For this exercise, the choice of language is free.

### Presentation of the exercise:

The exercise consists in "describing" character strings according to the following principle:

<ul>
<li>Let's take the string "a". This is composed of one (1) occurrence of the character 'a'. So we can describe the string "a" by the string "1a".
<li>Now take the new string "1a". This is composed of one (1) character '1' then one (1) character 'a'. We can therefore describe it as "111a".
<li>Similarly, the string "111a" is composed of 3 consecutive '1' characters and then one (1) 'a' character. So we can describe it as "311a"
<li>and so on...
</ul>

If we represent the successive chains vertically, where each chain describes the previous one, we obtain:
<br/>a
<br/>1a
<br/>111a
<br/>311a
<br/>13211a
<br/>111312211a
<br/>...

Such a suite is called [Conway's Suite] (https://fr.wikipedia.org/wiki/Conway_Suite) or "audioactive" suite.

The objective of the exercise is to create a generator of Conway sequences.


### Step 1:
Create a `cutString` function which takes a string as a parameter and returns the same string in which successive non-identical characters are separated by a space.

Eg:

    cutString("ab") // returns "a b"
    cutString("aabbca") // returns "aa bb c a"

### Step 2:
Create a `decritString` function, inspired by `cutString`, which takes a string as parameter and returns a string which describes, as explained above, the characters that make up the string as parameter.

Ex:

    describeString("ab") // returns "1a1b"
    describeString("aabbca") // returned "2a2b1c1a"

### Step 3:
Create a `suiteConway` function that returns the first `n` terms of the sequence that start with the character `charac`. `n` and `charac` are passed as function parameters.

Ex:

    conway('a', 3)
    a
    1a
    111a

    conway('1', 3)
    1
    11
    21
    
### Step 4:
Display Conway's suite issued in a browser. Use centered text to display it as a pyramid.