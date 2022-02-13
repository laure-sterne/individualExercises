// Step 1

// piste : qqch à faire avec le format -> création date en séparant jour, mois et année

function formattedDate(d = new Date) {
    let month = String(d.getMonth() + 1);
    let day = String(d.getDate());
    const year = String(d.getFullYear());
  
    if (month.length < 2) month = '0' + month;
    if (day.length < 2) day = '0' + day;
  
    return `${day}/${month}/${year}`;
}

function isValidDate(){

}

document.getElementById("date").innerText = formattedDate(d = new Date);
 /*
function isValidDate(date) {
    let date = prompt("Donnez-mua une date siouplai :3");

    date.setDate() + "/" + date.setMonth() + "/" + date.setFullYear();
    console.log(date);

    
}

alert("Votre date n'est pas valide ! Veuillez la saisir au format dd/mm/yyyy.")

isValidDate(date);


/*

// Step 2
function isPalindrome() {

};


// Step 3
function getNextPalindromes() {

};

*/