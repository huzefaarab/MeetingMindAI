from utils.filehandler import extract_text
from utils.parser import chunk_text
from utils.embedder import (embed_chunks,store_chunks)
from utils.retriever import semantic_search
from utils.llm import generate_response

RAG_PROMPT="""This is a RAG System and
 the follwing is the Query : {query} and 
 the following are the Relevant chunks : {relevant_chunks}

 Instructions: 
 1.DO NOT invent Information
 2.Only answer to questions that are relevant to the given chunks

"""



def ingestion(filepath):

    try:
        #Text Extraction
        text,source_file=extract_text(file_path=filepath)

        #Chunks
        chunks=chunk_text(text=text,source_file=source_file)
        
        #Embeddings
        embeddings=embed_chunks([chunk["text"] for chunk in chunks])

        #Store
        store_chunks(chunks=chunks,embeddings=embeddings)

        
    except Exception as e:
        raise Exception("Ingestion Failed with Error : ",e)


def answer_query(query):

    #Getting Relevant chunks
    relevant_chunks=semantic_search(query=query)

    #Filtering soruces and docs
    relevant_text=relevant_chunks["documents"][0]
    relevant_sources=[source["source"] for source in relevant_chunks["metadatas"][0]]

    #merging sources and docs
    relevant_context=[f"Document :\n {doc} \n Source : {source}" for doc,source in zip(relevant_text,relevant_sources)]
        
    #Getting the Answer
    prompt=RAG_PROMPT.format(query=query,relevant_chunks=relevant_context)
    answer=generate_response(prompt)
        
    return answer
















    

    