var mymap = L.map('map').setView([51.505, -0.09], 17);
L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
maxZoom: 18,
id: 'mapbox/streets-v11',
tileSize: 512,
zoomOffset: 0,
accessToken: 'pk.eyJ1IjoiamVzc2VzbWUiLCJhIjoiY2tqd3BvNHNuMGtqYzJ2bDdyd3hxbGc2YSJ9.QrC4h8kQU6GuhQG14sk6oA'
}).addTo(mymap);

var marker;

function centerMapOnMarker(map, marker) {
    var latLngs = marker.getLatLng();
    var markerBounds = [[latLngs.lat + 1, latLngs.lng + 1],[latLngs.lat - 1, latLngs.lng - 1]];
    map.fitBounds(markerBounds)
  }