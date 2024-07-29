from haystack.nodes import DensePassageRetriever, RAGenerator

def get_retriever(document_store):
    return DensePassageRetriever(
        document_store=document_store,
        query_embedding_model="facebook/dpr-question_encoder-single-nq-base",
        passage_embedding_model="facebook/dpr-ctx_encoder-single-nq-base"
    )

def get_generator():
    return RAGenerator(
        model_name_or_path="facebook/rag-token-nq",
        use_gpu=True
    )