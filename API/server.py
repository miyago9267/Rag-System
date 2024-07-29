from fastapi import FastAPI
from .models.Query import Query
from RagCore.pipeline import get_pipeline
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
pipe = get_pipeline()

@app.post("/query")
def query(query: Query):
    result = pipe.run(
        {
            "retriever": {"query": query.question},
            "prompt_builder": {"question": query.question},
        }
    )
    return {"answer": result["llm"]["replies"]}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "server:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )