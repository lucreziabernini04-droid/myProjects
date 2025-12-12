# Lausanne Hackathon – Civic RAG Chatbot

Hackathon project focused on building a Retrieval-Augmented Generation (RAG) chatbot
to provide clear and accessible information from official public administration sources.

The system was designed as a lightweight, deployable prototype with a conversational
interface aimed at improving citizen access to institutional content.

## Context
Hackathon project – Lausanne, Switzerland  
Team-based development under time constraints (MVP-oriented)

## What We Built
- A civic chatbot answering user questions using retrieved official content
- A Retrieval-Augmented Generation (RAG) pipeline
- A Streamlit-based interactive web application
- A Dockerized setup for easy deployment

## Data Sources
- Official Canton of Vaud website content
- HTML pages parsed and processed for information retrieval

## Architecture & Technologies
- **Frontend**: Streamlit
- **Backend**: Python
- **Retrieval**: Sentence Transformers + FAISS
- **Document Processing**: BeautifulSoup, PyPDF2
- **Language Model**: **Apertus (open-source LLM)**
- **Deployment**: Docker

## Key Features
- Conversational interface with chat history
- Context-aware answers grounded in retrieved documents
- Fully open-source oriented pipeline

## My Contribution
- Development and testing of the RAG pipeline
- Streamlit interface implementation
- Prompt design and response evaluation
- Integration and debugging of the end-to-end system

## Notes
This repository contains hackathon code and rapid prototypes. The focus was on
functionality and clarity rather than production-level optimization.
