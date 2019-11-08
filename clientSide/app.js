var browsebutton = document.querySelector("#fileFinder");
browsebutton.onclick = function(){

	$.getJSON( browsebutton, function( data ) {
		var items = [];
		$.each( data, function( key, val ) {
		  items.push( "<li id='" + key + "'>" + val + "</li>" );
		});
	   
		$( "<ul/>", {
		  "class": "my-new-list",
		  html: items.join( "" )
		}).appendTo( "body" );
	  });

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

