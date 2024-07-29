from haystack.components.retrievers.in_memory import InMemoryBM25Retriever
from haystack.components.generators import HuggingFaceLocalGenerator

def get_retriever(document_store):
    document_store = document_store
    retriever = InMemoryBM25Retriever(
        document_store=document_store,
    )
    return retriever

def get_generator():
    generator = HuggingFaceLocalGenerator(
        model="google/flan-t5-large",
        task="text2text-generation",
        generation_kwargs={
        "max_new_tokens": 100,
        "temperature": 0.9,
        })
    return generator