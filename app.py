import sys, getopt
import subprocess

__app_name__="reddit_butler"
__version__="0.1.0"

def main():
    #system call to spider
    if len(sys.argv) == 1: #check if only 1 argument, meaning hit reddit front page
        subprocess.run(["scrapy", "crawl", "butler", "-s", "CLOSESPIDER_ITEMCOUNT=20","-a", "start_urls=https://old.reddit.com", "-O", "./output/output.jsonl"])
    else:
        #build list of subs to gather
        sublist = []
        for i in sys.argv:
            if i != "app.py":
                sublist.append("https://old.reddit.com/r/" + i)
        subs = ','.join(sublist) #list of URLs built on inputted subreddits, TODO: Make more secure
        subprocess.run(["scrapy", "crawl", "butler", "-s", "CLOSESPIDER_ITEMCOUNT=20", "-a", "start_urls=" + subs, "-O", "./output/output.jsonl"])

if __name__ == "__main__":
    main()