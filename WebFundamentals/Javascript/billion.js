function billion(){
  var count = .01;
  var ten = false;
  for(i = 1; i < 30; i++){
    count = count * 2;
    if (count > 10000 && ten === false){
      console.log(i+" Days to reach $10000");
      ten = true;
    }
  }
  return count;
}
billion();



