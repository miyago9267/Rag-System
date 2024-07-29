from haystack.document_stores import InMemoryDocumentStore

def get_document_store():
    return InMemoryDocumentStore()