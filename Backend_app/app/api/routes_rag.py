from fastapi import APIRouter, HTTPException
from app.models.schemas import RAGRequest, RAGResponse
from app.core.rag import rag_answer

router = APIRouter(
    prefix="/rag",
    tags=["RAG"]
)


@router.post("/", response_model=RAGResponse)
def ask_rag(payload: RAGRequest):
    """استقبال سؤال من المستخدم وإرجاع إجابة RAG."""
    question = payload.question.strip()

    if not question:
        raise HTTPException(status_code=400, detail="السؤال لا يمكن أن يكون فارغًا.")

    answer = rag_answer(question)

    return RAGResponse(
        question=question,
        answer=answer
    )
