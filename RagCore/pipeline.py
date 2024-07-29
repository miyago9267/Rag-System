from haystack.pipelines import GenerativeQAPipeline
from .document_store import get_document_store
from .retriever_generator import get_retriever, get_generator

def get_pipeline():
    document_store = get_document_store()
    retriever = get_retriever(document_store)
    generator = get_generator()
    return GenerativeQAPipeline(generator=generator, retriever=retriever)