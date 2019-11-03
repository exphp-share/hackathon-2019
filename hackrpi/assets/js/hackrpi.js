document.forms["patient"].addEventListener('submit', function(e) {
    e.preventDefault();
    const mf = JSON.stringify({
        "email": document.querySelector('.field [name="email"]').value,
        "name": document.querySelector('.field [name="name"]').value,
        "pin": document.querySelector('.field [name="pin"]').value,
        "phone": document.querySelector('.field [name="phone"]').value,
    });

    var xhr = new XMLHttpRequest();
    xhr.open("POST", "http://localhost:5000/write-data");
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify(mf));
})