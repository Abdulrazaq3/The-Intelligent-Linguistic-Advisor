from fastapi import FastAPI
from app.api.routes_rag import router as rag_router

app = FastAPI(
    title="TILA RAG Backend",
    description="Arabic Grammar RAG API built with Qwen + ChromaDB",
    version="1.0.0"
)

# تسجيل الراوتر
app.include_router(rag_router)

# Endpoints removed for security reasons before pushing to GitHub