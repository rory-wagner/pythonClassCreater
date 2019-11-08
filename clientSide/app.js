var browsebutton = document.Selector("#filefind")
browsebutton.onclick = function(){
	var inputFile = browsebutton.value.getJSON()


	fetch("http://localhost:8080/files", {
			method: "POST",
			body: bodyStr,
			headers:{
				"Content-Type":"application/x-www-form-urlencoded"
			}

		}).then(function(response){
				console.log("Server Responed")

			});
	}
};

