$.getJSON( "/accounts/get_all_data/", function( data ) {
    var items=data;
console.log(items);
      // line chart data
    var months = ["July","August","September","October","November","December", "January", "Feburary", "March", "April", "May","June"];
            var data_set = items['scores'];
    console.log(data_set);
            var buyerData = {
                labels : months,
                datasets : [
                {
                    fillColor : "rgba(172,194,2,0.4)",
                    strokeColor : "#ACC26D",
                    pointColor : "#fff",
                    pointStrokeColor : "#9DB86D",
                    data : data_set
                }
            ]
            }
            // get line chart canvas
            var buyers = document.getElementById('buyers').getContext('2d');
            // draw line chart
            new Chart(buyers).Line(buyerData, {scaleFontSize: 16});

});

