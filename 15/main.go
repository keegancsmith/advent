package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type ingredient struct {
	c      [5]int
	amount int
}

var ingredients []*ingredient
var maxScore int

func score() int {
	s := ingredient{}
	for _, x := range ingredients {
		for i := 0; i < 5; i++ {
			s.c[i] += x.c[i] * x.amount
		}
	}
	isPartTwo := true
	if isPartTwo && s.c[4] != 500 {
		return 0
	}
	val := 1
	for i := 0; i < 4; i++ {
		if s.c[i] < 0 {
			return 0
		}
		val *= s.c[i]
	}
	return val
}

func set(idx, amount int) {
	if idx == 0 {
		ingredients[idx].amount = amount
		s := score()
		if s > maxScore {
			maxScore = s
		}
		return
	}
	for a := 0; a <= amount; a++ {
		ingredients[idx].amount = a
		set(idx-1, amount-a)
	}
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		line := scanner.Text()
		parts := strings.Fields(line)
		toInt := func(i int) int {
			x, _ := strconv.Atoi(strings.TrimRight(parts[i], ","))
			return x
		}

		ingredients = append(ingredients, &ingredient{
			c: [5]int{toInt(2), toInt(4), toInt(6), toInt(8), toInt(10)},
		})
	}

	set(len(ingredients)-1, 100)
	fmt.Println(maxScore)
}
