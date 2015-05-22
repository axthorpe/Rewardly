  
          $.getJSON( "/accounts/get_all_data/", function( data ) {

            var this_months_spending = data['rewards'];
            var new_rewards_points = this_months_spending*(1+Math.random()*.2);
            var change = new_rewards_points-this_months_spending;


            $('.fake1').text( Math.floor(new_rewards_points) );
            $('.fake2').text( Math.floor(change) );
          });
