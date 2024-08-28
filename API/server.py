from fastapi import FastAPI
from .models.Query import Query
from RagCore.pipeline import get_pipeline
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()
pipe = get_pipeline()

@app.post("/query")
def query(query: Query):
    result = pipe.run(
        {
            "retriever": {"query": query.question, "top_k": 5},
            "prompt_builder": {"query": query.question},
        }
    )
    torch.cuda.empty_cache()
    return {"answer": result}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "server:app",
        host="0.0.0.0",
        port=7001,
        reload=True
    )