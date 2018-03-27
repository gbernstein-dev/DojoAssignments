$(document).ready(function(){
  $("#click").click(function(){
    $(".functionality").css("font-weight", "bold");
  });
  $("#hide").click(function(){
    $("#hidden").hide("slow");
  });
  $("#show").click(function(){
    $("#hidden").show("slow");
  });
  $("#toggle").click(function(){
    $(".functionality").toggle();
  });
  $("#slideDown").click(function(){
    $("#hidden").hide("slow");
    $("#hidden").slideDown("slow");
  });
});