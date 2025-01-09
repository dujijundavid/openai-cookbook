# retrieval/search_engine.py
from retrieval.vectorizer import get_embedding
from data_management.database import get_session, Patent
import numpy as np
import faiss
import pickle

class SearchEngine:
    def __init__(self):
        self.session = get_session()
        self.index, self.patents = self.build_index()
    
    def build_index(self):
        patents = self.session.query(Patent).all()
        embeddings = []
        patent_ids = []
        for patent in patents:
            if patent.embedding:
                embedding = pickle.loads(patent.embedding.encode('latin1'))
                embeddings.append(embedding)
                patent_ids.append(patent.id)
        if not embeddings:
            embeddings = [get_embedding(f"{p.title}. {p.abstract}") for p in patents]
            for p, emb in zip(patents, embeddings):
                p.embedding = emb
                self.session.commit()
        embeddings = np.array(embeddings).astype('float32')
        dimension = len(embeddings[0])
        index = faiss.IndexFlatL2(dimension)
        index.add(embeddings)
        return index, patents
    
    def search(self, query, top_k=5):
        query_embedding = np.array([get_embedding(query)]).astype('float32')
        distances, indices = self.index.search(query_embedding, top_k)
        results = []
        for idx in indices[0]:
            if idx < len(self.patents):
                patent = self.patents[idx]
                results.append(patent)
        return results
