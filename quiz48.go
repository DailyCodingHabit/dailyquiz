package main

import (
	"fmt"
	"sort"
)

func main() {
	// DailyCodingHabit Quiz
	s := []int{10, -1, 25, 3, -30, 5}
	sort.Sort(sort.IntSlice(s))
	fmt.Println(sort.IntSlice(s).Search(6))
}
