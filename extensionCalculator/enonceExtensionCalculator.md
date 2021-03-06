`En français`

# Extension Calculator

Sujets et notions: gestion de fichiers, récursivité, et arithmétique.

Langage: Python

## Niveau 1 :

Écrire un programme `ExtensionCalculator` en python qui prend en argument le chemin d’un répertoire de la machine.

    > ./extensionCalculator.py myProject/

## Niveau 2 :

Faire en sorte que le programme liste les fichiers du répertoire passé en argument.

    > ./extensionCalculator.py myProject/
    fichiers et repertoires:
    res/
    main.c
    index.js
    data.json

## Niveau 3 :

Chaque fichier sur un disque dur possède une extension, un suffixe, qui définit son type, et sert à identifier son format. Exemple: un fichier “image.png” a pour extension “.png”, qui définit son type comme une image. Ce fichier pourra donc être traité comme une image et affiché par un logiciel de traitement de photo.
Faire en sorte que, en plus de lister les fichiers du répertoire passé en argument, il affiche le nombre de fois qu’une extension du même type apparait.

    > ./extensionCalculator.py myProject/
    fichiers et repertoires:
    res/
    main.c
    index.js
    data.json
    extensions :
    .c 1
    .js 1
    .json 1

## Niveau 4 :

Sur les programmes en ligne de commande UNIX, vous êtes peut-être familier avec le system d’options passés en argument. Exemple: `ls -a`  lance l’execution du programme `ls` qui liste les fichiers d’un répertoire avec l’option `-a`  pour “all” qui affiche aussi les fichiers cachés.
Implementer un system d’options similaire avec `-l` pour lister les fichiers, et `-e`  pour les extensions.
Ainsi, avec l’option `l` on aurait:

    > ./extensionCalculator.py myProject -l
    fichiers et repertoires:
    res/
    main.c
    index.js
    data.json

Avec l’option `e`:

    > ./extensionCalculator.py myProject -e
    extensions :
    .c 1
    .js 1
    .json 1

Avec les deux:

    > ./extensionCalculator.py myProject -l -e
    fichiers et repertoires:
    res/
    main.c
    index.js
    data.json
    extensions :
    .c 1
    .js 1
    .json 1

## Niveau 5 :

Calculer et afficher le pourcentage d’apparition d’une même extension.

    > ./extensionCalculator.py myProject -e
    33% .c
    33% .js
    33% .json

## Niveau 6 :

Ajouter la gestion d’un argument -r qui offre la possibilité de calculer ce pourcentage sur les sous repertoires de manière recursive.

    > ./extensionCalculator.py myProject -e -r
    25% .c
    25% .js
    25% .json
    25% .png

## Niveau bonus :

Ajouter la possibilité d’appliquer ce traitement non pas sur des repertoires du système mais des URLs de repo GitHub.

    ./extensionCalculator.py https://github.com/adatechschool/katas -e -r
    60.4% .py
    14.6% .java
    10.1% .js
    4.9% .html
    4.6% .hs
    4.2% .elm
    1.2% .cpp

`In english`

# Extension Calculator

Topics and notions: file management, recursion, and arithmetic.

Language: Python

## Level 1 :

Write an `ExtensionCalculator` program in python which takes as argument the path of a directory of the machine.

    > ./extensionCalculator.py myProject/

## Level 2 :

Make the program list the files in the directory passed as an argument.

    > ./extensionCalculator.py myProject/
    files and directories:
    res/
    main.c
    index.js
    data.json

## Level 3:

Each file on a hard disk has an extension, a suffix, which defines its type, and is used to identify its format. Example: an “image.png” file has the extension “.png”, which defines its type as an image. This file can therefore be treated as an image and displayed by photo processing software.
Ensure that, in addition to listing the files in the directory passed as an argument, it displays the number of times an extension of the same type appears.

    > ./extensionCalculator.py myProject/
    files and directories:
    res/
    main.c
    index.js
    data.json
    expansions:
    .c 1
    .js 1
    .json 1

## Level 4:

On UNIX command-line programs, you may be familiar with the system of options passed as arguments. Example: `ls -a` launches the execution of the program `ls` which lists the files of a directory with the option `-a` for “all” which also displays the hidden files.
Implement a similar system of options with `-l` for listing files, and `-e` for extensions.
So, with the `l` option we would have:

    > ./extensionCalculator.py myProject -l
    files and directories:
    res/
    main.c
    index.js
    data.json

With the `e` option:

    > ./extensionCalculator.py myProject -e
    expansions:
    .c 1
    .js 1
    .json 1
    
With both:

    > ./extensionCalculator.py myProject -l -e
    files and directories:
    res/
    main.c
    index.js
    data.json
    expansions:
    .c 1
    .js 1
    .json 1

## Level 5:

Calculate and display the percentage of appearance of the same extension.

    > ./extensionCalculator.py myProject -e
    33% .c
    33% .js
    33% .json

## Level 6:

Add the management of an argument -r which offers the possibility of calculating this percentage on the subdirectories in a recursive way.

    > ./extensionCalculator.py myProject -e -r
    25%.c
    25% .js
    25% .json
    25% .png

## Bonus level:

Add the possibility of applying this treatment not to system directories but to GitHub repo URLs.

    ./extensionCalculator.py https://github.com/adatechschool/katas -e -r
    60.4% .py
    14.6% .java
    10.1% .js
    4.9% .html
    4.6%.hs
    4.2% .elm
    1.2% .cpp