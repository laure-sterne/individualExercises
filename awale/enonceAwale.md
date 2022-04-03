`En français`

## Étape 0: Avant de commencer...
Cette exercice vise à reproduire le jeu Awalé (ou Awelé) en adoptant une approche orientée objet. Aucun langage n'est imposé, seul le paradigme. Il est donc recommandé de partir sur un langage orienté objet ou un langage multi paradigme qui le supporte.
Vidéo explicative des règles du jeu : https://www.youtube.com/watch?v=J0c-vE-X1x8 (1m30)

## Étape 1: Le plateau de jeu, les bases
- Écrire la classe et les attributs qui matérialisera le plateau de jeu: les cases et les lettres
Il va donc falloir trouver une structure de donnée adaptée au format du plateau où chaque case va devoir contenir un nombre defini de graines
Le lettres servent à pointer une case.
- Y ajouter une première fonction display: affichage du plateau dans la console
- Une seconde fonction isEmpty: le plateau est-il vide ? (toutes les cases à zero)
```
     A  B  C  D  E  F
    (0)(0)(0)(0)(0)(0)
    (0)(0)(0)(0)(0)(0)
     G  H  I  J  K  L
```

## Étape 2: La representation du joueur
- Écrire la classe et les attributs qui serviront à représenter le joueur.
- Ajouter une fonction d'increment du score

## Étape 3: Le début de la fin, la logique de semer/recolter les graines
Voici le coeur du jeu. Notez bien que semer se fait dans un sens et récolter, dans l'autre.
Ces fonctions vont donc devoir s'ajouter à la classe du platedau de jeu.
- saw: semer les graines d'une case aux suivantes
- harvest: recolter les graines d'une case et des precedentes
Il est recommandé de creer une fonction qui retourne la case suivante, en parcourant le plateau de jeu dans un sens ou dans l'autre. Cette (ou ces fonctions si vous en faite deux: une pour un sens et une autre pour l'autre) pourra donc être appelée par les fonctions de saw/harvest.

## Étape 4: Le jeu
- Maintenant que le plus dur est passé, creer la classe et les attributs pour materialiser le jeu. Prendre en compte deux joueurs et une gestion des tours.
Il va donc falloir antinciper:
- l'affichage du plateau et des cores
- la demande demande de saisie et boucle de jeu.
- la gestion de la fin du jeu. Pour un souci de simplicité, on assumera que le jeu se termine quand le plateau et vide.

`In english`

## Step 0: Before you begin...
This exercise aims to reproduce the Awalé (or Awelé) game by adopting an object-oriented approach. No language is imposed, only the paradigm. It is therefore recommended to start with an object-oriented language or a multi-paradigm language that supports it.
Explanatory video of the rules of the game: https://www.youtube.com/watch?v=J0c-vE-X1x8 (1m30)

## Step 1: The game board, the basics
- Write the class and attributes that will materialize the game board: boxes and letters
It will therefore be necessary to find a data structure adapted to the format of the board where each box will have to contain a defined number of seeds
The letters are used to point a box.
- Add a first display function: display of the tray in the console
- A second isEmpty function: is the board empty? (all boxes zero)
```
     A B C D E F
    (0)(0)(0)(0)(0)(0)
    (0)(0)(0)(0)(0)(0)
     G H I J K L
```

## Step 2: The player representation
- Write the class and attributes that will be used to represent the player.
- Add score increment function

## Step 3: The beginning of the end, the logic of sowing/reaping the seeds
Here is the heart of the game. Note that sowing is done in one direction and reaping in the other.
These functions will therefore have to be added to the class of the game board.
- saw: sow seeds from one box to the next
- harvest: harvest the seeds of a square and the previous ones
It is recommended to create a function that flips the next square, traversing the game board in one direction or the other. This (or these functions if you make two: one for one direction and another for the other) can therefore be called by the saw/harvest functions.

## Step 4: The Game
- Now that the hardest part is over, create the class and attributes to materialize the game. Take into account two players and turn management.
We will therefore have to anticipate:
- display of the board and cores
- the request input request and game loop.
- the management of the end of the game. For the sake of simplicity, we will assume that the game ends when the board is empty.