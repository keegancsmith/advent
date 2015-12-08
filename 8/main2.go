package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	size := 0
	total := 0
	for scanner.Scan() {
		line := scanner.Text()
		total += len(line)
		size += 2
		for _, c := range line {
			switch c {
			case '\\', '"':
				size += 2
			default:
				size += 1
			}
		}
	}
	fmt.Println(size - total)
}
