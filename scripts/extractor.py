from bs4 import BeautifulSoup
import os

INPUT_DIR = "data/raw_html"
OUTPUT_DIR = "data/cleaned_text"

os.makedirs(OUTPUT_DIR, exist_ok=True)

def clean_html(html):
    soup = BeautifulSoup(html, "lxml")

    # Remove scripts, styles
    for tag in soup(["script", "style", "header", "footer", "nav", "aside"]):
        tag.decompose()

    # Get text
    text = soup.get_text(separator="\n")

    # Remove empty lines
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    return "\n".join(lines)

if __name__ == "__main__":
    # Example: read saved HTML files
    for filename in os.listdir(INPUT_DIR):
        if filename.endswith(".html"):
            filepath = os.path.join(INPUT_DIR, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                html = f.read()

            cleaned_text = clean_html(html)

            # Save cleaned text
            output_path = os.path.join(OUTPUT_DIR, filename.replace(".html", ".txt"))
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(cleaned_text)

            print(f"Cleaned {filename}")
