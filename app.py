import streamlit as st
import pandas as pd
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Load data
df = pd.read_csv("students_cleaned.csv")

# Combine text
documents = df.apply(
    lambda row: f"{row['Name']} is {row['Age']} years old, lives in {row['City']} and studies {row['Course']}.",
    axis=1
)

# Embeddings
model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(documents.tolist())

# FAISS index
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(np.array(embeddings))

# Streamlit UI
st.title("🎓 Student RAG Chatbot")

query = st.text_input("Ask about students:")

if query:
    query_embedding = model.encode([query])
    D, I = index.search(query_embedding, k=1)
    st.write("Answer:")
    st.write(documents.iloc[I[0][0]])
