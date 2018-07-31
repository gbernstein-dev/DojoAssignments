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

console.log(heffalumps.west.south.south.south)
