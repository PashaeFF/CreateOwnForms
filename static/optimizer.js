function RemoveAtribute(id) {
    const checkboxes = document.querySelectorAll(`input[type='checkbox'][id='${id}']`);
    checkboxes.forEach(checkbox => {
        checkbox.addEventListener("click", () => {
        if (checkbox.checked) {
            checkboxes.forEach(cb => {
            if (cb !== checkbox) {
                cb.removeAttribute("required");
            }
            });
        } else {
            checkboxes.forEach(cb => {
            if (cb !== checkbox) {
                cb.setAttribute("required", "");
            }
            });
        }
        });
    });
}

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
    $("#submit").append('<button type="submit" class="btn btn-primary" id="submit_button" style="background-color:#01cb30;">Submit</button>');
    }
    
    const progressPercent = Math.floor((currentPage / totalPages) * 100);
    document.querySelector('.progress-bar').style.width = `${progressPercent}%`;
    document.querySelector('.progress-bar').innerHTML = `${progressPercent}%`;
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
    document.querySelector('.progress-bar').innerHTML = `${progressPercent}%`;
    window.scrollTo(0, 0);
}