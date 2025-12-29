# Student RAG Application

This project demonstrates a complete pipeline of:
- CSV data cleaning
- RAG-based chatbot development
- Deployment on Hugging Face Spaces

## Dataset
- students_raw.csv (raw data)
- students_cleaned.csv (cleaned data)

## Data Cleaning
The data cleaning process is implemented in `clean_data.py` and includes:
- Removal of duplicate records
- Handling missing values
- Fixing invalid email addresses

## RAG Application
The chatbot is built using:
- Streamlit for UI
- Sentence Transformers for embeddings
- FAISS for similarity search

## Deployment
Hugging Face Space Link:
https://huggingface.co/spaces/gazar12/student-rag-app
