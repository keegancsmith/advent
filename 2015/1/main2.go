package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	all := os.Args[1]
	for i := range all {
		in := all[:i+1]
		x := strings.Count(in, "(") - strings.Count(in, ")")
		if x == -1 {
			fmt.Println(i + 1)
			break
		}
	}
}
