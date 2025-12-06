# The Intelligent Linguistic Advisor  
المستشار اللغوي – فريق رنان

This repository contains the project **“Linguistic Advisor” (المستشار اللغوي)** developed by **Team Ranan** as part of the Samsung – Misk AI Innovation program.

The project is motivated by the growing need for accessible, accurate, and fast linguistic support in Modern Standard Arabic as digital communication expands.  
Our main objective is to develop an **AI-powered conversational system** capable of delivering high-quality linguistic consultations using **trusted, authoritative datasets** from the King Salman Global Academy for Arabic Language.  
The system aims to improve users’ writing quality, increase their linguistic confidence, and reinforce the presence of Arabic in the digital age.

---

## 3. Repository Structure

The repository is organized as follows:

- `Data_preparation/`  
  Consists of notebook for data preprocessing and preparation.

- `AI_system_and_evaluation/`  
  Consists of notebooks for building the AI system, RAG pipeline, evaluation, and results.

- `SIC_AI_Capstone Project_Final Report`  
  Full written report describing the system, methodology, experiments, and results.

- `SIC AI Presentation`  
  Final presentation slides.

- `SIC_AI_Capstone Project_Work Breakdown Structure`  
  WBS file summarizing project tasks and timeline.

- `Backend & Web Application (`backend_app/`)` 

This folder contains the end-to-end application used to serve the Intelligent Linguistic Advisor through a web interface. It combines a **FastAPI backend** with a simple **React frontend**.

- Location: `backend_app/main.py` and related modules.
- Responsibilities:
  - Exposes REST endpoints for the RAG pipeline.
  - Connects to the vector database (ChromaDB) and the Qwen models.
  - Handles query → retrieval → generation → response flow for the chatbot.

---

## 4. Technical Overview

- AI-powered conversational assistant for Modern Standard Arabic.  
- Focus on grammar, morphology, syntax, spelling, and formal writing quality.  
- Uses Retrieval-Augmented Generation (RAG) over curated Arabic linguistic references.  
- Implemented using Python and standard NLP / deep learning tools (Jupyter notebooks, data pipelines, and evaluation scripts).

---

## 5. Team – Ranan

- **Abdulrazaq Al-Dawsari** – [LinkedIn](https://www.linkedin.com/in/abdulrazaq-h-aldawsari-046511209?)  
- **Rahaf Mahfoudh** – [LinkedIn](https://www.linkedin.com/in/rahaf-faiz-81b267251?)  
- **Raniyah Alghamdi** – [LinkedIn](https://www.linkedin.com/in/raniyah-alghamdi?)  
- **Maher Alhijile** – [LinkedIn](https://www.linkedin.com/in/maher-alhijile/)  
- **Bader Alshamrani** – [LinkedIn](https://www.linkedin.com/in/bader-alshamrani-49a04a245?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app)  
- **Shahad Alnashwan** – [LinkedIn](https://www.linkedin.com/in/shahad-alnashwan?utm_source=share_via&utm_content=profile&utm_medium=member_ios)  

> **Note:** All team members jointly contributed to developing and optimizing the model to achieve strong performance and reliability.
