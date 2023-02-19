// ###### CHECK AND OPTIMIZE REQUIRED INPUTS
function toggleRequired(element) {
    var text = document.getElementById(element);
    console.log("element input >", element)
    var id = text.getAttribute('class');
    console.log("id >", id)
    var elements = document.querySelectorAll('#' + id);
    console.log("elements >", elements)
  for (var i = 0; i < elements.length; i++) {
    console.log('elements i >' ,elements[i])
    if (elements[i].value.trim() === '') {
        console.log('Null', elements[i].value)
        elements[i].setAttribute('required', true);
    } else {
        console.log('Full')
        elements[i].removeAttribute('required');
    }
  }
}

 function RemoveAtribute(element) {
    console.log("element>",element)
    var checkbox = document.getElementById(element);
    if (checkbox.checked == true)
        {
        console.log("checked")
        var id = checkbox.getAttribute('class');
        console.log("id >",id)
        var elements = document.querySelectorAll('#' + id + '[required]');
        console.log("elements >",elements)
        for (var i = 0; i < elements.length; i++) {
            elements[i].removeAttribute('required');
            console.log("changed >", elements[i])
        }
    }
    else {
        console.log("Unchecked")
        var id = checkbox.getAttribute('class');
        console.log("id >",id)
        var elements = document.querySelectorAll('#' + id);
        console.log("elements >",elements)
        for (var i = 0; i < elements.length; i++) {
            elements[i].setAttribute('required', true);
            console.log("changed >", elements[i])
    }
    
    } 
}
// ###### END CHECK AND OPTIMIZE REQUIRED INPUTS

// ######## PAGINATE AND PROGRESS BAR OPTIMIZER
function paginateCards(page) {
const cards = document.querySelectorAll('.card_1');
const cardsPerPage = 5;
const startIndex = (page - 1) * cardsPerPage;
const endIndex = startIndex + cardsPerPage;

for (let i = 0; i < cards.length; i++) {
if (i >= startIndex && i < endIndex) {
cards[i].style.display = 'block';
} else {
cards[i].style.display = 'none';
}
}

const totalCards = cards.length;
const totalPages = Math.ceil(totalCards / cardsPerPage);
const progressPercent = Math.floor((page / totalPages) * 100);
document.querySelector('.progress-bar').style.width = `${progressPercent}%`;
}

let currentPage = 1;
paginateCards(currentPage);

document.getElementById('prev-btn').addEventListener('click', function() {
if (currentPage > 1) {
currentPage--;
paginateCards(currentPage);
if (currentPage === 1) {
document.getElementById('prev-btn').setAttribute('disabled', '');
document.getElementById('next-btn').setAttribute('style', 'background-color:#01cb30;');
}
}
document.getElementById('next-btn').removeAttribute('disabled');
document.getElementById('next-btn').setAttribute('style', 'background-color:#01cb30;');
$("#submit_button").remove();
});

document.getElementById('next-btn').addEventListener('click', function() {
const cards = document.querySelectorAll('.card_1');
const cardsPerPage = 5;
const totalCards = cards.length;
const totalPages = Math.ceil(totalCards / cardsPerPage);

if (currentPage === totalPages) {
document.getElementById('prev-btn').remove();
document.getElementById('next-btn').remove();
$("#submit").append('<button type="submit" class="btn btn-primary" id="submit_button" style="background-color:#01cb30;">Submit</button>');
}

if (currentPage < totalPages) {
currentPage++;
paginateCards(currentPage);
if (currentPage === totalPages) {
document.getElementById('next-btn').setAttribute('disabled', '');
document.getElementById('next-btn').setAttribute('style', 'background-color:#c4c4c4;');
$("#submit").append('<button type="submit" class="btn btn-primary" id="submit_button" style="background-color:#01cb30;">Submit</button>');
}
}
document.getElementById('prev-btn').removeAttribute('disabled');
});

document.addEventListener('DOMContentLoaded', function() {
const cards = document.querySelectorAll('.card_1');
const cardsPerPage = 5;
const totalCards = cards.length;
const totalPages = Math.ceil(totalCards / cardsPerPage);

if (totalPages > 0 && currentPage === totalPages) {
document.getElementById('prev-btn').remove();
document.getElementById('next-btn').remove();
document.getElementById('page_count').remove()
$("#submit").append('<button type="submit" class="btn btn-primary" id="submit_button" style="background-color:#01cb30;">Submit</button>');
}
const progressPercent = Math.floor((currentPage / totalPages) * 100);
document.querySelector('.progress-bar').style.width = `${progressPercent}%`;
});
function paginateCards(page) {
const cards = document.querySelectorAll('.card_1');
const cardsPerPage = 5;
const startIndex = (page - 1) * cardsPerPage;
const endIndex = startIndex + cardsPerPage;

for (let i = 0; i < cards.length; i++) {
if (i >= startIndex && i < endIndex) {
cards[i].style.display = 'block';
} else {
cards[i].style.display = 'none';
}
}

const totalCards = cards.length;
const totalPages = Math.ceil(totalCards / cardsPerPage);
const progressPercent = Math.floor((page / totalPages) * 100);
document.querySelector('.progress-bar').style.width = `${progressPercent}%`;
document.getElementById('page_count').innerHTML = `Step ${currentPage}/${totalPages}`;
window.scrollTo(0, 0);
}