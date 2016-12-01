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
		vowels := 0
		twice := false
		illegal := false
		for i, c := range line {
			// vowel check
			if c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' {
				vowels += 1
			}
			if i == 0 {
				continue
			}
			if byte(c) == line[i-1] {
				twice = true
			}
			d := line[i-1 : i+1]
			if d == "ab" || d == "cd" || d == "pq" || d == "xy" {
				illegal = true
			}
		}
		if vowels >= 3 && twice && !illegal {
			nice += 1
		}
	}
	if err := scanner.Err(); err != nil {
		panic(err)
	}
	fmt.Println(nice)
}
