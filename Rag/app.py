from RagCore.pipeline import get_pipeline
from haystack.trainer import Trainer

pipeline = get_pipeline()

trainer = Trainer(
    retriever=pipeline.retriever,
    generator=pipeline.generator,
    document_store=pipeline.retriever.document_store,
    train_filename="train_data/train.json",
    dev_filename="train_data/dev.json"
)

trainer.train()