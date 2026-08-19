# MeetingMind AI

## AI Meeting Memory Assistant

MeetingMind AI is an AI-powered meeting memory assistant that helps users retrieve important discussions, decisions, tasks, and deadlines from meeting transcripts.

Instead of manually searching through lengthy meeting transcripts, users can upload a transcript and ask questions in natural language. The system retrieves relevant sections from the transcript and uses an LLM to generate a context-aware answer.

---

## Project Status

✅ **Version 1 Completed**

Current Version:  
**V1 - Working RAG Application**

The first version provides an end-to-end Retrieval-Augmented Generation (RAG) pipeline with a Streamlit interface.

---

## V1 Features

- Upload meeting transcripts
- Support for Markdown, TXT, PDF, and DOCX files
- Document text extraction
- Document chunking
- Text embeddings
- Persistent ChromaDB vector storage
- Semantic similarity search
- Retrieval-Augmented Generation (RAG)
- Source-aware context provided to the LLM
- Natural language question answering
- Session-based chat history
- Streamlit user interface

---

## RAG Pipeline

```text
Document
    ↓
Text Extraction
    ↓
Chunking
    ↓
Embedding
    ↓
ChromaDB
    ↓
Semantic Retrieval
    ↓
Relevant Chunks + Sources
    ↓
LLM
    ↓
Answer
```

---

## Project Structure

```text
MeetingMindAI/
│
├── app.py
├── pipeline.py
├── requirements.txt
├── README.md
│
├── data/
│   └── Company X/
│
├── database/
│   └── ChromaDB data
│
└── utils/
    ├── embedder.py
    ├── filehandler.py
    ├── llm.py
    ├── parser.py
    └── retriever.py
```

---

## Tech Stack

- Python
- Streamlit
- ChromaDB
- Gemini API
- Embeddings
- Retrieval-Augmented Generation (RAG)

---

## Current Architecture

### Ingestion Pipeline

```text
File
 ↓
Text Extraction
 ↓
Chunking
 ↓
Embedding
 ↓
ChromaDB Upsert
```

### Question Answering Pipeline

```text
User Query
 ↓
Query Embedding
 ↓
Semantic Search
 ↓
Relevant Documents + Sources
 ↓
RAG Prompt
 ↓
Gemini
 ↓
Answer
```

---

## Future Improvements

The V1 system provides the basic working RAG pipeline. Future development will focus on improving RAG quality and reliability, including:

- Chunking strategy improvements
- Embedding model evaluation
- Retrieval method improvements
- Retrieval evaluation
- RAG evaluation
- Better source citations
- Improved prompt/context construction
- Multi-meeting retrieval
- Production-oriented RAG improvements

---

## License

This project is currently under development.
