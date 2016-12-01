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
		for i := 1; i < len(line)-1; i += 1 {
			size += 1
			x, y := line[i], line[i+1]
			if x != '\\' {
				continue
			}
			switch y {
			case '\\', '"':
				i += 1
			case 'x':
				i += 3
			}
		}
	}
	fmt.Println(total - size)
}
