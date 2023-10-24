
//MAPA lugar->(-33.399614, -70.50725//,->zoom)//
var map = L.map('map').setView([-33.399614, -70.50725], 13);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

L.marker([-33.399614, -70.50725]).addTo(map)
    .bindPopup('Automotora Vandall')
    .openPopup();
//FIN MAPA//

