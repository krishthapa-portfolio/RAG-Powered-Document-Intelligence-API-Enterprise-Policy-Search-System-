from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

# Step 1: Load PDF
loader = PyPDFLoader("data/sample.pdf")
documents = loader.load()

# Step 2: Split into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=100
)

chunks = text_splitter.split_documents(documents)

# Step 3: Create embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-mpnet-base-v2"
)

# Step 4: Store in ChromaDB
vectorstore = Chroma.from_documents(
    chunks,
    embeddings,
    persist_directory="db"
)

vectorstore.persist()

print("✅ Data ingested and stored in ChromaDB")