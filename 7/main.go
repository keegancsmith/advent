package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type wire func() uint16

var wires = map[string]wire{}
var memoize = map[string]uint16{}

func get(id string) uint16 {
	var v uint16
	var ok bool
	if v, ok = memoize[id]; ok {
		return v
	}
	i, err := strconv.Atoi(id)
	if err == nil {
		v = uint16(i)
	} else {
		v = wires[id]()
	}
	memoize[id] = v
	return v
}

func nullary(a string) wire {
	return func() uint16 { return get(a) }
}

func unary(a, b string) wire {
	switch a {
	case "NOT":
		return func() uint16 { return 65535 - get(b) }
	default:
		panic("Unexpected unary operator")
	}
}

func binary(a, b, c string) wire {
	switch b {
	case "AND":
		return func() uint16 { return get(a) & get(c) }
	case "OR":
		return func() uint16 { return get(a) | get(c) }
	case "LSHIFT":
		return func() uint16 { return get(a) << get(c) }
	case "RSHIFT":
		return func() uint16 { return get(a) >> get(c) }
	default:
		panic("Unexpected binary operator")
	}
}

func parse(line string) (wire, string) {
	parts := strings.Fields(line)
	switch len(parts) {
	case 3:
		return nullary(parts[0]), parts[2]
	case 4:
		return unary(parts[0], parts[1]), parts[3]
	case 5:
		return binary(parts[0], parts[1], parts[2]), parts[4]
	default:
		panic("Unexpected line")
	}
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		line := scanner.Text()
		f, id := parse(line)
		wires[id] = f
	}
	isPartTwo := true
	if isPartTwo {
		wires["b"] = nullary("16076")
	}
	fmt.Println(get("a"))
}
