from haystack.components.retrievers.in_memory import InMemoryBM25Retriever
from haystack.components.generators import HuggingFaceLocalGenerator
from haystack.utils import ComponentDevice, Device, DeviceMap, Secret
import os

def get_retriever(document_store):
    document_store = document_store
    retriever = InMemoryBM25Retriever(
        document_store=document_store,
    )
    return retriever

def get_generator():
    generator = HuggingFaceLocalGenerator(
            model=os.getenv("LLM_MODEL"),
            token=Secret.from_token(os.getenv("HF_API_TOKEN")),
            generation_kwargs={
                "max_new_tokens": 150,
            }
        )
    return generator