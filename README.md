# Books Scraper

This project crawls the entire selection of books on books.toscrape.com.

## Requirements

* Python 3
* Scrapy

## Usage

1. Clone repo
2. CD into the project. You should be in the same folder as scrapy.cfg.
3. Run the spider with `scrapy crawl books`
4. Different export options include:
  * `scrapy crawl books -o books.json`
  * `scrapy crawl books -o books.jl`
  * `scrapy crawl books -o books.csv`

