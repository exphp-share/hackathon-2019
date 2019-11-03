document.forms["patient"].addEventListener('submit', function(e) {
	e.preventDefault();
	const mf = JSON.stringify({"email": document.querySelector('.field [name="email"]').value,
	"name": document.querySelector('.field [name="name"]').value});
	console.debug(mf);
})
