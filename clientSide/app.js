var pythonButton = document.querySelector("#pyButton");
var cxxButton = document.querySelector("#cppButton");

pythonButton.onclick = function (){
	path = "http://localhost:8080/python";
	sendJSON(path);
};

cxxButton.onclick = function (){
	path = "http://localhost:8080/c++";
	sendJSON(path);
};

function sendJSON(path){
	
	var textArea = document.querySelector("#inputBox");

	var bodyString = "jsonData=" + encodeURIComponent(textArea.value);
	console.log(bodyString)

	fetch(path, {
		method: "POST",
		body: bodyString,
		headers: {
			"Content-Type": "application/x-www-form-urlencoded"
		}

	}).then(function(response) {
		fetch("http://localhost:8080/files", {
			
		})

	});
}
