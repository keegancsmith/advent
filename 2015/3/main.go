package main

import (
	"fmt"
	"os"
)

type pos struct {
	x, y int
}

func main() {
	p := pos{0, 0}
	s := map[pos]struct{}{p: struct{}{}}
	d := map[rune]pos{
		'>': pos{0, 1},
		'<': pos{0, -1},
		'^': pos{1, 0},
		'v': pos{-1, 0},
	}
	for _, c := range os.Args[1] {
		p.x += d[c].x
		p.y += d[c].y
		s[p] = struct{}{}
	}
	fmt.Println(len(s))
}
