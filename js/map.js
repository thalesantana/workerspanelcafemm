var data = '[{"lat": -13.103920724367565,"long": -52.10791325712833, "people_number": 4}, {"lat": -12.971688847390759,"long": -38.501132213857524, "people_number": 7}, {"lat": -22.901103216851517,"long": -43.17305053572673, "people_number": 5}, {"lat": -19.903952721886068,"long": -43.935221372850194, "people_number": 15}]'
var data_lat_long = JSON.parse(data);

function inicializar() {
  var map = L.map('map').setView([data_lat_long[0].lat, data_lat_long[0].long], 4);
    mapLink = '<a href="https://openstreetmap.org">OpenStreetMap</a>';
    L.tileLayer(
        'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: 'Map data &copy; ' + mapLink,
        maxZoom: 16,
        title: '2 Desenvolvedores'
        }).addTo(map);
        for (var i = 1; i < data_lat_long.length; i++){
          var marker = L.marker([data_lat_long[i].lat, data_lat_long[i].long]).addTo(map);
          marker.bindTooltip(data_lat_long[i].people_number + " Desenvolvedores", { permanent: false, offset: [0, 12] });
        }
}

inicializar();