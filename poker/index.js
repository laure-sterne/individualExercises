/* Level 1 : modify and understand this program to shuffle the deck of cards

declare card elements */
const suits = ["♠︎ Spades", "♢ Diamonds", "♣︎ Club", "♡ Heart"];
const values = [ "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10",
"Jack", "Queen", "King"];

// empty array to contain cards
let deck = [];

function createDeck(couleurs, valeurs){ 
    // create a deck of cards
    for (let i = 0; i < couleurs.length; i++) {
        for (let x = 0; x < valeurs.length; x++) {
            let card = valeurs[x] + " " + couleurs[i];
            deck.push(card);
        }
    }

    // shuffle the cards
    for (let i = deck.length - 1; i > 0; i--) {
        let j = Math.floor(Math.random() * i);
        let temp = deck[i];
        deck[i] = deck[j];
        deck[j] = temp;
    }
   return deck;
};

// console.log(createDeck(suits, values));


// Level 2 : distribution and remove cards which are in hand's players

let hand = [];

function deal(numberOfCards){
    console.log('Your two cards are:');

    // display 2 results
    for (let i = 0; i < numberOfCards; i++) {   
        result = Math.floor(Math.random * deck[i])
        hand.push(result);
    }
    return hand;
};

console.log(deal(3));

