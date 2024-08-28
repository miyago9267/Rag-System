package main

import (
	"docscrawler/internal/net"
)

func main() {
	// url := "https://law.moj.gov.tw/LawClass/LawAll.aspx?media=print&pcode=C0000001"
	url := "https://law.moj.gov.tw/LawClass/LawAll.aspx?media=print&pcode=N0060001"
	net.FetchDocs(url)
}
