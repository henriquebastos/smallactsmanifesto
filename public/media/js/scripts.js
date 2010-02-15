$(document).ready(function() {
  $(".textfield").mouseover(function() {
    $("#info_"+$(this).attr("id")).show();
  });
  
  $(".textfield").bind('mouseout blur',function() {
    $("#info_"+$(this).attr("id")).hide();
  });
});
