function coinChange(coins){
  var total = {dollars: 0, dimes: 0, pennies: 0};

  while (coins >= 100){
    coins -= 100;
    total.dollars += 1;
  }
  while (coins >= 10){
    coins -= 10;
    total.dimes += 1;
  }
  while (coins >= 1){
    coins -= 1;
    total.pennies += 1;
  }
  return total;
}

console.log(coinChange(298))