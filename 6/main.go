package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	var grid [1000][1000]bool
	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		line := scanner.Text()
		parts := strings.Split(line, " ")
		var (
			f              func(bool) bool
			offset         int
			x1, y1, x2, y2 int
		)
		if parts[0] == "turn" {
			offset = 2
			if parts[1] == "on" {
				f = func(_ bool) bool { return true }
			} else {
				f = func(_ bool) bool { return false }
			}
		} else {
			offset = 1
			f = func(x bool) bool { return !x }
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
			if grid[x][y] {
				on += 1
			}
		}
	}
	fmt.Println(on)
}
