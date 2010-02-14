$(document).ready(function() {
  $(".textfield").mouseover(function() {
    $("#info_"+$(this).attr("id")).show();
  });
  
  $(".textfield").bind('click mouseout',function() {
    $("#info_"+$(this).attr("id")).hide();
  });
});
