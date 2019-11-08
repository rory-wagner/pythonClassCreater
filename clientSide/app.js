var browsebutton = document.querySelector("#fileFinder");
browsebutton.onclick = function (){


	fetch("http://localhost:8080/python", {
		method: "POST",
		headers: {
			"Content-Type": "application/x-www-form-urlencoded"
		}

	}).then(function(response) {


	});
}
