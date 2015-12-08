package main

import (
	"crypto/md5"
	"fmt"
	"strconv"
	"strings"
)

func main() {
	prefix := "bgvyzdsv"
	for i := 1; ; i += 1 {
		s := prefix + strconv.Itoa(i)
		o := fmt.Sprintf("%x", md5.Sum([]byte(s)))
		if strings.HasPrefix(o, "000000") {
			fmt.Println(i)
			fmt.Println(s)
			fmt.Println(o)
			break
		}
	}
}
