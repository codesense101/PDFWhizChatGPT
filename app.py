import os
import pickle
from dotenv import load_dotenv
import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.callbacks import get_openai_callback


# sidebar contents
with st.sidebar:
    st.title("💬PDFWhizChat")
    st.markdown('''
    ## About
    This app is an LLM powered chat app.
    - [Streamlit](https://streamlit.io)
    - [Langchat](https://langchat.github.io)
    - [OpenAI](https://openai.com)
    ''')
    add_vertical_space(5)  # add 5 vertical space
    st.write("Made with :heart: by [Wipro](https://wipro.com)")



def main():
    # main contents
    st.header("Chat with PDF 💬")

    # Load the environment variables
    load_dotenv()

    # Upload a PDF file
    pdf_file = st.file_uploader("Upload a PDF file", type=["pdf"])

    # If a PDF file is uploaded
    if pdf_file is not None:
        st.write(f"File name: {pdf_file.name}")

        # Load the PDF file
        pdf_reader = PdfReader(pdf_file)
        
        # Extract the text from the PDF
        text=""
        for page in pdf_reader.pages:
            text += page.extract_text()
        
        # Split the text into chunks
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,    #`chunk_size` is the number of characters in each chunk
            chunk_overlap=200,  #`chunk_overlap` is the number of characters to overlap chunks
            length_function=len,    #`length_func` is the function used to calculate the length of a text
        )
        chunks = text_splitter.split_text(text)

        store_name = pdf_file.name[:-4]

        # Check if the vector store exists
        if os.path.exists(f"{store_name}.pkl"):
            # Load the vector store
            with open(f"{store_name}.pkl", "rb") as f:
                VectorStore = pickle.load(f)
                st.write('Embeddings loaded from the disk')
        else:   # If the vector store does not exist
            # Load the OpenAI Embeddings
            embeddings = OpenAIEmbeddings()
            VectorStore = FAISS.from_texts(chunks, embeddings)
            # Save the vector store
            with open(f"{store_name}.pkl", "wb") as f:
                pickle.dump(VectorStore, f)
            st.write('Embeddings computed and saved to the disk')

        # Accept User questions/ query
        query = st.text_input("Ask questions about your PDF file:")  
        st.write('👨: ', query)
        
        if query:
            # Search for the most similar chunks
            docs = VectorStore.similarity_search(query, k=2)
            # st.write('LLM: ', docs)
            
            # Load the LLM
            # NOTE: Change the LLM model here
            llm = OpenAI(model_name='gpt-3.5-turbo',temperature=0.7)
            
            # Load the LLM chain
            chain = load_qa_chain(llm, chain_type="stuff")

            # Create a callback to log the OpenAI API usage
            with get_openai_callback() as cb:
                # Answer the question
                response = chain.run(input_documents=docs, question=query)
                print(cb)
            # Print the answer
            st.write('🤖: ', response)


if __name__ == "__main__":
    main()
