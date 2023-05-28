let map;

function initMap() {
  const mapOptions = {
    zoom: 15,
    center: { lat: -33.437796, lng: -70.650445 }
  };
  map = new google.maps.Map(document.getElementById("mapa"), mapOptions);
  const marker = new google.maps.Marker({
    position: { lat: -33.437796, lng: -70.650445 },
    map,
    title: "Lugar del evento"
  });
}
