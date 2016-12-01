package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

var containers []int
var totals = map[int]int{}

func f(idx, used, n int) {
	if used == 150 {
		totals[n] = totals[n] + 1
	} else if used > 150 {
		return
	} else if idx >= len(containers) {
		return
	} else {
		f(idx+1, used+containers[idx], n+1)
		f(idx+1, used, n)
	}
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		line := scanner.Text()
		x, _ := strconv.Atoi(line)
		containers = append(containers, x)
	}
	f(0, 0, 0)
	minK, V, T := len(containers), 0, 0
	for k, v := range totals {
		if k < minK {
			minK = k
			V = v
		}
		T += v
	}
	fmt.Println("Part1", T)
	fmt.Println("Part2", minK, V)
}
