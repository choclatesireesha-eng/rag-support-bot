import re

# Read the crawled text
with open("../data/site.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Clean the text
text = re.sub(r'\s+', ' ', text)  # Replace all whitespace (tabs/newlines) with a single space
text = text.strip()

# Chunk the text
chunk_size = 500  # characters per chunk
chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

# Save chunks to a new file
with open("../data/chunks.txt", "w", encoding="utf-8") as f:
    for idx, chunk in enumerate(chunks):
        f.write(f"--- Chunk {idx+1} ---\n{chunk}\n\n")

print(f"{len(chunks)} chunks saved to data/chunks.txt")
