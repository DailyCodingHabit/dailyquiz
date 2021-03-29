package main

import (
	"fmt"
)

func dailycoding(num ...int) {
	num[0] = 1
}
func main() {
	i := []int{2, 3, 6}
	dailycoding(i...)
	fmt.Println(i[1] + i[0])
}

// 4 (3+1)
