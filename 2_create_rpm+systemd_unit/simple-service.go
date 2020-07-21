package main
import (
    "fmt"
    "time"
)
func main() {
    var n int = 0
    var i int = 3
    for {
        n += 1
        fmt.Println("simple service line", n)
        time.Sleep(time.Duration(i) * time.Second)
    }
}
