`En français`

# Compression de texte

## Introduction

Cet exercice traite de la compression, qui est un procédé permettant de représenter une certaine quantité d'information en utilisant et en occupant un espace plus petit qu'originellement.

Il existe plusieurs type de compression, dans cet exercice nous nous intéresserons à la compression :

- **sans perte**, c'est à dire que le résultat final ne sera pas dégradé par rapport à l'information originelle ;
- **par dictionnaire**, c'est à dire que nous gagnerons de la place en remplaçant certaines bribes d'information par une référence plus courte.
  Nous stockerons cette référence et la bribe associée dans un dictionnaire, afin de nous permettre de reconstruire l'information originelle lors d'une étape de décompression.

Nous nous baserons sur le texte d'exemple suivant :

----

généralement, on utilise un texte en faux latin ( le texte ne veut rien dire, il a été modifié ), le lorem ipsum ou lipsum, qui permet donc de faire office de texte d'attente. l'avantage de le mettre en latin est que l'opérateur sait au premier coup d'oeil que la page contenant ces lignes n'est pas valide, et surtout l'attention du client n'est pas dérangée par le contenu, il demeure concentré seulement sur l'aspect graphique. ce texte a pour autre avantage d'utiliser des mots de longueur variable, essayant de simuler une occupation normale. la méthode simpliste consistant à copier-coller un court texte plusieurs fois ( « ceci est un faux-texte ceci est un faux-texte ceci est un faux-texte ceci est un faux-texte ceci est un faux-texte » ) a l'inconvénient de ne pas permettre une juste appréciation typographique du résultat final. il circule des centaines de versions différentes du lorem ipsum, mais ce texte aurait originellement été tiré de l'ouvrage de cicéron, de finibus bonorum et malorum ( liber primus ), texte populaire à cette époque, dont l'une des premières phrases est : « neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit... » ( « il n'existe personne qui aime la souffrance pour elle-même, ni qui la recherche ni qui la veuille pour ce qu'elle est... » ). expert en utilisabilité des sites web et des logiciels, jakob nielsen souligne que l'une des limites de l'utilisation du faux-texte dans la conception de sites web est que ce texte n'étant jamais lu, il ne permet pas de vérifier sa lisibilité effective. la lecture à l'écran étant plus difficile, cet aspect est pourtant essentiel. nielsen préconise donc l'utilisation de textes représentatifs plutôt que du lorem ipsum. on peut aussi faire remarquer que les formules conçues avec du faux-texte ont tendance à sous-estimer l'espace nécessaire à une titraille immédiatement intelligible, ce qui oblige les rédactions à formuler ensuite des titres simplificateurs, voire inexacts, pour ne pas dépasser l'espace imparti. contrairement à une idée répandue, le faux-texte ne donne même pas un aperçu réaliste du gris typographique, en particulier dans le cas des textes justifiés : en effet, les mots fictifs employés dans le faux-texte ne faisant évidemment pas partie des dictionnaires des logiciels de pao, les programmes de césure ne peuvent pas effectuer leur travail habituel sur de tels textes. par conséquent, l'interlettrage du faux-texte sera toujours quelque peu supérieur à ce qu'il aurait été avec un texte réel, qui présentera donc un aspect plus sombre et moins lisible que le faux-texte avec lequel le graphiste a effectué ses essais. un vrai texte pose aussi des problèmes de lisibilité spécifiques ( noms propres, numéros de téléphone, retours à la ligne fréquents, composition des citations en italiques, intertitres de plus de deux lignes ... ) qu'on n'observe jamais dans le faux-texte.

----


## Étape 1 - Découper et reconstruire le texte

### Découpage

Nous allons tout d'abord transformer le texte pour le rendre plus facilement manipulable.

Créez une fonction `A` (donnez-lui le nom que vous voulez, c'est simplement pour y faire référence dans cet exercice) prenant en paramètre ce texte (ou tout autre chaîne de caractères) et retourne une liste de mots.

Nous définissons un mot comme un ensemble de caractères, quels qu'ils soient, à l'exception des espaces, qui séparent les mots entre eux.
Par exemple, pour le texte suivant :

```
----
qu'elle est... » ). expert en utilisabilité des
----
```

... la liste des mots est : `['qu'elle', 'est...', '»', ').', 'expert', 'en', 'utilisabilité', 'des']`.

Il est possible d'utiliser la fonction `split`, présente dans de nombreux langages (souvent sous forme de méthode du type `String`), ou tout autre équivalent.

### Reconstruction

Créez également une fonction `B` prenant en paramètre une liste de mots, et retournant une chaîne de charactère composée de l'ensemble des mots dans l'ordre, séparés par un espace.

Cette fonction est "l'inverse" de la fonction `A` créée à l'étape **Découpage** : actuellement, sans aucune modification des mots, elle vous permet de reformer le texte originel à partir du résultat de la fonction `A`.


## Étape 2 - Compression avec dictionnaire fixe

Nous allons maintenant remplacer certains mots du texte par des références.

Nous utiliserons le dictionnaire suivant :

```
{'texte': '1',
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
```

Créez une fonction `C` prennant en paramètre une liste de mots et un dictionnaire.

Pour chaque mot dans la liste, si le mot existe dans le dictionnaire en tant que clef, remplacez-le par la valeur associée.

Par exemple, avec le dictionnaire précédent et la liste `['mais', 'ceci', 'est', 'un', 'long', 'faux-texte']`, la fonction doit retourner `['mais', '8', '5', 'un', 'long', '9']`.

Vous pouvez maintenant enchaîner vos fonctions `A`, `C` et `B` pour produire un nouveau texte :

- `A` divise le texte originel en liste de mots,
- `C` remplace certains de ces mots par les références du dictionnaire,
- `B` récupère la liste de mots et reconstruit un texte complet.

Vous venez de compresser le texte !


## Étape 3 - Décompression

Le texte produit à l'étape 3 est certe plus court, mais il n'est pas lisible en l'état. Il faut donc passer par une étape de décompression : remplacer les références par les mots originels.

C'est le but de cette étape.

On peut penser intuitivement que l'étape de substitution des références par les mots originels est très proche de ce que faisait la fonction `C`, et c'est vrai !

À un détail près, qui est que maintenant les mots que nous cherchons dans le texte ne sont plus les clefs du dictionnaire, mais ses valeurs.

Pour résoudre ce détail, il y a une possibilité simple : "inverser" le dictionnaire, par exemple transformer `{'texte': '1', 'lorem': '2'}` en `{'1': 'texte', '2': 'lorem'}`. Dans ce cas, la fonction `C` peut être utilisée directement : il suffit de changer le dictionnaire passé en argument.

Il est bien évidemment possible d'y arriver en ne gardant qu'un seul dictionnaire.

Dans tous les cas, vous avez maintenant un ensemble de fonction vous permettant de compresser et décompresser le texte.

Prenez un peu de temps pour analyser le gain de place de votre compression. Vous pouvez également ajouter ou enlever des mots de votre dictionnaire pour évaluer leurs impacts.


## Étape 4 - Un meilleur dictionnaire

Le dictionnaire proposé est loin d'être complet, et même s'il l'était, peut-être ne serait-il pas adapté à tous les textes.

Nous allons donc faire une fonction pour générer notre propre dictionnaire.

Créez une fonction `D` qui prend en paramètre une liste de mots, et retourne un dictionnaire dont les clefs sont les mots du texte, et les valeurs leur nombre d'apparition.

Par exemple, avec la liste `['ceci', 'est', 'un', 'faux-texte', 'ceci', 'est']`, la fonction retournera : `{'ceci': 2, 'est': 2, 'un': 1, 'faux-texte': 1}`.

Cette fonction vous permet de voir quels mots apparaissent le plus souvent dans le texte, et s'il est efficace de les remplacer par une référence : par exemple, remplacer le mot `'un'` par la référence `'254'` n'entraîne pas de gain de place, mais au contraire une perte !

À partir de vos observations, construisez un dictionnaire plus riche que celui proposé en exemple, tester votre compression / décompression et regardez le gain de place.

Il vous est également possible de générer automatiquement un dictionnaire de références à partir des contraintes de votre choix, par exemple *"je ne veux remplacer que les mots de plus de 3 caractères qui apparaissent au moins 2 fois"*.

Il vous faut pour cela une fonction `E` qui prend en paramètre un dictionnaire de nombre d'apparition des mots, et qui retourne un dictionnaire de référence.

Par exemple, si vous ne voulez que substituer les mots de plus de 3 caractères qui apparaissent au moins 2 fois, avec l'argument `{'avec': 3, 'tous': 1, 'un': 23, 'nuit': 10}`, la fonction retournera : `{'avec': '1', 'nuit': '2'}`.

Vous pouvez donc, à partir de ces contraintes, filtrer le dictionnaire produit par votre fonction `D`, puis associer à chacun des mots conservés une référence unique

Lorsque vous avez cette fonction, vous aurez un code de compression adaptatif au texte compressé :

- `A` divise le texte originel en liste de mots,
- `D` analyse cette liste de mot pour construire un dictionnaire du nombre d'apparition des mots,
- `E` utilise ce dictionnaire pour produire un dictionnaire de références,
- `C` remplace certains de ces mots par les références du dictionnaire de références produit par `E`,
- `B` récupère la liste de mots et reconstruit un texte compressé complet.

À partir de ça, essayer de changer les contraintes de génération de votre dictionnaire de référence, pour trouver les paramètres les plus efficaces !

## Étape 5 - ...

Essayez votre code de compression sur d'autres textes. Attention : jusqu'à présent, un certain nombre de subtilités n'étaient pas traitées, car le texte était simplifié :

- absence de saut de ligne,
- absence de majuscule,
- absence de nombre (qui rentrent en colision avec les références utilisées dans le dictionnaire de compression),
- espaces ajoutés autour de certains caractère (comme autour des parenthèses `(`, `)`),
- ...

`In english`

# Text compression

## Introduction

This exercise deals with compression, which is a process for representing a certain amount of information by using and occupying a smaller space than originally.

There are several types of compression, in this exercise we will focus on compression:

- **lossless**, ie the final result will not be degraded compared to the original information;
- **by dictionary**, ie we will save space by replacing certain snippets of information with a shorter reference.
  We will store this reference and the associated snippet in a dictionary, in order to allow us to reconstruct the original information during a decompression step.

We will base ourselves on the following example text:

----

généralement, on utilise un texte en faux latin ( le texte ne veut rien dire, il a été modifié ), le lorem ipsum ou lipsum, qui permet donc de faire office de texte d'attente. l'avantage de le mettre en latin est que l'opérateur sait au premier coup d'oeil que la page contenant ces lignes n'est pas valide, et surtout l'attention du client n'est pas dérangée par le contenu, il demeure concentré seulement sur l'aspect graphique. ce texte a pour autre avantage d'utiliser des mots de longueur variable, essayant de simuler une occupation normale. la méthode simpliste consistant à copier-coller un court texte plusieurs fois ( « ceci est un faux-texte ceci est un faux-texte ceci est un faux-texte ceci est un faux-texte ceci est un faux-texte » ) a l'inconvénient de ne pas permettre une juste appréciation typographique du résultat final. il circule des centaines de versions différentes du lorem ipsum, mais ce texte aurait originellement été tiré de l'ouvrage de cicéron, de finibus bonorum et malorum ( liber primus ), texte populaire à cette époque, dont l'une des premières phrases est : « neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit... » ( « il n'existe personne qui aime la souffrance pour elle-même, ni qui la recherche ni qui la veuille pour ce qu'elle est... » ). expert en utilisabilité des sites web et des logiciels, jakob nielsen souligne que l'une des limites de l'utilisation du faux-texte dans la conception de sites web est que ce texte n'étant jamais lu, il ne permet pas de vérifier sa lisibilité effective. la lecture à l'écran étant plus difficile, cet aspect est pourtant essentiel. nielsen préconise donc l'utilisation de textes représentatifs plutôt que du lorem ipsum. on peut aussi faire remarquer que les formules conçues avec du faux-texte ont tendance à sous-estimer l'espace nécessaire à une titraille immédiatement intelligible, ce qui oblige les rédactions à formuler ensuite des titres simplificateurs, voire inexacts, pour ne pas dépasser l'espace imparti. contrairement à une idée répandue, le faux-texte ne donne même pas un aperçu réaliste du gris typographique, en particulier dans le cas des textes justifiés : en effet, les mots fictifs employés dans le faux-texte ne faisant évidemment pas partie des dictionnaires des logiciels de pao, les programmes de césure ne peuvent pas effectuer leur travail habituel sur de tels textes. par conséquent, l'interlettrage du faux-texte sera toujours quelque peu supérieur à ce qu'il aurait été avec un texte réel, qui présentera donc un aspect plus sombre et moins lisible que le faux-texte avec lequel le graphiste a effectué ses essais. un vrai texte pose aussi des problèmes de lisibilité spécifiques ( noms propres, numéros de téléphone, retours à la ligne fréquents, composition des citations en italiques, intertitres de plus de deux lignes ... ) qu'on n'observe jamais dans le faux-texte.

----

## Step 1 - Cut and reconstruct the text

### Cutting

We will first transform the text to make it easier to manipulate.

Create a function `A` (give it the name you want, it's just to refer to it in this exercise) taking as parameter this text (or any other character string) and returns a list of words.

We define a word as a set of characters, whatever they are, with the exception of spaces, which separate words from each other.
For example, for the following text:

```
----
qu'elle est... » ). expert en utilisabilité des
----
```

... the list of words is: `['that she', 'is...', '»', ').', 'expert', 'in', 'usability', 'des']` .

It is possible to use the `split` function, present in many languages ​​(often in the form of a method of the `String` type), or any other equivalent.

### Rebuilding

Also create a function `B` taking as parameter a list of words, and returning a character string composed of all the words in order, separated by a space.

This function is the "inverse" of the `A` function created in the **Cutting** step: currently, without any modification of the words, it allows you to reform the original text from the result of the `A function `.


## Step 2 - Compression with fixed dictionary

We will now replace some words in the text with references.

We will use the following dictionary:

```
{'texte': '1',
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
```
Create a `C` function taking as parameters a list of words and a dictionary.

For each word in the list, if the word exists in the dictionary as a key, replace it with the associated value.

For example, with the previous dictionary and the list `['but', 'this', 'is', 'a', 'long', 'false-text']`, the function must return `['but', '8', '5', 'one', 'long', '9']`.

You can now chain your `A`, `C` and `B` functions together to produce new text:

- `A` divides the original text into a list of words,
- `C` replaces some of these words with dictionary references,
- `B` retrieves the list of words and reconstructs a complete text.

You have just compressed the text!


## Step 3 - Decompression

The text produced in step 3 is certainly shorter, but it is not readable as it is. It is therefore necessary to go through a decompression stage: replace the references with the original words.

This is the purpose of this step.

We can intuitively think that the step of replacing the references by the original words is very close to what the `C` function did, and it's true!

With one detail, which is that now the words we are looking for in the text are no longer the keys of the dictionary, but its values.

To solve this detail, there is a simple possibility: "invert" the dictionary, for example transform `{'text': '1', 'lorem': '2'}` into `{'1': 'text' , '2': 'lorem'}`. In this case, the `C` function can be used directly: all you have to do is change the dictionary passed as an argument.

It is of course possible to achieve this by keeping only one dictionary.

In any case, you now have a set of functions allowing you to compress and decompress the text.

Take some time to analyze the space saving of your compression. You can also add or remove words from your dictionary to assess their impact.


## Step 4 - A Better Dictionary

The proposed dictionary is far from being complete, and even if it were, perhaps it would not be suitable for all texts.

So we are going to make a function to generate our own dictionary.

Create a `D` function which takes a list of words as a parameter, and returns a dictionary whose keys are the words of the text, and the values ​​their number of occurrences.

For example, with the list `['this', 'is', 'a', 'false-text', 'this', 'is']`, the function will return: `{'this': 2, 'is ': 2, 'one': 1, 'dummy-text': 1}`.

This function allows you to see which words appear most often in the text, and if it is effective to replace them with a reference: for example, replacing the word `'un'` with the reference `'254'` n' does not result in a gain of space, but on the contrary a loss!

From your observations, build a richer dictionary than the one proposed as an example, test your compression / decompression and watch the space saving.

You can also automatically generate a dictionary of references from the constraints of your choice, for example *"I only want to replace words longer than 3 characters that appear at least twice"*.

You need for that a function `E` which takes in parameter a dictionary of number of appearance of the words, and which returns a dictionary of reference.

For example, if you only want to substitute words longer than 3 characters that appear at least 2 times, with the argument `{'with': 3, 'all': 1, 'one': 23, 'night' : 10}`, the function will return: `{'with': '1', 'night': '2'}`.

You can therefore, from these constraints, filter the dictionary produced by your `D` function, then associate with each of the words kept a unique reference

When you have this function, you will have a compression code adaptive to the compressed text:

- `A` divides the original text into a list of words,
- `D` analyzes this list of words to build a dictionary of the number of occurrences of words,
- `E` uses this dictionary to produce a dictionary of references,
- `C` replaces some of these words with references from the dictionary of references produced by `E`,
- `B` recovers the list of words and reconstructs a complete compressed text.

From there, try to change the generation constraints of your reference dictionary, to find the most efficient parameters!

## Step 5 - ...

Try your compression code on other texts. Attention: until now, a certain number of subtleties were not treated, because the text was simplified:

- no line break,
- absence of capital letters,
- absence of numbers (which collide with the references used in the compression dictionary),
- spaces added around certain characters (like around parentheses `(`, `)`),
- ...