import fitz
import os
from haystack.document_stores.in_memory import InMemoryDocumentStore
from haystack import Document

def pdf_to_text(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page_num in range(doc.page_count):
        page = doc.load_page(page_num)
        text += page.get_text()
    return text

def get_document_store(pdf_paths):
    document_store = InMemoryDocumentStore()

    documents = [
        Document(content="Rome is the capital of Italy"),
        Document(content="Paris is the capital of France"),
        Document(content="Tokyo is the capital of Japan")
    ]
    
    # for f in os.listdir(pdf_paths):
    #     if f.endswith(".pdf"):
    #         pdf_path = os.path.join(pdf_paths, f)
    #         text = pdf_to_text(pdf_path)
    #         documents.append(Document(content=text))

    document_store.write_documents(documents)
    return document_store