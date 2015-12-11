package main

import "fmt"

func valid(buf []byte) bool {
	l := 1
	pair := 0
	run := false
	foundpair := false
	for i := 0; i < len(buf); i++ {
		switch buf[i] {
		case 'i', 'o', 'l':
			return false
		}
		if i == 0 {
			continue
		}
		if buf[i-1]+1 == buf[i] {
			l += 1
		} else {
			l = 1
		}
		if l == 3 {
			run = true
		}
		if buf[i-1] == buf[i] && !foundpair {
			pair += 1
			foundpair = true
		} else {
			foundpair = false
		}
	}
	return run && pair >= 2
}

func next(buf []byte, i int) bool {
	if i < 0 {
		return false
	}
	if buf[i] == 'z' {
		buf[i] = 'a'
		return next(buf, i-1)
	}
	buf[i] = buf[i] + 1
	return true
}

func main() {
	buf := []byte("hepxcrrq")
	b := false
	//buf := []byte("abcdefgh")
	for {
		next(buf, len(buf)-1)
		fmt.Println("checking", string(buf))
		if valid(buf) {
			if b {
				fmt.Println(string(buf))
				break
			}
			b = true
		}
	}
}
