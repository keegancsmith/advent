package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

type Edge struct {
	n string
	w int
}

var (
	G       = map[string][]Edge{}
	seen    = map[string]bool{}
	curDist = 0
	minDist = math.MaxInt32
)

func dfs(n string) {
	if seen[n] {
		return
	}
	seen[n] = true
	defer func() { delete(seen, n) }()

	if len(seen) == len(G) {
		if curDist < minDist {
			minDist = curDist
		}
		return
	}

	for _, e := range G[n] {
		curDist += e.w
		dfs(e.n)
		curDist -= e.w
	}
}

func add(a, b string, w int) {
	e := Edge{b, w}
	l, ok := G[a]
	if !ok {
		l = []Edge{e}
	} else {
		l = append(l, e)
	}
	G[a] = l
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		line := scanner.Text()
		parts := strings.Fields(line)
		a, b, ws := parts[0], parts[2], parts[4]
		w, _ := strconv.Atoi(ws)
		add(a, b, w)
		add(b, a, w)
	}
	for n := range G {
		dfs(n)
	}
	fmt.Println(minDist)
}
