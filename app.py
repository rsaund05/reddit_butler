import typer
import subprocess

__app_name__="reddit_butler"
__version__="0.1.0"

def main(urls: str):
    #system call to spider
    print("Grabbing: " + urls)
    subprocess.run(["scrapy", "crawl", "butler", "-s", "CLOSESPIDER_ITEMCOUNT=20", "-a", "start_urls=" + urls, "-O", "./output/output.jsonl"])

if __name__ == "__main__":
    typer.run(main)