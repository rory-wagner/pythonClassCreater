var pythonButton = document.querySelector("#pyButton");
var cxxButton = document.querySelector("#cppButton");

pythonButton.onclick = function (){
	path = "http://localhost:8080/python";
	sendJSON(path);
	var xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function() {
		if (this.readyState == 4 && this.status == 200) {
			var file = document.querySelector("#fileSearch");

		};
		xhttp.open("POST", file, true);
		xhttp.send();
	};
};

cxxButton.onclick = function (){
	path = "http://localhost:8080/c++";
	sendJSON(path);
};

function sendJSON(path){
	
	var textArea = document.querySelector("#inputBox");

	var bodyString = "jsonData=" + encodeURIComponent(textArea.value);
	var bodyString = file;
	console.log(bodyString);

	fetch(path, {
		method: "POST",
		body: bodyString,
		headers: {
			"Content-Type": "application/x-www-form-urlencoded"
		}

	}).then(function(response) {
		fetch(path, {
			
			// var xhttp = new XMLHttpRequest();
			// xhttp.onreadystatechange = function() {
			// 	if (this.readyState == 4 && this.status == 200) {
			// 		var file = document.querySelector("#fileSearch");

			// 	};
			// 	xhttp.open("POST", file, true);
			// 	xhttp.send();
			// };
			
		});

	});
};
