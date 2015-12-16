package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func trim(s string) string {
	return strings.TrimRight(s, ",:")
}

func toInt(s string) int {
	x, _ := strconv.Atoi(s)
	return x
}

func main() {
	sue := map[string]int{
		"children":    3,
		"cats":        7,
		"samoyeds":    2,
		"pomeranians": 3,
		"akitas":      0,
		"vizslas":     0,
		"goldfish":    5,
		"trees":       3,
		"cars":        2,
		"perfumes":    1,
	}
	scanner := bufio.NewScanner(os.Stdin)
	isPartTwo := true
	for scanner.Scan() {
		line := scanner.Text()
		parts := strings.Fields(line)
		for i := range parts {
			parts[i] = trim(parts[i])
		}
		found := true
		for i := 2; i < len(parts) && found; i += 2 {
			x := parts[i]
			y := toInt(parts[i+1])
			switch x {
			case "cats", "trees":
				found = sue[x] < y
			case "pomeranians", "goldfish":
				found = sue[x] > y
			default:
				found = sue[x] == y
			}
			if !isPartTwo {
				found = sue[x] == y
			}
		}
		if found {
			fmt.Println(parts[1])
		}
	}
}
