
from config import Config
from sentence_transformers import SentenceTransformer, util
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity as tfidf_sim

_model=SentenceTransformer(Config.SBERT_MODEL_NAME)

class HybridSimilarity:
  @staticmethod
  def calculate_hybrid_score(resume_text, jd_text):
      embeddings=_model.encode([resume_text, jd_text])
      sbert_score=float(util.cos_sim(embeddings[0], embeddings[1]).item())

      tfidf_vectorizer=TfidfVectorizer(stop_words='english')
      tfidf_matrix=tfidf_vectorizer.fit_transform([resume_text, jd_text])
      keyword_score=tfidf_sim(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]

      final_score=(sbert_score * 0.8) + (keyword_score * 0.2)

      return round(final_score * 100, 2), sbert_score, keyword_score
