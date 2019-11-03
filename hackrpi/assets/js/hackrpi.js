document.forms["patient"].addEventListener('submit', function(e) {
	e.preventDefault();

	
	function splitCommas(s) {
        return s.split(',').map((token) => token.trim());
    }

	function getFieldText(name) {
		return document.querySelector('.field [name="' + name + '"]').value;
	}
	const mf = {
		"email": getFieldText('email'),
		"name": getFieldText('name'),
		"pin": getFieldText('pin'),
		//"allergy": document.querySelector('.field [name="allergy"]'),
		"allergy" : splitCommas(getFieldText('allergy')),
		"currentmed" : splitCommas(getFieldText('currentmed')),
	};

	var xhr = new XMLHttpRequest();
	xhr.open("POST", "/write-data");
	xhr.setRequestHeader('Content-Type', 'application/json');
	//console.debug(mf);
	xhr.send(JSON.stringify(mf));

	
})
