# Embeddings with ChromaDB Basic Example
# Use: LangChain & ChromaDB
# Data extracted from Wikipedia on Generative AI

import os
import warnings
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from configparser import ConfigParser
import chromadb
from chromadb.utils import embedding_functions

warnings.filterwarnings("ignore")


# --- Authentication ---
# Read API key from environment (injected via OpenShift secrets or .env)
# Get API details from config.ini

config = ConfigParser()
with open("config.ini") as f:
    config.read_file(f)

openai_api_key = os.environ["AIM_API_KEY"]
os.environ["OPENAI_API_VERSION"] = config.get("aim", "api_version")
OPENAI_API_BASE = config.get("aim", "url")
OPENAI_API_TYPE = config.get("aim", "type")


# --- Initialising Embedding Model ---

embeddingsoai = embedding_functions.OpenAIEmbeddingFunction(
    deployment_id="aim-text-embedding-3-large-lab",
    api_type="azure",
    api_base=OPENAI_API_BASE,
    api_key=openai_api_key,
    api_version="2024-06-01"
)


# --- Loading text document and Chunking with no overlap ---
# Using Character text splitter.
# Other options: Split Code, Markdown Header Text Splitter,
# Recursively Split By Character & Split by Token
# See LangChain Docs: https://python.langchain.com/docs/modules/data_connection/document_transformers/text_splitters/character_text_splitter

loader = TextLoader("gaiwiki.txt")
documents = loader.load()

text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

print(docs[0].page_content)
print(len(docs))


# --- Creating Chroma client & Loading ---
# Default embedding model if not specified: sentence_transformer
# Customize distance method using arg "metadata" in create_collection
# Distance method options: l2, ip or cosine

def create_chroma_db(documents, name):
    chroma_client = chromadb.Client()
    db = chroma_client.create_collection(
        name=name,
        metadata={"hnsw:space": "cosine"},
        embedding_function=embeddingsoai
    )
    for i in range(len(documents)):
        db.add(
            documents=documents[i].page_content,
            ids=str(i),
            metadatas=documents[i].metadata
        )
    return db


db = create_chroma_db(docs, "gaiwiki")


# --- Query Chroma ---

def get_relevant_passage(query, db):
    passage = db.query(query_texts=[query], n_results=1)['documents'][0][0]
    return passage


passage = get_relevant_passage("Controversy in 2023", db)
print(passage)
