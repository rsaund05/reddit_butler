# reddit_butler
- Basic command line scraper for old.reddit.com.<br />
- Just a basic html scraper, doesn't touch the dreaded Reddit API ;)<br />
- Data is outputted in json, so its easy to integrate with other applications.<br />
- NOTE: In order to function, reddit_butler has to ignore robots.txt, so YMMV if you decide to use or implement this, as your IP can be banned if you make too many requests.<br />

### How to use
Scrapy must be installed via PIP before using.
```
pip install scrapy
```

From the root directory, run the following command, or envoke your installed Python runtime with app.py.
Giving no subreddits will run the spider on the homepage:
```
python app.py
```
app.py can take a specific list of subs (NOT case sensitive) to scrape like so:
```
python app.py pics askreddit food
```

Data is written to 
```
./output/output.jsonl
```
