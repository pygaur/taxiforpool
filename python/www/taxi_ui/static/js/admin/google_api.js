    function initialize() {
        var markers = [];
        var options = {
            types: ['geocode'],
            componentRestrictions: {
                country: 'in'
            }
        };
        var autocompleteOrigin = new google.maps.places.Autocomplete(document.getElementById('id_pickup_point'), options);
        var autocompleteDestination = new google.maps.places.Autocomplete(document.getElementById('id_destination_point'), options);
        var autocompleteLandmark = new google.maps.places.Autocomplete(document.getElementById('id_landmark'), options);
        google.maps.event.addListener(autocompleteOrigin, 'place_changed', setFromLocation);
        google.maps.event.addListener(autocompleteDestination, 'place_changed', setToLocation);
        google.maps.event.addListener(autocompleteLandmark, 'place_changed', setLandmark);
    }

    function setFromLocation() {
        $originLocation = this.getPlace().geometry.location.toString();
        $originLocation = ($originLocation != undefined) ? $originLocation.replace("(", "").replace(")", "").replace(",", " ") : "0 0";
    }

    function setLandmark() {
        $originLandmark = this.getPlace().geometry.location.toString();
        $originLandmark = ($originLandmark != undefined) ? $originLandmark.replace("(", "").replace(")", "").replace(",", " ") : "0 0";
    }


    function setToLocation() {
        $destinationLocation = this.getPlace().geometry.location.toString();
        $destinationLocation = ($destinationLocation != undefined) ? $destinationLocation.replace("(", "").replace(")", "").replace(",", " ") : "0 0";
    }
    google.maps.event.addDomListener(window, 'load', initialize);
