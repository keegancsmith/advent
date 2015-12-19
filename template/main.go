package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strconv"
)

func SlurpNumbers() [][]int {
	r, _ := regexp.Compile(`-?[0-9]+`)
	nums := make([][]int, 0)
	scanner := bufio.NewScanner(os.Stdin)
	for i := 0; scanner.Scan(); i += 1 {
		line := scanner.Text()
		ss := r.FindAllString(line, -1)
		n := make([]int, len(ss))
		for j, s := range ss {
			n[j], _ = strconv.Atoi(s)
		}
		nums = append(nums, n)
	}
	return nums
}

func main() {
	nums := SlurpNumbers()
	for _, n := range nums {
		fmt.Println(n)
	}
}
