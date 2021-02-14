$(document).ready(function() {

	var location = {}

    setInterval(function() {
		if (location // 👈 null and undefined check
			&& Object.keys(location).length === 0 && location.constructor === Object) {
				return false;
			}
		console.log(location)
        if (mymap.hasLayer(marker)) {
          mymap.removeLayer(marker)
          marker = L.marker(location);
          marker.addTo(mymap)
          centerMapOnMarker(mymap, marker);
        }
        else {
          marker = L.marker(location);
          marker.addTo(mymap)
          centerMapOnMarker(mymap, marker);
		}
		return false;
	},
	5000)

	$('button#centerMap').mouseup

    $('form#power').submit(function(event) {
		message = {pass: $('#password_power').val(), state: $('#power_button').val()}
	  $.ajax({
		type: "POST", // HTTP method POST or GET
		contentType: 'application/json; charset=utf-8', //content type
		url: "http://localhost:5000/ipa/power_state", //Where to make Ajax calls
		dataType:'json', // Data type, HTML, json etc.
		processData: false,
		data: JSON.stringify(message),
	}).done(
		function(data) {
			if (data.state && (data.state != "")) {
				$("#power_button").val(data.state)
			}
			$("#log").prepend("<br>" + $("<div/>").text(data.message).html());
		  }
	);
      return false;
    });

    setInterval(() => {
		$.ajax({
			type: "GET", // HTTP method POST or GET
			contentType: 'application/json; charset=utf-8', //content type
			url: "http://localhost:5000/ipa/controller", //Where to make Ajax calls
			success: function(data) {
				var data = data
				location = data["location"]
				$("#data_table").html("");
				for ([key, value] of Object.entries(data)) {
					var counter = 0
					if (Array.isArray(value)) {
						var length = value.length
						$("#data_table").append(
							`<tr id="data_${key}"}><th ${length <= 1 ? "" : `rowspan=${length}`}>${key}</th></tr>`
						)
						value.forEach(element => {
							if (counter == 0) {
								$(`#data_${key}`).append(
									`<td>${element}</td>`
								)
								counter = 1
							} else {
								$("#data_table").append(`<tr><td>${element}</td></tr>`)
							}
						})
					} else if (typeof(value) == "object") {
						if (value["$date"]){
							var d = new Date(value["$date"])
							$("#data_table").append(
								`<tr><th>${key}</th><td>${d}</td></tr>`
							)
						} else {
							var length = Object.keys(value).length
							$("#data_table").append(
								`<tr id="data_${key}"><th ${length <= 1 ? "" : `rowspan=${length}`}>${key}</th></tr>`
							)
							for (const [deepkey, deepvalue] of Object.entries(value)) {
								if (counter == 0) {
									$(`#data_${key}`).append(
										`<td>${deepkey}: ${deepvalue}</td>`
									)
									counter = 1
								} else {
									$("#data_table").append(
										`<tr><td>${deepkey}: ${deepvalue}</td></tr>`
									)
								}
							}
						}
					} else {
						$("#data_table").append(
							`<tr id="data_${key}" }><th>${key}</th><td>${value}</td></tr>`
						)
					}
				}
			}
		})
		return false;
	}, 5000)
	
	
  });