const list = document.querySelector('.my_list');
const addItemBtn = document.querySelector('#add_item');

addItemBtn.addEventListener('click', function () {
    const newItem = document.createElement('li');
    newItem.textContent = 'Item';

    list.appendChild(newItem);
});
