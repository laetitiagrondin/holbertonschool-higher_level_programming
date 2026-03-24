const header = document.querySelector('header');
const redcolor = document.querySelector('#red_header');

redcolor.addEventListener('click', function () {
    header.classList.add('red');
});
