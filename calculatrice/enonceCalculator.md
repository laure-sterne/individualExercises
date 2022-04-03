`En français`

## Calculator

### STEP 1

Designez une page HTML qui prendra la forme d'une calculatrice. 
- Afficher les chiffres de `0` à `9`
- Afficher un bouton `+`

```javascript
<button id="0">0</button>
```

### STEP 2

Afficher le cadrant de la calculatrice, qui affichera le chiffre sélectionné par l'utilisateur.

Hints:

```javascript
<button id="1" onclick="button1clicked()">1</button>
var cadrant = document.getElementById("cadrant");
cadrant.text += "1"
```

### STEP 3

Afficher aussi l'opérateur `+` dans le cadrant lorsqu'il est sélectionné, afin de pouvoir construire une opération.

### STEP 4

Intégrer l'opérateur `=` qui déclanchera le calcule de votre opération et affichera le résultat dans le cadrant.

### STEP 5

Intégrer l'opérateur `-`

### STEP 6

Intégrer les opérateurs `/` et `*`

> Attention, ces opérateurs ont un ordre d'exécution !

Si l'on a un calcul du type `3+3*3` l'opérateur `*` à la priorité !

### STEP 7

On ajoute des parenthèses ?

`In english`

## Calculator

### STEP 1

Design an HTML page that will take the form of a calculator.
- Display digits from `0` to `9`
- Show a `+` button

```javascript
<button id="0">0</button>
```

### STEP 2

Display the calculator face, which will display the digit selected by the user.

Hints:

```javascript
<button id="1" onclick="button1clicked()">1</button>
var frame = document.getElementById("frame");
frame.text += "1"
```

### STEP 3

Also display the `+` operator in the frame when it is selected, in order to be able to construct an operation.

### STEP 4

Integrate the `=` operator which will trigger the calculation of your operation and display the result in the quadrant.

### STEP 5

Include the `-` operator

### STEP 6

Include the `/` and `*` operators

> Attention, these operators have an execution order!

If we have a calculation of the `3+3*3` type, the `*` operator has priority!

### STEP 7

Add parentheses?