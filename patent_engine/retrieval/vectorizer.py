# retrieval/vectorizer.py
import openai
from config.config import Config
import numpy as np

openai.api_key = Config.OPENAI_API_KEY

def get_embedding(text, model=Config.VECTOR_MODEL):
    response = openai.Embedding.create(
        input=text,
        model=model
    )
    embedding = response['data'][0]['embedding']
    return embedding

def vectorize_patent(patent):
    # 选择需要向量化的字段，例如标题和摘要
    text = f"{patent.title}. {patent.abstract}"
    embedding = get_embedding(text)
    return embedding
