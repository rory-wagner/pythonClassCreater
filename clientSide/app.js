var pythonButton = document.querySelector("#pyButton");
var cxxButton = document.querySelector("#cppButton");
var file = 0;
var fileLink;
var textArea = document.querySelector("#inputBox");
var fileNameInput = document.querySelector("#fileNameInput");
var classNameInput = document.querySelector("#classNameInput");

pythonButton.onclick = function (){
	path = "http://localhost:8080/python";
	if(fileNameInput.value != "" && fileNameInput.value.slice(-3) != ".py" ){
		alert("Only a proper Python filename is accepted.");
		return
	}
	sendJSON(path);
};

cxxButton.onclick = function (){
	path = "http://localhost:8080/c++";
	if(fileNameInput.value != "" && fileNameInput.value.slice(-4) != ".cpp" ){
		alert("Only a proper C++ filename is accepted.");
		return
	}
	sendJSON(path);
};

function sendJSON(path){

	console.log(typeof textArea.value);
	var possibleObject;
	try{
		possibleObject = JSON.parse(textArea.value);
	}
	catch{
		alert("Only proper JSON formatting is accepted.");
		return
	}
	// if (typeof JSON.parse(textArea.value) != 'object' ){
	// 	alert("Only proper JSON formatting is accepted.");
	// 	return
	// }
	var bodyString = "jsonData=" + encodeURIComponent(textArea.value);


	if(fileNameInput.value != ""){
		bodyString += "&fileName=" + encodeURIComponent(fileNameInput.value);
	}
	else{
		bodyString += "&fileName=" + encodeURIComponent("null");
	}
	if(classNameInput.value != ""){
		bodyString += "&className=" + encodeURIComponent(classNameInput.value);
	}
	else{
		//Might need to change "null" here...
		bodyString += "&className=" + encodeURIComponent("null");
	}

	//Here we are trying to change the bodyString
	//Need to get that working by tomorrow or else just scrap it.
	if( file !== 0 ){
		bodyString = file;
	}
	console.log(bodyString);

	fetch(path, {
		method: "POST",
		body: bodyString,
		headers: {
			"Content-Type": "application/x-www-form-urlencoded"
		}

	}).then(function (postResponse) {
		console.log(postResponse);
		console.log(fileNameInput.value);
		fetch(path + "/" + fileNameInput.value, {
			method: "GET",
			headers: {
			}
		}).then(function main(getResponse){

			getResponse.text().then(function (fileLink) {

				console.log("Server responded from GET!");
				console.log(fileLink);
				fileLink = fileLink.slice(6);
				
				//make sure fileLink is a link to a file.
				var downloadLink = document.querySelector("#downloadLink");
				var displayLink = document.querySelector("#displayLink");
				displayLink.style.display = "block";
				downloadLink.setAttribute("href", fileLink);
				downloadLink.innerHTML = "download";
				console.log("Finished");
			})
		});
	}
)};
	// var xhttp = new XMLHttpRequest();
	// xhttp.onreadystatechange = function() {
	// 	if (this.readyState == 4 && this.status == 200) {
	// 		file = document.querySelector("#fileSearch");

	// 	};
	// 	xhttp.open("POST", file, true);
	// 	xhttp.send();
	// };
