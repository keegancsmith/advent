package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strings"
)

var R = map[string]string{}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		line := scanner.Text()
		parts := strings.Fields(line)
		if len(parts) == 0 {
			break
		}
		a, b := parts[0], parts[2]
		_, ok := R[b]
		if ok {
			panic(b)
		} else {
			R[b] = a
		}
	}
	scanner.Scan()
	input := scanner.Text()
	i := 0
	froms := make([]string, len(R))
	for s := range R {
		froms[i] = s
		i += 1
	}
	sort.Sort(StringSlice(froms))
	steps := 0
	for {
		for _, s := range froms {
			for {
				c := strings.Count(input, s)
				if c <= 0 {
					break
				}
				steps += c
				input = strings.Replace(input, s, R[s], -1)
			}
		}
		fmt.Println("Step", steps, input)
		if input == "e" {
			break
		}
	}
	fmt.Println(steps)
}

type StringSlice []string

func (p StringSlice) Len() int           { return len(p) }
func (p StringSlice) Less(i, j int) bool { return len(p[i]) > len(p[j]) }
func (p StringSlice) Swap(i, j int)      { p[i], p[j] = p[j], p[i] }
