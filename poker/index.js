// Level 1 – modify and understand this program to shuffle the deck of cards


// empty array to contain cards
const deck = [];

function createDeck(){ 

    const suits = ["♠︎ Spades", "♢ Diamonds", "♣︎ Club", "♡ Heart"];
    const values = [ "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10",
"Jack", "Queen", "King"];

    // create a deck of cards
    for (let i = 0; i < suits.length; i++) {
        for (let x = 0; x < values.length; x++) {
            let card = values[x] + " " + suits[i];
            deck.push(card);
        }
    }

    // shuffle the cards by creating an other deck
    for (let i = deck.length - 1; i > 0; i--) {
        let j = Math.floor(Math.random() * i);
        let temp = deck[i];
        deck[i] = deck[j];
        deck[j] = temp;
    }

    console.log("The length of shuffled deck", deck.length)
    return deck;
};

createDeck();


// Level 2 – distribution and remove cards which are in hand's players
function deal(numberOfCards){

    let hand = [];

    for (let i = 0; i < numberOfCards; i++) {
        let randomCard = Math.floor(Math.random() * deck.length);
        let myCard = deck.splice(randomCard, 1)
        hand.push(myCard[0]);
    }

    console.log("The new length of new deck", deck.length)
    return hand;
};

const player1 = console.log("The cards of player1 are: ", deal(2));
const player2 = console.log("The cards of player2 are: ", deal(2));


// Level 3 – draw lots poker card
function flop(){

    console.log("First round!")
    deal(1);
    let centerCards = deal(3);
    console.log("The card in center after first", centerCards)

    console.log("Second round!")
    deal(1);
    centerCards.push(deal(1)[0]);
    console.log("The card in center after second", centerCards)


    console.log("Third and last round!")
    deal(1);
    centerCards.push(deal(1)[0]);
    console.log("The card in center after third", centerCards)

}

let cards = flop()


// Level 4 – show the cards player and the center cards
function showdown(){

}
