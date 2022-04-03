`En français`

## Langage : Libre

Cet exercice individuel consiste à écrire la logique d'un jeu de poker suivant les règles du Texas hold'em.

# Niveau 1

Écrire une fonction `createDeck` qui génère un deck de 52 cartes à jouer sous forme d'un tableau de chaines de caractères type "1♠︎" ou "V♣︎". Utiliser une fonction qui mélange automatiquement le tableau de carte (le javascript ne possède pas de fonction shuffle. Chercher un equivalent ou une implementation).
Rappel : les cartes vont de 1 (As) à 10 puis Valet (J), Dame (Q) et Roi (K). Les types sont ♠︎♣︎♡♢.

# Niveau 2

Pour la suite, un deck sera déclaré et stocké dans une constante `deck`.
Écrire une fonction `deal` qui distribue (et donc retire du deck) un nombre de carte, le nombre doit être donné en paramètre.
Créer une variable par joueur. Chaque joueur doit recevoir 2 cartes.
Partant sur 2 joueurs, on aura donc :

	const player1 = deal(2)
    const player2 = deal(2)


# Niveau 3

Écrire une fonction `flop` qui retournera le flop, c'est à dire les 5 cartes posés au centre du jeu, communes à tous les joueurs. La fonction utilisera la fonction `deal` et exécutera les tours comme un veritable croupier, en brulant les cartes entre chaque.

Les tours sont composés de la manière suivante :
Premier tour = 1 carte brulés, 3 cartes sorties;
Deuxième tour = 1 carte brulés, 1 carte sortie;
Troisième tour = 1 carte brulés, 1 carte sortie.

Cartes tirés seront stockés dans une variable `cards`.

# Niveau 4

Écrire une fonction `showdown` qui affichera la main d'un joueur. Elle prendra donc, en premier paramètre, les deux cartes d'un joueur, et en second le flop (`cards` déclaré en niveau 3).
Une main de joueur peut posséder les éléments suivants : une ou deux paires, un brelan, un carré, une couleur, une suite ou une quinte.

Pour plus de détails, voir la [page Wikipédia](https://fr.wikipedia.org/wiki/Main_au_poker#Ordre_des_niveaux_des_mains) sur les mains au poker.

Exemple d'usage :

    const deck = createDeck() // ["1♡", "8♦︎" ...]
    const p1 = deal(2)        // ["10♡", "K♧"]
    const p2 = deal(2)        // ["8♦︎", "5♧"]
    let cards = flop()        // ["J♡", "K♦︎", "7♠︎" ...]
    showdown(p1, flop)
    showdown(p2, flop)


Affichera :

    hand: ["10♡", "K♧", "J♡", "K♦︎", "7♠︎" ... ]
    > brelan de 10
    hand: ["8♦︎", "5♧", "J♡", "K♦︎", "7♠︎" ... ]
    > brelan de 10

`In english`

## Language: Free

This individual exercise consists of writing the logic of a poker game following the rules of Texas hold'em.

# Level 1

Write a `createDeck` function that generates a deck of 52 playing cards as an array of "1♠︎" or "V♣︎" type strings. Use a function that automatically shuffles the array of cards (the javascript does not have a shuffle function. Look for an equivalent or an implementation).
Reminder: the cards go from 1 (Ace) to 10 then Jack (J), Queen (Q) and King (K). Types are ♠︎♣︎♡♢.

# Level 2

For the following, a deck will be declared and stored in a `deck` constant.
Write a `deal` function that deals (and therefore removes from the deck) a number of cards, the number must be given as a parameter.
Create one variable per player. Each player should receive 2 cards.
Starting with 2 players, we will therefore have:

const player1 = deal(2)
    const player2 = deal(2)


# Level 3

Write a `flop` function that will return the flop, ie the 5 cards placed in the center of the deck, common to all players. The feature will use the `deal` feature and run the rounds like a real dealer, burning the cards between each.

The rounds are composed as follows:
First round = 1 card burnt, 3 cards out;
Second round = 1 card burnt, 1 card out;
Third round = 1 card burnt, 1 card out.

Drawn cards will be stored in a `cards` variable.

# Level 4

Write a `showdown` function that will display a player's hand. It will therefore take, in first parameter, the two cards of a player, and in second the flop (`cards` declared in level 3).
A player's hand can have the following elements: one or two pairs, a three of a kind, a quad, a flush, a straight or a straight.

For more details, see the [Wikipedia page](https://fr.wikipedia.org/wiki/Hand_au_poker#Ordre_des_levels_des_mains) on poker hands.

Example of use:

    const deck = createDeck() // ["1♡", "8♦︎" ...]
    const p1 = deal(2) // ["10♡", "K♧"]
    const p2 = deal(2) // ["8♦︎", "5♧"]
    let cards = flop() // ["J♡", "K♦︎", "7♠︎" ...]
    showdown(p1, flop)
    showdown(p2, flop)


Will display:

    hand: ["10♡", "K♧", "J♡", "K♦︎", "7♠︎" ... ]
    > set of 10
    hand: ["8♦︎", "5♧", "J♡", "K♦︎", "7♠︎" ... ]
    > set of 10