package main

import "fmt"

func dailyCodingHabit() {
	fmt.Println("2")
}
func main() {
	go dailyCodingHabit()
	fmt.Println("1")
}
