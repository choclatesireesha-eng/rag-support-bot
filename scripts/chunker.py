import os
import uuid

INPUT_DIR = "data/cleaned_text"
OUTPUT_FILE = "data/chunks.txt"

CHUNK_SIZE = 500
CHUNK_OVERLAP = 50

chunks = []

for filename in os.listdir(INPUT_DIR):
    if filename.endswith(".txt"):
        filepath = os.path.join(INPUT_DIR, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            text = f.read()

        start = 0
        while start < len(text):
            end = min(start + CHUNK_SIZE, len(text))
            chunk_text = text[start:end]

            chunk_id = str(uuid.uuid4())
            # Fix: replace newlines in chunk text to avoid breaking tabs
            clean_chunk_text = chunk_text.replace("\n", " ").replace("\r", "")
            
            # Append properly formatted line
            chunks.append(f"{chunk_id}\t{filename}\t{clean_chunk_text}\n")

            start += CHUNK_SIZE - CHUNK_OVERLAP

# Save all chunks
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.writelines(chunks)

print(f"Saved {len(chunks)} chunks to {OUTPUT_FILE}")

