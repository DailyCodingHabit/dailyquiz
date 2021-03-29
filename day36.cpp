

// C++ Code Example
#include <iostream>
using namespace std;

int dailycoding (int x)
{
  int output;
  output = x * 2;
  return output;
}

int main ()
{
  cout << dailycoding(3);
}

// Golang Example
package main

import "fmt"

func dailycoding(x int) int {
	output := x * 2
	return output
}

func main() {
	fmt.Println(dailycoding(3))
}


// JavaScript Example
function dailycoding(x) {
	output = x * 2;
	return output;
}
dailycoding(3);
// Output 6


// PHP Example
function dailycoding($input) {
	$output = $input * 2; 
	return $output; 
}
echo dailycoding(3);
// Output 6
	