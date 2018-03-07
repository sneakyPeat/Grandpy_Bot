$(document).ready(function() {
    $("form").on("submit", function(event) {

        $.ajax({
            url: "/ajax",
            type: "POST",
            dataType: "json",
            data: {query: $("#query").val()},
            success:function(response){
                displayAjax(response);
            }
        });
        event.preventDefault();
    });
});

function displayAjax(response) {
    var r_answer = random_answer();
    var query = response.json.query;
    var address = response.json.address;
    var latitude = response.json.lat;
    var longitude = response.json.lng;
    var title = response.json.title;
    var closest_thing_str = "La chose la plus proche que je connaisse est : ";
    var content = response.json.content;
    var url_content = response.json.wiki_link;
    var error = "Désolé, mais je n'ai rien trouvé ... &#9785";

    if (query === "Empty") {
        $(".answer h4").html(error);
        $("p.grandpy_answer").html("");
        document.getElementById("map").style.display = "none";
        $(".wiki").html("");
        $(".wiki_link").attr("href", url_content).html("");
    } else {
        // show the map
        document.getElementById("map").style.display = "block";

        // display the adress
        $(".grandpy_answer").html(r_answer + address);

        // init the map
        initMap(latitude, longitude);

        if (content != "nothing found") {
            // wikipedia info
            $(".answer h4").html(closest_thing_str + title);
            $(".wiki").html(content);
            $(".wiki_link").attr("href", url_content).html("En savoir plus sur wikipedia ...");
        } else {
            $("h4").html("").addClass('text-center');
            $(".wiki").html("Je ne connais rien à propos de cet endroit ...").addClass('text-center');
            $(".wiki_link").attr("href", "").html("");
        }
    }
}

function random_answer() {
    var answer = ["Bien sûr mon poussin ! La voici : ",
                  "Ah je me rappel très bien de cet endroit ",
                  "A cet endroit, je me souviens : ",
                  "Il y a bien longtemps que je ne suis pas allé ici : "
              ];

    var random_number = Math.floor(Math.random() * answer.length);

    return answer[random_number];
}

function initMap(latitude, longitude) {
    var coord = new google.maps.LatLng(latitude, longitude);
    var map = new google.maps.Map(document.getElementById("map"), {
      zoom: 10,
      center: coord
    });
    var marker = new google.maps.Marker({
      position: coord,
      map: map
    });
    return map;
}
