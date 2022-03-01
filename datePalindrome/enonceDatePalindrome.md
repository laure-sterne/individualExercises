`En français`

Pour cet exercice, le choix du langage est libre. Il va s'agir de manipuler des chaines de caractères représentant des dates.
### Niveau 1:
Créer une fonction `isValidDate` qui prend en paramètre une date en string et determine si elle est valide.
Pour qu'une date soit valide, il faut qu'elle existe et qu'elle soit au format dd/mm/aaaa.

### Niveau 2:
Créer une fonction `isPalindrome` qui prend une date en string en paramètre et retourne un booleen qui indique si la date est un palindrome. Si la date est invalide, retourner false. (Exemple de dates palindromes = qui se lit dans les deux sens)

### Niveau 3:
Créer une fonction `getNextPalindromes` qui donne les `x` prochaines dates palindromes à compter d’aujourd’hui. La fonction prend le `x` en paramètre.

#### Exemple d’usage :
Niveau 1

    isValidDate("03/04/2001") // true
    isValidDate("03/14/2001") // false

Niveau 2

    isPalindrome("11/02/2011") // true
    isPalindrome("03/04/2001") // false

Niveau 3

    getNextPalindromes(8)
    22/02/2022
    03/02/2030
    13/02/2031
    23/02/2032
    04/02/2040
    14/02/2041
    24/02/2042
    05/02/2050

`In english`

For this exercise, the choice of language is free. It will be a question of manipulating character strings representing dates.
### Level 1:
Create an `isValidDate` function that takes a string date as a parameter and determines if it is valid.
For a date to be valid, it must exist and be in the format dd/mm/yyyy.

### Level 2:
Create an `isPalindrome` function that takes a date string as a parameter and returns a boolean that indicates whether the date is a palindrome. If the date is invalid, return false. (Example of dates palindromes = which can be read both ways)

### Level 3:
Create a `getNextPalindromes` function that gives the next `x` palindrome dates from today. The function takes the `x` as a parameter.

#### Example of use:
Level 1

    isValidDate("03/04/2001") // true
    isValidDate("03/14/2001") // false

Level 2

    isPalindrome("11/02/2011") // true
    isPalindrome("03/04/2001") // false

Level 3

    getNextPalindromes(8)
    02/22/2022
    02/03/2030
    02/13/2031
    02/23/2032
    02/04/2040
    02/14/2041
    02/24/2042
    02/05/2050