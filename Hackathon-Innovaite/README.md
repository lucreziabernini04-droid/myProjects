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
An AI assistant based on Retrieval-Augmented Generation (RAG) that simplifies access to
university information through two complementary integration modes:

- **Browser extension**: the assistant is embedded directly into university webpages via
  a Chrome extension, allowing students to ask questions without leaving the site.
- **Website integration**: the assistant can also be deployed directly within the
  university website as a native conversational interface.

When information is missing, the system automatically generates a personalized email to
the appropriate university office, which the user can send with a single click.

## Architecture & Technologies
- **Backend**: Python
- **API**: FastAPI (chat handling and escalation logic)
- **Retrieval**: RAG pipeline with vector database (Qdrant)
- **Document ingestion**: PDF parsing and indexing
- **Frontend (Option 1)**: Chrome browser extension (HTML, CSS, JavaScript)
- **Frontend (Option 2)**: Direct website integration
- **Framework**: DataPizza AI framework

## Key Features
- No manual website navigation required
- Dual integration: browser extension and native website deployment
- Automatic email generation with all relevant information
- Reduced help desk workload
- Reduced hallucinations thanks to RAG grounding
- Seamless user experience within existing university platforms

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
