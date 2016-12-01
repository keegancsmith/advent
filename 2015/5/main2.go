package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	nice := 0
	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		line := scanner.Text()
		repeat := false
		pair := false
		seen := map[string]bool{}
		for i, c := range line {
			if i <= 1 {
				continue
			}
			if rune(line[i-2]) == c {
				repeat = true
			}
			if seen[line[i-1:i+1]] {
				pair = true
			}
			seen[line[i-2:i]] = true
		}
		if repeat && pair {
			nice += 1
		}
	}
	if err := scanner.Err(); err != nil {
		panic(err)
	}
	fmt.Println(nice)
}
