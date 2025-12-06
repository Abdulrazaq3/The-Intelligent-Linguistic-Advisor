from openai import OpenAI
import chromadb
from app.core.config import settings


# ========= 1) Fireworks Client =========

client = OpenAI(
    api_key=settings.FIREWORKS_API_KEY,
    base_url="https://api.fireworks.ai/inference/v1"
)

# أسماء النماذج من الإعدادات
EMBED_MODEL = settings.EMBEDDING_MODEL
LLM_MODEL = settings.LLM_MODEL


def get_embeddings(text_list):
    """إرجاع Embeddings من Qwen3-Embedding-8B (بُعد 4096)."""
    clean = [t.replace("\n", " ") for t in text_list]
    resp = client.embeddings.create(
        model=EMBED_MODEL,
        input=clean,
    )
    return [d.embedding for d in resp.data]


# ========= 2) ChromaDB Connection =========

db = chromadb.PersistentClient(path=settings.CHROMA_PATH)
collection = db.get_collection("grammar_collection")


# ========= 3) Context Retrieval =========

def retrieve_context(question: str, top_k: int = 3):
    """استرجاع أفضل k مقاطع من قاعدة البيانات."""
    embedding = get_embeddings([question])

    results = collection.query(
        query_embeddings=embedding,
        n_results=top_k,
        include=["documents"]
    )

    docs = results.get("documents", [[]])[0]

    if not docs:
        return None
    
    return "\n---\n".join(docs)


# ========= 4) RAG Answer Generation =========

def rag_answer(question: str) -> str:
    """يعطي جواب باستخدام RAG فقط."""
    
    context = retrieve_context(question)

    if not context:
        return "عذراً، لم أجد أي معلومات مطابقة في قاعدة البيانات."

    system_instruction = """
أنت مساعد صارم في النحو والصرف.
تجيب فقط بناءً على الـ Context المعطى.
إذا لم توجد إجابة في السياق، قل:
"عذراً، لا توجد معلومات كافية في البيانات للإجابة على هذا السؤال."
جاوب بالعربية فقط.
"""

    prompt = f"""
Context:
{context}

سؤال المستخدم:
{question}
"""

    response = client.chat.completions.create(
        model=LLM_MODEL,
        messages=[
            {"role": "system", "content": system_instruction},
            {"role": "user", "content": prompt},
        ],
        temperature=0.0,
        max_tokens=200,
    )

    return response.choices[0].message.content
