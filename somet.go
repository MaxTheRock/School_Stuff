package main

import (
    "fmt"
    "net/http"
)

func main() {
    url := "https://gitea.kdnsite.site"

    for i := 0; i < 999999999999; i++ {
        resp, err := http.Get(url)
        if err != nil {
            fmt.Println("Error:", err)
            continue
        }
        fmt.Println("Response Status:", resp.Status)
        resp.Body.Close()
    }
}