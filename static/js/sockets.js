$(document).ready(function() {

    namespace = "/";
    var socket = io.connect(null, {port: 5000, rememberTransport: false});

    socket.on("connect", function() {
      socket.emit("hello", {data: 'connected to the SocketServer...'});
    });

    socket.on("response", function(msg) {
      $("#log").append("<br>" + $("<div/>").text("logs #" + msg.count + ":" + msg.message).html());
    });

    socket.on("georesp", function(location) {
        if (mymap.hasLayer(marker)) {
          console.log(mymap.hasLayer(marker))
          mymap.removeLayer(marker)
          console.log(location.latitude)
          console.log(location.longitude)
          marker = L.marker([parseInt(location.latitude), parseInt(location.longitude)]).addTo(mymap);
          mymap.setView(latlng.LatLng, mymap.getZoom(), {animation: true}).fitBounds(L.LatLng().fitBounds);
        }
        else {
          console.log("Here")
          console.log(mymap.hasLayer(marker))
          latlng.LatLng([location.latitude, location.longitude])
          marker = L.marker(latlng.latlng).addTo(mymap);
  
          mymap.setView(latlng.LatLng, mymap.getZoom(), {animation: true}).fitBounds(L.LatLng().fitBounds);
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
  });