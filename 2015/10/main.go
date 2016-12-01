package main

import (
	"bytes"
	"fmt"
)

func lookandsay(s string) string {
	out := bytes.Buffer{}
	l := 'a'
	x := 0
	for _, c := range s {
		if l != 'a' && l != c {
			out.WriteString(fmt.Sprintf("%d%c", x, l))
			x = 0
		}
		l = c
		x += 1
	}
	out.WriteString(fmt.Sprintf("%d%c", x, l))
	return out.String()
}

func main() {
	s := "1321131112"
	for i := 0; i < 50; i += 1 {
		fmt.Println(i, len(s))
		s = lookandsay(s)
	}
	fmt.Println(len(s))
}
