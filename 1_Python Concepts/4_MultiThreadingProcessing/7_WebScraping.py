import threading
import requests
from bs4 import BeautifulSoup

urls = [
    "https://example.com/page1",
    "https://example.com/page2",
    "https://example.com/page3",
]

session = requests.Session()
def fetch_contents(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")
        print(f"{len(soup.text)} characters from {url}")
    except requests.RequestException as e:
        print(f"Failed to fetch {url}: {e}")

threads = []
for url in urls:
    thread = threading.Thread(target=fetch_contents, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All web pages fetched")

#Another Version
from concurrent.futures import ThreadPoolExecutor

def fetch_contents(url):
    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.content, "html.parser")
    return len(soup.text)

with ThreadPoolExecutor(max_workers=len(urls)) as executor:
    results = list(executor.map(fetch_contents, urls))

for url, count in zip(urls, results):
    print(f"{count} characters from {url}")