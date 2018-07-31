function minMaxAvg(arr){
  var min = arr[0];
  var max = arr[0];
  var sum = 0;
  for (var i=0; i<arr.length; i++){
    if (arr[i]>max){
      max = arr[i];
    }
    else if (arr[i]<min) {
      min = arr[i];
    }
    sum += arr[i];
  }
  var avg = sum/arr.length;
  
  return "min is " + min + " and max is " + max + " and the avg is " + avg ;
}

console.log(minMaxAvg([3, 2, 5]));