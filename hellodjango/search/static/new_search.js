

// Checks if the search box is empty, if so it throws up an error. However, it only looks at the main search, need to bind 
// to the search in the top-right also. If no error then a series of messages appear on the screen usings animation. They are 
// set so that it distracts the user from the loading time. If the user has already had an error and searches after 
// the error message is removed

$('form').on('submit', function(e){
  var btn = $('#button');
    if($('#search-box').val()===''){
      e.preventDefault();
      btn.after('<div class="error text-center"> You have not entered a name. Please retry</div>');
    }else{ 
        btn.after("<div id='box' class='searched text-center'> Give us a sec, we're pulling the data together... </div>");
          $('#box').hide().fadeIn(500)
            setTimeout(function (){
              $('#box').fadeOut(500)
            }, 5000)
            btn.after("<div id='box2' class='searched text-center'>Videos, news and tweets coming up... </div>");
         $('#box2').delay(5500).hide().fadeIn(500)
            setTimeout(function (){
              $('#box2').fadeOut(500)
            }, 10000)
          btn.after("<div id='box3' class='searched text-center'>Almost there... </div>");
         $('#box3').delay(10500).hide().fadeIn(500)
            setTimeout(function (){
              $('#box3').fadeOut(500)
            },17000)
            btn.html('Loading...')
            // setTimeout(function () {
            //     btn.button('reset')
            // }, 25000)
            if ($('.error').length){
              $('.error').remove()
            }
        }

 
});