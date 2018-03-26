function printRange(x, y = 0, z = 1){
  for (i = x; i < y; i=i+z){
    console.log(i);
  }
}
printRange(10);