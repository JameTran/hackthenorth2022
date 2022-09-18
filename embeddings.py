import cohere
from numpy import dot
from numpy.linalg import norm

co = cohere.Client('kVZ1RsPpqi2y7lX5tVZJX8fcD7mtFKIDlteoo0GB')

def cos_sim(a, b):
    return dot(a, b)/(norm(a)*norm(b))

def semantic_similarity(text1, text2):
    embeds = co.embed(texts=[text1, text2])
    return cos_sim(embeds.embeddings[0], embeds.embeddings[1])