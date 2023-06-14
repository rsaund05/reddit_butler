import sys, getopt
import subprocess

__app_name__="reddit_butler"
__version__="0.1.0"

def main():
    #system call to spider
    if len(sys.argv) == 1:
        subprocess.run(["scrapy", "crawl", "butler", "-s", "CLOSESPIDER_ITEMCOUNT=20","-a", "start_urls=https://old.reddit.com", "-O", "./output/output.jsonl"])
    else:
        #build list of subs to gather
        subprocess.run(["scrapy", "crawl", "butler", "-s", "CLOSESPIDER_ITEMCOUNT=20", "-a", "start_urls=" , "-O", "./output/output.jsonl"])

if __name__ == "__main__":
    main()