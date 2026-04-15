# 🔹 IMPORTS
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os


# 🔹 LOAD ENV
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")


# 🔹 EMBEDDINGS + DB
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-mpnet-base-v2"
)

vectorstore = Chroma(
    persist_directory="db",
    embedding_function=embeddings
)


# 🔹 LOAD GROQ MODEL
llm = ChatGroq(
    api_key=api_key,
    model="openai/gpt-oss-120b"
)


# 🔥 CORE FUNCTION (THIS IS THE AI BRAIN)
def ask_question(question):

    docs = vectorstore.similarity_search(question, k=3)

    context = "\n\n".join([d.page_content for d in docs])

    prompt = f"""
    You are a helpful assistant.

    Use ONLY this context to answer
    {context}

    Question: {question}
    """

    response = llm.invoke(prompt)

    return response.content


# 🧪 TEST BLOCK (RUNS ONLY WHEN YOU EXECUTE FILE DIRECTLY)
if __name__ == "__main__":
    print(ask_question("What is vacation policy?"))





