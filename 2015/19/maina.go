package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

var R = map[string][]string{}
var S = map[string]bool{}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		line := scanner.Text()
		parts := strings.Fields(line)
		if len(parts) == 0 {
			break
		}
		a, b := parts[0], parts[2]
		li, ok := R[a]
		if !ok {
			li = []string{b}
		} else {
			li = append(li, b)
		}
		R[a] = li
	}
	scanner.Scan()
	input := scanner.Text()
	for s, li := range R {
		i := 0
		for {
			j := strings.Index(input[i:], s)
			if j < 0 {
				break
			}
			for _, repl := range li {
				S[input[:i+j]+repl+input[i+j+len(s):]] = true
			}
			i += j + 1
		}
	}
	fmt.Println(len(S))
}
