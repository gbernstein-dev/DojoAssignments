$(document).ready(function(){
  $.get("https://pokeapi.co/api/v2/pokemon/1", function(data){
    console.log(data);
  }, "json");
});