package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Edge struct {
	Person string
	Cost   int
}

var G = map[string]map[string]int{}
var S = map[string]bool{}
var L []string
var A = 0

func dfs(n string, i int) {
	if S[n] {
		return
	}
	L[i] = n
	S[n] = true
	defer func() { S[n] = false }()
	if i == len(G)-1 {
		f := func(x int) int {
			if x < 0 {
				return x + len(G)
			} else if x >= len(G) {
				return x - len(G)
			}
			return x
		}
		s := 0
		for i, n := range L {
			s += G[n][L[f(i-1)]] + G[n][L[f(i+1)]]
		}
		if s > A {
			A = s
		}
		return
	}
	for m := range G[n] {
		dfs(m, i+1)
	}
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		line := scanner.Text()
		parts := strings.Fields(line)
		x, d, es, y := parts[0], parts[2], parts[3], parts[10]
		e, _ := strconv.Atoi(es)
		y = y[:len(y)-1]
		if d == "lose" {
			e = 0 - e
		}
		l, ok := G[x]
		if !ok {
			l = map[string]int{}
			G[x] = l
		}
		l[y] = e
	}
	isPartTwo := true
	if isPartTwo {
		G[""] = map[string]int{}
		for n := range G {
			G[""][n] = 0
			G[n][""] = 0
		}
	}
	L = make([]string, len(G))
	for n := range G {
		dfs(n, 0)
	}
	fmt.Println(A)
}
