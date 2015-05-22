// pie chart data
            var pieData = [
                {
                    value: 20,
                    color:"#28C967"
                },
                {
                    value : 40,
                    color : "#1965A3"
                }
            ];
            // pie chart options
            var pieOptions = {
                 segmentShowStroke : false,
                 animateScale : true,
            }
            // get pie chart canvas
            var countries= document.getElementById("countries").getContext("2d");
            // draw pie chart
            new Chart(countries).Pie(pieData, pieOptions);