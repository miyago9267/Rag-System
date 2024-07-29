from haystack.document_stores.in_memory import InMemoryDocumentStore
from haystack import Document

def get_document_store():
    document_store = InMemoryDocumentStore()
    document_store.write_documents([
        Document(content="My name is Jean and I live in Paris."), 
        Document(content="My name is Mark and I live in Berlin."), 
        Document(content="My name is Giorgio and I live in Rome.")
    ])
    return document_store