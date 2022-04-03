`En français`

## Principe

Il s'agit de recréer le jeu "Puissance 4" : https://fr.wikipedia.org/wiki/Puissance_4

Dans ce jeu, il y a 7 colonnes de 6 lignes, et deux joueurs jouent tour à tour : l'objectif est de créer une ligne de 4 jetons de sa couleur (au moins). Cette ligne peut être verticale, horizontale ou diagonale.

Chaque joueur vient donc glisser un pion dans la colonne de son choix, et ce pion prend automatiquement la première place disponible (tout en bas si la colonne était vide, en deuxième ligne en partant du bas s'il y avait déjà un pion dedans, etc.).

## Niveau 1 - structure

L'objectif est de créer une classe "Partie" qui permette de jouer à Puissance 4 : cette classe aura notamment une méthode "jouer" qui prendra comme paramètre la colonne dans laquelle le joueur actuel veut placer son pion. Il faudra détecter quand un des deux joueurs a gagné, et afficher un message de félicitations pour ce joueur (numéro 1 ou numéro 2).

Par convention, les colonnes seront numérotées de 1 à 7 (de gauche à droite) et c'est le joueur 1 qui commencera.

## Niveau 2 - méthodes

Créer une méthode "afficher" qui affiche la grille de jeu

## Niveau 3 - encapsulation et instanciation

Nous allons maintenant créer une classe Joueur afin que chaque joueur puisse donner son nom en début de partie.

La classe devra aussi contenir le nombre de victoire de chaque joueur et ce compteur devra, bien sûr, être incrémenté à chaque victoire du joueur
Créer pour cela une méthode "hasWon" appelée dans la méthode "jouer" qui vérifie si le coup est gagnant et qui devra incrémenter une valeur dans l'objet du joueur gagnant.

## Niveau 4 - Heritage

Nous allons maintenant créer une nouvelle classe qui devra hériter de la classe Partie mais qui changera les règles de jeu.
Les joueurs doivent pouvoir choisir quel jeu ils lancent au début.

Nous vous proposons une variante où il faut aligner 5 pions et l'affichage se fait avec des couleurs (ou symbole différent), mais vous pouvez imaginer d'autres alternatives !

`In english`

## Principe

It is to recreate the game Connect Four : https://en.wikipedia.org/wiki/Connect_Four

In this game, there is 7 columns of 6 lines, and two players play takes turns : the goal is to create a line of 4 tokens of their color (at less). This line can be vertical, horizontal or diagonal.

Each player therefore slides a pawn into the column of his choice, and this pawn automatically takes the first available place (at the very bottom if the column was empty, in the second line from the bottom if there was already a pawn in it, etc.).

## Step 1 – Structure

The goal is to create a "Game" class that allows you to play Power 4: this class will notably have a "play" method that will take as a parameter the column in which the current player wants to place his pawn. It will be necessary to detect when one of the two players has won, and display a congratulatory message for this player (number 1 or number 2).

By convention, the columns will be numbered from 1 to 7 (from left to right) and player 1 will start.

## Step 2 – Methods

Create a "display" method that displays the game grid

## Step 3 – Encapsulation and instantiation

We are now going to create a Player class so that each player can give their name at the start of the game.

The class must also contain the number of wins of each player and this counter must, of course, be incremented with each victory of the player
To do this, create a "hasWon" method called in the "play" method which checks if the move is a winner and which must increment a value in the object of the winning player.

## Step 4 – Inheritance

We are now going to create a new class which will have to inherit from the Party class but which will change the rules of the game.
Players should be able to choose which game they start at the start.

We offer you a variant where you have to align 5 pawns and the display is done with colors (or different symbol), but you can imagine other alternatives!