$(document).ready(function() {

    namespace = "/";
    var socket = io("ws://jesse.plus")
	var scooter_data = ""


    socket.on("connect", function() {
      socket.emit("hello", {data: 'connected to the SocketServer...'});
	});

	socket.on("dataresponse", function(msg) {
		var data = JSON.parse(msg.message)
		$("#data_location").text("Location: " + data["location"][0] + ", " + data["location"][1]).html()
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
	})

	socket.on("power_response", function(msg) {
		if (msg.state && (msg.state != "")) {
			$("#power_button").val(msg.state)
		}
		$("#log").prepend("<br>" + $("<div/>").text("logs #" + msg.count + ": " + msg.message).html());
	})

    socket.on("response", function(msg) {
      	$("#log").prepend("<br>" + $("<div/>").text("logs #" + msg.count + ": " + msg.message).html());
    });

    socket.on("georesp", function(location) {
        if (mymap.hasLayer(marker)) {
          mymap.removeLayer(marker)
          marker = L.marker([parseInt(location.latitude), parseInt(location.longitude)]);
          marker.addTo(mymap)
          centerMapOnMarker(mymap, marker);
        }
        else {
          marker = L.marker([parseInt(location.latitude), parseInt(location.longitude)]);
          marker.addTo(mymap)
          centerMapOnMarker(mymap, marker);
        }
    })

    $('form#emit').submit(function(event) {
    socket.emit('scooter_info', {data: $('#emit_data').val()});
    return false;
	});

    $('form#power').submit(function(event) {
      socket.emit('power_signal', {pass: $('#password_power').val(), state: $('#power_button').val()});
      return false;
    });

    $('button#geoloc').mouseup(function(event) {
        socket.emit('geoloc', {"data": "Updating marker"})
        return false;
	});
    $('button#test').mouseup(function(event) {
        socket.emit('geoloc', {"data": "Updating marker"})
        return false;
    });

    setInterval(() => {
		socket.emit('scooter_info', {data: $('#emit_data').val()});
		return false;
    }, 5000)
  });