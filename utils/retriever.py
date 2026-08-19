import chromadb
from chromadb.utils import embedding_functions


def semantic_search(query,collection_name="MeetingMindAI"):

    embedding_function=embedding_functions.DefaultEmbeddingFunction()

    question_embedding=embedding_function([query])

    client=chromadb.PersistentClient("database/")
    collection=client.get_collection(name=collection_name)

    relevant_chunks=collection.query(n_results=5,query_embeddings=question_embedding)

    return relevant_chunks
