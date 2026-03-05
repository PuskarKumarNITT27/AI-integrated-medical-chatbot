from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint, HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv

load_dotenv()

#constants
DATA_PATH="./"    #always take relative path from the directory where you are running command

#step 1: Load the pdfs

def load_pdf_files(data_path):
    loader = DirectoryLoader(
        data_path,
        glob="*.pdf",
        loader_cls=PyPDFLoader
    )
    
    documents = loader.lazy_load()
    return documents

documents = load_pdf_files(data_path=DATA_PATH)

# print("length of pdf pages",len(load_pdf_files(data_path=DATA_PATH)))

#steps 2: create chunks 

def create_chunks(extracted_text):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    
    text_chunks = text_splitter.split_documents(extracted_text)
    return text_chunks

text_chunks = create_chunks(documents)
print(f"Number of chunks : {len(text_chunks)}")


# step 3: create vector embeddings

def get_embedding_model():
    
    embedding_model = HuggingFaceEmbeddings(model_name = "sentence-transformers/all-MiniLM-L6-v2")
    
    return embedding_model

embedding_model = get_embedding_model()

# step 4: store embeddings in FAISS

DB_FAISS_PATH = "vectorDatabase/db_FAISS"

db = FAISS.from_documents(text_chunks,embedding_model)

db.save_local(DB_FAISS_PATH)