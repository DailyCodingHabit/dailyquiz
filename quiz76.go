package main

import "fmt"
import "strings"

func dailyCoding(a []string) {
	for i := range a {
		a[i] = "%%"
	}
	b := strings.Join(a, "")
	fmt.Printf(b + "%%")
}
func main() {
	dailyCoding([]string{"1", "Coding"})
}
