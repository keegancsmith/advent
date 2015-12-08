package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	in := os.Args[1]
	fmt.Println(strings.Count(in, "(") - strings.Count(in, ")"))
}
