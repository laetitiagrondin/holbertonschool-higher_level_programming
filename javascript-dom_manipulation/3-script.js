const header = document.querySelector('header');
const toggleBtn = document.querySelector('#toggle_header');

toggleBtn.addEventListener('click', function () {
    if (header.classList.contains('red')) {
        header.classList.remove('red');
        header.classList.add('green');
    }
    else {
        header.classList.remove('green');
        header.classList.add ('red');
    }
});
