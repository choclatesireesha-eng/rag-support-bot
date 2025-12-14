import requests
from bs4 import BeautifulSoup

# Replace this with the website you want to crawl
URL = "https://example.com"

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

# Extract all visible text
text = soup.get_text()

# Save to a file
with open("../data/site.txt", "w", encoding="utf-8") as f:
    f.write(text)

print("Website text saved to data/site.txt")
