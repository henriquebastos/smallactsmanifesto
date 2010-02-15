$(document).ready(function() {
  $(".field").bind('mouseover focus',function() {
    $(".info_label", this).show();
  });

  $(".field").bind('mouseout',function() {
    $(".info_label", this).hide();
  });

  $(".field > input").bind('focus',function() {
    $(".info_label", $(this).parent()).show();
  });

  $(".field > input").bind('blur',function() {
    $(".info_label", $(this).parent()).hide();
  });

});
