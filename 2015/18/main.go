package main

import (
	"bufio"
	"fmt"
	"os"
)

func next(a [][]bool, b [][]bool) {
	delta := [][]int{
		{-1, 0},
		{0, -1},
		{1, 0},
		{0, 1},
		{1, -1},
		{-1, 1},
		{-1, -1},
		{1, 1},
	}
	isPartTwo := true
	for x := range a {
		for y := range a[x] {
			if isPartTwo && (x == 0 || x == len(a)-1) && (y == 0 || y == len(a[x])-1) {
				a[x][y], b[x][y] = true, true
				continue
			}
			c := 0
			for _, d := range delta {
				x1, y1 := x+d[0], y+d[1]
				if x1 >= 0 && x1 < len(a) && y1 >= 0 && y1 < len(a[x]) && a[x1][y1] {
					c += 1
				}
			}
			b[x][y] = (a[x][y] && (c == 2 || c == 3)) || (!a[x][y] && c == 3)
		}
	}
}

func main() {
	i := 0
	a, b := make([][]bool, 100), make([][]bool, 100)
	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		a[i], b[i] = make([]bool, 100), make([]bool, 100)
		line := scanner.Text()
		for j, c := range line {
			a[i][j] = c == '#'
		}
		i += 1
	}
	for i = 0; i < 100; i += 1 {
		if i%2 == 0 {
			next(a, b)
		} else {
			next(b, a)
		}
	}
	ans := 0
	for x := range a {
		for y := range a[x] {
			if a[x][y] {
				ans += 1
			}
		}
	}
	fmt.Println(ans)
}
