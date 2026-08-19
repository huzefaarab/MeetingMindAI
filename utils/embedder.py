import chromadb
from chromadb.utils import embedding_functions
from pathlib import Path


def embed_chunks(chunk_docs):
    embedding_function = embedding_functions.DefaultEmbeddingFunction()

    

    embeddings = embedding_function(chunk_docs)

    return embeddings

def store_chunks(chunks, embeddings):
    db_path=Path("database/")
    db_path.mkdir(parents=True,exist_ok=True)
    client = chromadb.PersistentClient(path=db_path)
    collection = client.get_or_create_collection(name="MeetingMindAI")

    ids = [
        f"{chunk['metadata']['source']}_{chunk['metadata']['chunk_index']}"
        for chunk in chunks
    ]

    try:
        collection.upsert(
            ids=ids,
            documents=[chunk["text"] for chunk in chunks],
            metadatas=[chunk["metadata"] for chunk in chunks],
            embeddings=embeddings
        )


    except Exception as e:
        print("ACTUAL ERROR:", e)
        raise