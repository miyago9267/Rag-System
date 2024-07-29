from fastapi import FastAPI
from .models.Query import Query
from RagCore.pipeline import get_pipeline

app = FastAPI()
pipe = get_pipeline()

@app.post("/query")
def query(query: Query):
    result = pipe.run(query=query.question, params={"Retriever": {"top_k": 10}})
    return {"answer": result['answers'][0].answer}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "server:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )