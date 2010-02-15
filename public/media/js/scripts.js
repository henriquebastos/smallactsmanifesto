$(document).ready(function() {
  $(".textfield").bind('mouseover focus',function() {
    $("#info_"+$(this).attr("id")).show();
  });
  
  $(".textfield").bind('mouseout blur',function() {
    $("#info_"+$(this).attr("id")).hide();
  });
});
