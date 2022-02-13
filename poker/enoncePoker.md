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
