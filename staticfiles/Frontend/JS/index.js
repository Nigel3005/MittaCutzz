// Define how many menu's and button's you have by changing these numbers:
var buttonCount = 3;

// All variables and definings
var btn = [];

// One time loop to get all button's from the HTML sheet
for (let i=1; i<=buttonCount; i++) {
    btn[i] = document.getElementById('btn-' + i);
}

// Function to call in an "onclick" function in your HTML sheet:
// Define the menu to open like this "chooseMenu(<menu number>)" in your HTML sheet
function chooseMenu(a) {
    for (let b=1; b<=buttonCount; b++) {
        if(a === b) {
            btn[b].classList.add('active');
        } else if (a !== b) {
            btn[b].classList.remove('active');
        }
    }
}

// Set menu-1 as default, choose other menu number to set to default here
chooseMenu(1);