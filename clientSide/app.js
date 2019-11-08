var browsebutton = document.Selector("#filefind")
browsebutton.onclick = function()
{
	$.getJSON(


	fetch("http://localhost:8080/files").then(function (response) 
	{
		response.json().then(function(data){

			method:"POST",
			body: bodyStr,
			headers:{

					"Content-Type":"application/x-www-form-urlencoded"
			}

		});.then(function(response){
				console.log("Server Responed")

	});
}

