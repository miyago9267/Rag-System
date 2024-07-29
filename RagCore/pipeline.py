from haystack import Pipeline
from .document_store import get_document_store
from .retriever_generator import get_retriever, get_generator
from .prompt_builder import get_prompt_builder

def get_pipeline():
    retriever = get_retriever(get_document_store())
    generator = get_generator()
    prompt_builder = get_prompt_builder()

    rag_pipeline = Pipeline()
    rag_pipeline.add_component("retriever", retriever)
    rag_pipeline.add_component("prompt_builder", prompt_builder)
    rag_pipeline.add_component("llm", generator)
    rag_pipeline.connect("retriever", "prompt_builder.documents")
    rag_pipeline.connect("prompt_builder", "llm")
    return rag_pipeline