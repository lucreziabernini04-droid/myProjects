# Innovaite Hackathon – AI Assistant for University Websites

Hackathon project aimed at simplifying students’ interaction with complex university websites
through an AI-powered assistant.

The system helps users retrieve official information and, when data is missing, automatically
generates a personalized email to the appropriate university office, reducing friction and
administrative workload.

## Context
Hackathon project – Innovaite / dAIe  
Team-based development

## Problem
University websites often contain fragmented and hard-to-navigate information.
Students frequently fail to find essential details, leading to frustration, delays, and
increased workload for university help desks.

## Solution
An AI assistant based on Retrieval-Augmented Generation (RAG) that:
- Retrieves official information from university documents and websites
- Answers students’ questions conversationally
- Automatically generates a personalized email to the university office when information
  is missing, allowing the user to send it with a single click

## Architecture & Technologies
- **Backend**: Python
- **API**: FastAPI
- **Retrieval**: RAG pipeline with vector database (Qdrant)
- **Document ingestion**: PDF parsing and indexing
- **Frontend**: Browser extension (HTML, CSS, JavaScript)
- **Framework**: DataPizza AI framework

## Key Features
- No manual website navigation required
- Reduced help desk workload
- Automatic email generation with all relevant information
- Reduced hallucinations thanks to RAG grounding
- Seamless integration into existing university websites via browser extension

## Project Structure
The prototype includes:
- A backend service handling chat, retrieval, and escalation
- A RAG pipeline for document ingestion and querying
- A browser extension embedding the assistant directly into university webpages

## My Contribution
- Contribution to the RAG-based solution design
- Participation in system architecture and feature definition
- Collaboration on user experience and escalation workflow

## Roadmap
Planned future developments include:
- Integration with official university websites
- Scalability to multiple universities and ticketing systems
- Answer confidence scoring
- Expanded document coverage and full web scraping
- User authentication and self-learning from help desk replies
