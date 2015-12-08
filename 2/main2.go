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
		if z < y {
			y, z = z, y
		}
		if z < x {
			x, z = z, x
		}
		t += 2*x + 2*y + x*y*z
	}
	fmt.Println(t)
}
