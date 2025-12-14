# app/main.py

from fastapi import FastAPI
from pydantic import BaseModel
import subprocess
import os

app = FastAPI()

# -------------------------------
# Request models
# -------------------------------
class CrawlRequest(BaseModel):
    baseUrl: str

class AskRequest(BaseModel):
    question: str

# -------------------------------
# Crawl endpoint
# -------------------------------
@app.post("/crawl")
def crawl(request: CrawlRequest):
    base_url = request.baseUrl
    script_path = os.path.join(os.getcwd(), "crawler", "crawler.py")

    if not os.path.exists(script_path):
        return {"error": f"{script_path} not found."}

    try:
        subprocess.run(["python", script_path, base_url], check=True)
        return {"message": f"Simulated crawl for {base_url}"}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}

# -------------------------------
# Ask endpoint
# -------------------------------
@app.post("/ask")
def ask(request: AskRequest):
    question = request.question

    # Load chunks metadata
    chunks_file = os.path.join(os.getcwd(), "data", "chunks.txt")
    if not os.path.exists(chunks_file):
        return {"error": f"{chunks_file} not found. Run the chunker first."}

    with open(chunks_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # For testing: return top 3 chunks (mock retrieval)
    top_chunks = []
    for line in lines[:3]:  # take first 3 chunks as "top chunks"
        top_chunks.append(line.strip())

    # Combine into a context
    context = "\n".join(top_chunks)

    # Generate mock answer
    answer = f"Answer based on retrieved context:\n{context}\nQuestion: {question}\nAnswer: This site is for documentation examples."

    return {
        "answer": answer,
        "sources": top_chunks
    }

