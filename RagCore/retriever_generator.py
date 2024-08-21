from haystack.components.retrievers.in_memory import InMemoryBM25Retriever
from haystack.components.generators import HuggingFaceLocalGenerator
from haystack.utils import Secret
import os

def get_retriever(document_store):
    document_store = document_store
    retriever = InMemoryBM25Retriever(
        document_store=document_store,
    )
    return retriever

def get_generator():
    generator = HuggingFaceLocalGenerator(
        model="google/byt5-small",
        task="text2text-generation",
        token=Secret.from_token(os.getenv("HF_API_TOKEN")),
        generation_kwargs={
            "max_new_tokens": 350,
            # "temperature": 0.9,
        })
    return generator