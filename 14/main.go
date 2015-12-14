package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type state struct {
	speed, length, rest, x, y, d, points int
}

func main() {
	raceTime := 2503
	scanner := bufio.NewScanner(os.Stdin)
	states := make([]*state, 0)
	for scanner.Scan() {
		line := scanner.Text()
		parts := strings.Fields(line)
		_, speeds, lengths, rests := parts[0], parts[3], parts[6], parts[13]
		speed, _ := strconv.Atoi(speeds)
		length, _ := strconv.Atoi(lengths)
		rest, _ := strconv.Atoi(rests)
		states = append(states, &state{speed, length, rest, 0, 0, 0, 0})
	}
	maxDist := 0
	for t := 0; t < raceTime; t++ {
		maxDist = 0
		for _, s := range states {
			if s.x < s.length {
				s.d += s.speed
				s.x += 1
			} else if s.y < s.rest-1 {
				s.y += 1
			} else {
				s.x, s.y = 0, 0
			}
			if s.d > maxDist {
				maxDist = s.d
			}
		}
		for _, s := range states {
			if s.d == maxDist {
				s.points += 1
			}
		}
	}
	maxPoints := 0
	for _, s := range states {
		if s.points > maxPoints {
			maxPoints = s.points
		}

	}
	fmt.Println("Part 1:", maxDist)
	fmt.Println("Part 2:", maxPoints)
}
