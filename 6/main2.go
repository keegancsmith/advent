package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	var grid [1000][1000]int
	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		line := scanner.Text()
		parts := strings.Split(line, " ")
		var (
			f              func(int) int
			offset         int
			x1, y1, x2, y2 int
		)
		if parts[0] == "turn" {
			offset = 2
			if parts[1] == "on" {
				f = func(x int) int { return x + 1 }
			} else {
				f = func(x int) int {
					y := x - 1
					if y < 0 {
						y = 0
					}
					return y
				}
			}
		} else {
			offset = 1
			f = func(x int) int { return x + 2 }
		}
		fmt.Sscanf(parts[offset], "%d,%d", &x1, &y1)
		fmt.Sscanf(parts[offset+2], "%d,%d", &x2, &y2)
		for x := x1; x <= x2; x++ {
			for y := y1; y <= y2; y++ {
				grid[x][y] = f(grid[x][y])
			}
		}
	}
	on := 0
	for x := 0; x < 1000; x++ {
		for y := 0; y < 1000; y++ {
			on += grid[x][y]
		}
	}
	fmt.Println(on)
}
