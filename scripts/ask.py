import faiss
import numpy as np

# Load FAISS index
INDEX_FILE = "data/faiss.index"
index = faiss.read_index(INDEX_FILE)

# Load metadata (chunk_id + source)
METADATA_FILE = "data/metadata.txt"
with open(METADATA_FILE, "r", encoding="utf-8") as f:
    metadata = [line.strip() for line in f]

# Function to retrieve top-k chunks
def retrieve_chunks(query_embedding, k=3):
    D, I = index.search(query_embedding, k)
    top_chunks = []
    for idx in I[0]:
        if idx == -1:
            continue
        top_chunks.append(metadata[idx])
    return top_chunks

# Function to combine retrieved chunks into context
def combine_chunks(chunks):
    combined = ""
    for chunk in chunks:
        combined += f"{chunk}\n"
    return combined

# Main function
def main():
    question = input("Enter your question: ")

    # For testing: generate random query embedding (1536-dim)
    query_embedding = np.random.rand(1, 1536).astype("float32")

    top_chunks = retrieve_chunks(query_embedding, k=3)
    context = combine_chunks(top_chunks)

    # Mock answer using retrieved context
    answer = f"Answer based on retrieved context:\n{context}\nQuestion: {question}\nAnswer: This site provides documentation examples."

    print("\n--- RAG Bot Response ---")
    print(answer)
    print("\nSources:")
    for chunk in top_chunks:
        print(f"- {chunk}")

if __name__ == "__main__":
    main()
