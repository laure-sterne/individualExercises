`En français`

# Motus

Le Motus est un jeu télévisé ou les candidats doivent deviner un mot. Leur est fourni un nombre de lettres et la première lettre du mot à deviner. Quand un candidat essaie un mot, on lui dit si les lettre données sont bonnes, mal placés, ou pas dans le mot.
Vous trouverez en annexe les sources HTML et JavaScript du jeu Motus. Ces sources présentent des bugs.

L’objectif de l’exercice est d’avoir un jeu fonctionnel.

## Step 1

Commencez par intégrer le code en annexe dans des fichiers HTML et JS. Faites le tour de ce qui fonctionne et de ce qui ne fonctionne pas.

## Step 2

Au boulot!
Fixez les bugs, et nettoyez un peu cette code base.

## Step 3

Le code source contient une note “TODO”. Le développeur à laissé une note pour developper une fonctionnalité pour plus tard.
Ajoutez la fonctionnalité manquante.

## Step 4

Écrivez des tests.


## Annexes :
### HTML
```
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Motus</title>
  </head>
  <body>
     <input id="word" />
     <button onclick="guess()">Ok</button>
     <p id="try"></p>
     <p id="well"></p>
     <p id="miss"></p>
     <p id="not"></p>
     <p id="win"></p>
  </body>
</html>
```


### JS
```
function tryWord(word, base) {
	// TODO: fix jeu sensible à la casse.
	if (word === base) {
		return true
  } else {
  	let wellPlaced = [];
    let notInWord = [];
    let missplaced = [];
    
  	let arrayBase = base.split('');
    let arrayWord = word.split('');
    
		for (let i = 0; i < arrayBase.length-1; i++) {
    	if (arrayBase[i] === arrayWord[i]) {
      	wellPlaced.push(arrayWord[i]);
      }	else {
        missplaced.push(arrayWord[i])
      }
    }
    
    for (const char of arrayWord) {
    	if (arrayBase.includes(char) === false) {
      	notInWord.push(char)
      }
    }
    
    return { wellPlaced: wellPlaced, missplaced: missplaced, notInWord: notInWord }
  }
}
function guess() {
	let base = 'dictionnaire'
	let word = document.getElementById("word").value
	let result = tryWord(word, base)
  document.getElementById("word").value = ''
 	document.getElementById("try").innerText = word
  document.getElementById("well").innerText = 'Bien placé: '+result.wellPlaced.join(', ')
  document.getElementById("miss").innerText = 'Mal placé: '+result.missplaced.join(', ')
  document.getElementById("not").innerText = 'Pas dans le mot: '+result.notInWord.join(', ')
  if (result.wellPlaced.length === base.length) {
	  document.getElementById("win").innerText = 'Vous avez gagné'
  }
```

`In english`

# Motus

The Motus is a game show where candidates have to guess a word. They are provided with a number of letters and the first letter of the word to guess. When a candidate tries a word, they are told if the given letters are good, misplaced, or not in the word.
You will find in appendix the HTML and JavaScript sources of the game Motus. These sources have bugs.

The objective of the exercise is to have a functional game.

##Step 1

Start by embedding the attached code in HTML and JS files. Explore what works and what doesn't.

##Step 2

At work!
Fix the bugs, and clean up this code base a bit.

##Step 3

The source code contains a “TODO” note. The developer left a note to develop a feature for later.
Add the missing functionality.

##Step 4

Write tests.


## Appendices:
### HTML
```
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Motus</title>
  </head>
  <body>
     <input id="word" />
     <button onclick="guess()">Ok</button>
     <p id="try"></p>
     <p id="well"></p>
     <p id="miss"></p>
     <p id="not"></p>
     <p id="win"></p>
  </body>
</html>
```


### JS
```
function tryWord(word, base) {
	// TODO: fix jeu sensible à la casse.
	if (word === base) {
		return true
  } else {
  	let wellPlaced = [];
    let notInWord = [];
    let missplaced = [];
    
  	let arrayBase = base.split('');
    let arrayWord = word.split('');
    
		for (let i = 0; i < arrayBase.length-1; i++) {
    	if (arrayBase[i] === arrayWord[i]) {
      	wellPlaced.push(arrayWord[i]);
      }	else {
        missplaced.push(arrayWord[i])
      }
    }
    
    for (const char of arrayWord) {
    	if (arrayBase.includes(char) === false) {
      	notInWord.push(char)
      }
    }
    
    return { wellPlaced: wellPlaced, missplaced: missplaced, notInWord: notInWord }
  }
}
function guess() {
	let base = 'dictionnaire'
	let word = document.getElementById("word").value
	let result = tryWord(word, base)
  document.getElementById("word").value = ''
 	document.getElementById("try").innerText = word
  document.getElementById("well").innerText = 'Bien placé: '+result.wellPlaced.join(', ')
  document.getElementById("miss").innerText = 'Mal placé: '+result.missplaced.join(', ')
  document.getElementById("not").innerText = 'Pas dans le mot: '+result.notInWord.join(', ')
  if (result.wellPlaced.length === base.length) {
	  document.getElementById("win").innerText = 'Vous avez gagné'
  }
```
