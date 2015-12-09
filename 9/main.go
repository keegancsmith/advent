package main

import (
	"bufio"
	"fmt"
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
	ans     = -1
)

func candidate() {
	if ans == -1 {
		ans = curDist
		return
	}
	isPartTwo := true
	if isPartTwo {
		if curDist > ans {
			ans = curDist
		}
	} else {
		if curDist < ans {
			ans = curDist
		}
	}
}

func dfs(n string) {
	if seen[n] {
		return
	}
	seen[n] = true
	defer func() { delete(seen, n) }()

	if len(seen) == len(G) {
		candidate()
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
	fmt.Println(ans)
}
