$(document).ready(function() {
  var menuToggle = $('#js-mobile-menu').unbind();
  $('#js-navigation-menu').removeClass("show");

  menuToggle.on('click', function(e) {
    e.preventDefault();
    $('#js-navigation-menu').slideToggle(function(){
      if($('#js-navigation-menu').is(':hidden')) {
        $('#js-navigation-menu').removeAttr('style');
      }
    });
  });
});

/*
$(document).ready(function() {
  $("tr").click(function() {
    $link = $(this).attr('href');
    alert("The paragraph was clicked.");
    window.open($link);
  });
});
*/

$(document).off('click', 'a.a-click');
    $(document).on('click', 'a.a-click', function(event){
      event.stopPropagation();
    });

    $(document).off('click', 'tr.tr-click');
    $(document).on('click', 'tr.tr-click', function(event){
        $link = $(this).attr('href');
        window.open($link);
        event.stopPropagation();
    });
