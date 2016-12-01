package main

import (
	"fmt"
	"io"
)

func main() {
	var x, y, z int
	t := 0
	for {
		_, err := fmt.Scanf("%dx%dx%d", &x, &y, &z)
		if err != nil {
			if err == io.EOF {
				break
			} else {
				panic(err)
			}
		}
		a := x * y
		b := y * z
		c := x * z
		m := a
		if b < m {
			m = b
		}
		if c < m {
			m = c
		}
		t += 2*(a+b+c) + m
	}
	fmt.Println(t)
}
