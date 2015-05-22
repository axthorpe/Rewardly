// pie chart data


var items = {};
$.getJSON( "/accounts/get_all_data/", function( data ) {
  var items = data;

var this_months_budget =items['this_months_budget'];
var this_months_spending = items['this_months_spending'];
$('#this_month_percentage').text(Math.floor((this_months_spending/this_months_budget) * 100) + '%');
$('.fake1').text("$"+ Math.floor((this_months_spending *Math.random() *.2 +.05)) );
$('.fake2').text("$"+ Math.floor((this_months_spending *Math.random() *.2 +.05)) );
$('.fake3').text("$"+ Math.floor((this_months_spending *Math.random() *.2 +.05)) );
$('.fake4').text("$"+ Math.floor((this_months_spending *Math.random() *.2 +.05)) );

$('.last_month_total_expenditure').text("$"+ items['last_months_spending'] );

            var pieData = [
                {
                    value: this_months_spending,
                    color:"#28C967"
                },
                {
                    value : this_months_budget-this_months_spending,
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

});
