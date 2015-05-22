    // line chart data
    		var months = ["January","February","March","April","May","June", "July", "August", "October", "November", "December"];
            var buyerData = {
                labels : months,
                datasets : [
                {
                    fillColor : "rgba(172,194,2,0.4)",
                    strokeColor : "#ACC26D",
                    pointColor : "#fff",
                    pointStrokeColor : "#9DB86D",
                    data : [203,156,99,251,305,247, 343, 34, 343, 342, 234]
                }
            ]
            }
            // get line chart canvas
            var buyers = document.getElementById('buyers').getContext('2d');
            // draw line chart
            new Chart(buyers).Line(buyerData, {scaleFontSize: 16});