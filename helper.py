from sentence_transformers import SentenceTransformer
from sentence_transformers import util
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

def cal_similarity(text1, text2):
    emb1 = model.encode(text1)
    emb2 = model.encode(text2)
    cos_sim = util.cos_sim(emb1, emb2)
    sim=str(cos_sim)
    sim=sim.strip("tensor([[]])")
    sim=float(sim)
    return sim