# reddit_butler
Personal project web scraper for reddit.com

### How to use
Scrapy must be installed via PIP before using.
```
pip install scrapy
```

From the root directory, run the following command:
```
scrapy crawl butler -s CLOSESPIDER_ITEMCOUNT=20 -o ./output/output.jsonl
```