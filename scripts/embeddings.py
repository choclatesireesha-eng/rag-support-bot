import os
import numpy as np
import faiss

CHUNKS_FILE = "data/chunks.txt"
FAISS_INDEX_FILE = "data/faiss.index"
METADATA_FILE = "data/metadata.txt"

# Read chunks
chunks = []
metadata = []

with open(CHUNKS_FILE, "r", encoding="utf-8") as f:
    for line in f:
        parts = line.strip().split("\t")
        if len(parts) >= 3:
            chunk_id, source, chunk_text = parts[0], parts[1], "\t".join(parts[2:])
            chunks.append(chunk_text)
            metadata.append(f"{chunk_id}\t{source}")

# Create FAISS index
dimension = 1536
index = faiss.IndexFlatL2(dimension)  # L2 distance
embeddings = np.random.rand(len(chunks), dimension).astype("float32")
index.add(embeddings)

# Save index
faiss.write_index(index, FAISS_INDEX_FILE)

# Save metadata
with open(METADATA_FILE, "w", encoding="utf-8") as f:
    for item in metadata:
        f.write(f"{item}\n")

print(f"Saved {len(chunks)} embeddings to {FAISS_INDEX_FILE}")


