import streamlit as st
from pathlib import Path
import time

from pipeline import (ingestion,answer_query)


st.title("        MeetingMindAI")


if "upload_mode" not in st.session_state:
    st.session_state.upload_mode=False

if "question_mode" not in st.session_state:
    st.session_state.question_mode=False


button1,button2,spacer1,spacer2,spacer3=st.columns([1,1,1,1,1])


with button1:
    if st.button("Upload Transcript") :
        st.session_state.upload_mode=True

with button2:
    if st.button("Ask a Question"):
        st.session_state.question_mode=True
        

if "chat_history" not in st.session_state:
    st.session_state.chat_history={}


if st.session_state.question_mode:
    query=st.chat_input("Enter Your Query")
    
    if query is not None:
        with st.spinner("Generating an answer"):

            answer=answer_query(query)
            st.session_state.chat_history[query]=answer
            for query,response in st.session_state.chat_history.items():
                st.chat_message("user").write(query)
                st.chat_message("assistant").write(response)
                
    


if st.session_state.upload_mode:
    uploaded_file=st.file_uploader("Upload a .md/.pdf/.txt/.docx file ",type=["md","txt","pdf","docx"])
    if uploaded_file is not None:

        source_path= Path("data/Company X")/uploaded_file.name
        source_path.parent.mkdir(parents=True, exist_ok=True)

        with open(source_path,"wb") as file:
            file.write(uploaded_file.getbuffer())
        st.write(f"Selected File : {uploaded_file.name}")

        if st.button("Start Ingestion"):
            st.write("Starting ingestion...")
            ingestion(filepath=source_path)
            st.success("Ingestion done")
            time.sleep(1.3)


            st.session_state.upload_mode=False
            st.rerun()    

            


            
        

        
