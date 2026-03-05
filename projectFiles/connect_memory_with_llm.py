from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint,HuggingFaceEmbeddings
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_classic.retrievers.document_compressors import LLMChainExtractor
from langchain_classic.retrievers.contextual_compression import ContextualCompressionRetriever

load_dotenv()

# step 1: setup LLM and chat model 

llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-120b",
    temperature=0.7,
    task="text-generation"
)

chat_model = ChatHuggingFace(llm = llm)


# step 2: setup embedding model 

embedding_model = HuggingFaceEmbeddings(model_name = "sentence-transformers/all-MiniLM-L6-v2")



#step 3: create prompt 

template="""
use the piece of information provided in the context to answer user's question. 
If you don't know the answer, just say that you don't know, don't try to make up an answer.
Don't provide anything out of the given context\n\n

context: {context}\n
Question: {question}\n\n

start the answer directly. No small talk please
"""

prompt = PromptTemplate(
    template=template,
    input_variables=["context","question"]
)



#step 4: loading vector database

DB_FAISS_PATH = "vectorDatabase/db_FAISS"
vectorstore = FAISS.load_local(DB_FAISS_PATH,embedding_model,allow_dangerous_deserialization=True)

# set up base retriever
base_retriever = vectorstore.as_retriever()

# compressor
llm = chat_model
compressor = LLMChainExtractor.from_llm(llm)

compression_retriever = ContextualCompressionRetriever(
    base_retriever=base_retriever,
    base_compressor=compressor
)


def ask_question(user_query):

    results = compression_retriever.invoke(user_query)

    context = "\n\n".join(docs.page_content for docs in results)

    final_prompt = prompt.invoke({
        "context": context,
        "question": user_query
    })

    result = chat_model.invoke(final_prompt)

    return result.content



# user_query = input("Write user Query: ")

# results = compression_retriever.invoke(user_query)

# # print(f"Result: {results}")

# context = "\n\n".join(docs.page_content for docs in results)

# final_prompt = prompt.invoke({"context":context,"question":user_query})

# result = chat_model.invoke(final_prompt)

# print(f"Final answer: {result.content}")

