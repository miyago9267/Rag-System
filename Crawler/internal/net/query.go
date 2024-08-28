package net

import (
	"fmt"
	"log"
	"net/http"

	"github.com/PuerkitoBio/goquery"
)

func FetchDocs(url string) {

	resp, err := http.Get(url)
	if err != nil {
		log.Fatalf("HTTP request failed: %v", err)
	}
	defer resp.Body.Close()

	doc, err := goquery.NewDocumentFromReader(resp.Body)
	if err != nil {
		log.Fatalf("Failed to parse HTML: %v", err)
	}

	doc.Find(".row").Each(func(i int, s *goquery.Selection) {
		colNo := s.Find(".col-no").Text()
		line := s.Find(".line-0000").Text()

		if colNo != "" || line != "" {
			fmt.Printf("%s: %s\n\n", colNo, line)
		}
	})
}
