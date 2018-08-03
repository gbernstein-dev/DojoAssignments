heap=[undefined, 3, 8, 10, 11, 9, 20, 14]
function insertIntoHeap(arr, item){
  arr.push(item)
  var parent_index = Math.trunc((arr.length)/2);
  var push_value = arr[arr.length - 1];
  if (push_value < arr[parent_index]){
    temp = push_value;
    push_value = arr[parent_index];
    arr[parent_index] = temp;
    console.log(arr);
  }
}

insertIntoHeap(heap,7)


// the value of the item at the last index needs to be greater than
// the value at 1/2 the index, otherwise switch values 