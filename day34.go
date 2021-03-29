
// file math.go

package math

func Sum(a, b int) int {
    return a + b
}


// file math_test.go
// $ go test -v

package math

import "testing"

func TestSum(t *testing.T) {
    got := Sum(3, 3)
    want := 6
    if total != want {
       t.Errorf("return was incorrect
            got: %d, want: %d.", got, want)
    }
}

// Output
=== RUN   TestSum
--- PASS: TestSum (0.00s)
ok      ./sum 0.953s



