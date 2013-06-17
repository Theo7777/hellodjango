// On page load bring back the first two videos. If the user wants more clips then pressing the button
// will bring up the next 8 results
$(document).ready(function(event){
			//searches on for the first 2 clips from YouTube API so that the page loads faster
            $.get('https://gdata.youtube.com/feeds/api/videos?q={{details.firstName}}+{{details.lastName}}&orderby=relevance&max-results=2&v=2&alt=jsonc',
            function(response) {
                if(response.data && response.data.items) {
                    var items = response.data.items;
                    //check if video returned. If so add the value returned to the url. Then add it 
                    //to an iframe
                   	if(items.length>0) {
                        var item1 = items[0];
                        var item2 = items[1];
                        var videoid_1= "http://www.youtube.com/embed/"+item1.id;
                        var videoid_2 = "http://www.youtube.com/embed/"+item2.id;
                        console.log("Latest ID: '"+videoid_1+"'");
                        console.log("Latest ID: '"+videoid_2+"'");
                        var video1 = "<iframe width='420' height='315' src='"+videoid_1+"' frameborder='0' allowfullscreen></iframe>";
                        var video2 = "<iframe width='420' height='315' src='"+videoid_2+"' frameborder='0' allowfullscreen></iframe>";
                        $('#ajax_video1').html(video1);
                        $('#ajax_video2').html(video2);
                    }
                }
            })
			

			
				$('#button').on('click', function(event){
					//searches for the first 10 most relevant clips from youtube
					$.get('https://gdata.youtube.com/feeds/api/videos?q={{details.firstName}}+{{details.lastName}}&orderby=relevance&max-results=10&v=2&alt=jsonc',
			            function(response) {
			                if(response.data && response.data.items) {
			                    var new_items = response.data.items;
			                    // a for loop to iterate through all the videos returned.
			                    //Add this to the url and then save it as an iframe
			                    if(new_items.length>0) {
			                    	for (var i=2; i<=10; i++){
			                    		// console.log('here');
			                    		var new_item = new_items[i];  
			                    		console.log('after item');                  		
			                    		var videoid = "http://www.youtube.com/embed/" +new_item.id;
			                        	console.log("Latest ID: '"+videoid+"'");
			                        	var final_vid = "<iframe width='420' height='315' src='"+videoid+"' frameborder='0' allowfullscreen></iframe>";
			                        	//check if the number is even, if so place add left class to add to the left
			                        	if (i % 2 == 0) {
			                        		$('#ajax_video2')
			                        			.after('<div class="span4" id="left">'+ final_vid + '</div>');
			                        	}else{
			                        		$('#ajax_video2')
			                        			.after('<div class="span4" id="right">'+ final_vid + '</div>');

			                        	}//end for loop
			                        
			                    	}//end for loop
			                	}//end if
			            	}  //end response if
						})//end function response - closed bracket for get request
				//lengthen the height of the background so if fills all the videos
				$('.videos').css('height', '2000px');
					})
					
			});//end click function
		