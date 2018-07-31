var tigger = {character: "Tigger"};
var pooh = {character: "Pooh"};
var piglett = {character: "Piglett"};
var owl = {character: "Owl"};
var bees = {character: "Bees"};
var chris = {character: "Christopher Robin"};
var rabbit = {character: "Rabbit"};
var kanga = {character: "Kanga"};
var gopher = {character: "Gopher"};
var eeyore = {character: "Eeyore"};
var heffalumps = {character: "Heffalumps"};

tigger.north = pooh;
pooh.north = chris;
pooh.east = bees;
pooh.south = tigger;
pooh.west = piglett;
piglett.east = pooh;
piglett.north = owl;
owl.east = chris;
owl.south = piglett;
chris.south = pooh;
chris.west = owl;
chris.east = rabbit;
chris.north = kanga;
bees.north = rabbit;
bees.west = pooh;
rabbit.west = chris;
rabbit.east = gopher;
kanga.south = chris;
kanga.north = eeyore;
eeyore.south = kanga;
eeyore.east = heffalumps;
heffalumps.west = eeyore;

function move(direction) {
  if (direction !== undefined) {

    if (direction == "north"){
      player.location = player.location.north;
      console.log(`Player moved ${direction} and is now at ${player.location.character}`);
    }
    else if (direction == "east"){
      player.location = player.location.east;
      console.log(`Player moved ${direction} and is now at ${player.location.character}`);
    }
    else if (direction == "west"){
      player.location = player.location.west;
      console.log(`Player moved ${direction} and is now at ${player.location.character}`);
    }
    else if (direction == "south"){
      player.location = player.location.south;
      console.log(`Player moved ${direction} and is now at ${player.location.character}`); 
    }
    
    else{
      console.log("please enter valid input")
    }
  }
}
move("north");
move("east");
move("tacos");

