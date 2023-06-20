import sys, getopt
import subprocess

__app_name__="reddit_butler"
__version__="0.1.0"

def main():
    #system call to spider
    #build list of subs to gather
    sublist = []
    for i in sys.argv:
        if i != "app.py":
            sublist.append("https://old.reddit.com/r/" + i)
    if len(sublist) > 0:
        subs = ','.join(sublist) #stringified list of URLs sepereated by comma
    else:
        subs = "https://old.reddit.com/" #no inputted subreddits, crawl front page instead
    subprocess.run(["scrapy", "crawl", "butler", "-s", "CLOSESPIDER_ITEMCOUNT=50", "-a", "start_urls=" + subs, "-O", "./output/output.jsonl"])

if __name__ == "__main__":
    main()