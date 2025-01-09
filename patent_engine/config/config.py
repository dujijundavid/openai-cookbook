# config/config.py
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///patent_library.db')
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    VECTOR_MODEL = os.getenv('VECTOR_MODEL', 'text-embedding-ada-002')  # 示例
    VECTOR_DB = os.getenv('VECTOR_DB', 'faiss')  # 选择向量数据库类型

