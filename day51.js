


function linearSearch(arr, item) {
  for (var i = 0; i < arr.length; i++) {
    if (arr[i] === item) { 
      return i;
    }
  }
  return null;
}

var dailyCoding = [ 1, 22, 16, 0, 7, 9];

console.log(linearSearch(dailyCoding,7))
// output: 4



