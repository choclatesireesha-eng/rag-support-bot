# RAG Support Bot

A **Q&A Support Bot** using **Retrieval-Augmented Generation (RAG)**.  
This project crawls a website, extracts and cleans text, generates embeddings, stores them in a vector database (FAISS), and provides a REST API to answer user questions using only the crawled content.

---

## Features

- Crawl website pages and internal links.
- Extract and clean visible text from HTML.
- Chunk long text into smaller pieces for embeddings.
- Generate embeddings for each chunk (simulated/random in case OpenAI quota is exceeded).
- Store embeddings and metadata in FAISS vector database.
- Retrieve relevant chunks for a user query.
- Provide answers based on retrieved context.
- REST API endpoints:
  - `POST /crawl` → Crawl and index a website.
  - `POST /ask` → Ask a question about the crawled website.

---

## Project Structure

