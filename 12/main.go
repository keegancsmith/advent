package main

import (
	"encoding/json"
	"fmt"
	"os"
)

func f(vv interface{}) int {
	switch v := vv.(type) {
	case int:
		return v
	case float64:
		return int(v)
	case map[string]interface{}:
		s := 0
		for _, x := range v {
			if y, ok := x.(string); ok && y == "red" {
				return 0
			}
			s += f(x)
		}
		return s
	case []interface{}:
		s := 0
		for _, x := range v {
			s += f(x)
		}
		return s
	default:
		return 0
	}
}

func main() {
	var v interface{}
	json.NewDecoder(os.Stdin).Decode(&v)
	fmt.Println(f(v))
}
