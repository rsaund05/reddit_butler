import sys, getopt
import subprocess
import argparse

__app_name__="reddit_butler"
__version__="0.1.0"

def main():
    subs = []
    parser = argparse.ArgumentParser(description="Reddit Butler. Scan and collect reddit data without pesky API access.")
    parser.add_argument(
        '-d',
        '--debug',
        help='debug flag, for testing single post retrival'
    )
    parser.add_argument(
        '--subs', 
        '-s', 
        type=str,
        nargs='+',
        help='optional list of subreddits to scan. Scans homepage if nothing is passed in.',
        default=[]
    )
    args = parser.parse_args()
    for s in args.subs:
        subs.append("https://old.reddit.com/r/" + s)

    if len(subs) == 0:
        subs_url = 'https://old.reddit.com/'
    else:
        subs_url = ','.join(subs) #stringified list of URLs sepereated by comma
    subprocess.run(["scrapy", "crawl", "butler", "-s", "CLOSESPIDER_ITEMCOUNT=50", "-a", "start_urls=" + subs_url, "-O", "./output/output.jsonl"])

if __name__ == "__main__":
    main()