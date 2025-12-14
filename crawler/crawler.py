# crawler/crawler.py

import requests
import os
import sys
from urllib.parse import urlparse

def crawl_website(base_url):
    response = requests.get(base_url)
    domain = urlparse(base_url).netloc.replace(".", "_")
    output_dir = "data/raw_html"
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, f"{domain}.html")

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(response.text)
    
    print(f"Saved HTML for {base_url}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python crawler.py <base_url>")
        sys.exit(1)
    
    base_url = sys.argv[1]
    crawl_website(base_url)
