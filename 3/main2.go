package main

import (
	"fmt"
	"os"
)

type pos struct {
	x, y int
}

func do(path string) map[pos]struct{} {
	p := pos{0, 0}
	s := map[pos]struct{}{p: struct{}{}}
	d := map[rune]pos{
		'>': pos{0, 1},
		'<': pos{0, -1},
		'^': pos{1, 0},
		'v': pos{-1, 0},
	}
	for _, c := range path {
		p.x += d[c].x
		p.y += d[c].y
		s[p] = struct{}{}
	}
	return s
}

func main() {
	var santaPath, roboPath []byte
	for i, c := range os.Args[1] {
		if i%2 == 0 {
			santaPath = append(santaPath, byte(c))
		} else {
			roboPath = append(roboPath, byte(c))
		}
	}
	santa := do(string(santaPath))
	robo := do(string(roboPath))
	for p, v := range robo {
		santa[p] = v
	}
	fmt.Println(len(santa))
}
