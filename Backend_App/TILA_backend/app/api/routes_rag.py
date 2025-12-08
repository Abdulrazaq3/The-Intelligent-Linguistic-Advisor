from fastapi import APIRouter, HTTPException
from app.models.schemas import RAGRequest, RAGResponse
from app.core.rag import rag_answer

router = APIRouter(
    prefix="/rag",
    tags=["RAG"]
)

# Endpoints removed for security reasons before pushing to GitHub