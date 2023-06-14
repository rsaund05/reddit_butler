# reddit_butler
Personal project web scraper for reddit.com

### How to use
Scrapy must be installed via PIP before using.
```
pip install scrapy
```

From the root directory, run the following command. Giving no subreddits will run the spider on the homepage:
```
python app.py
```
app.py can take a specific list of subs (case sensitive) to scrape like so:
```
python app.py pics AskReddit Food
```