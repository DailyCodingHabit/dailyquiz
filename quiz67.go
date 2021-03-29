package main

import (
	"fmt"
	"strings"
)

func main() {
	value1, value2 := "DAILY", "coding"
	index1, index2 := strings.Index("Habit", "b"), strings.Index("Quiz", "z")
	if strings.EqualFold(string(value1[index1]), string(value2[index2])) {
		fmt.Println(true)
	} else {
		fmt.Println(false)
	}
}
