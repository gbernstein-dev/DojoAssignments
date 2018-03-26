function fancy(arr,symbol,reverse=false){
  if(reverse === true){
    for(var i = arr.length - 1; i >= 0; i--){
      console.log(i+symbol+arr[i]);
    }
  }
  else{
    for(var x = 0; x < arr.length; x++){
      console.log(x+symbol+arr[x]);
    }
  }
}
fancy(["Hello","World","Again"],"->",true);

