from sentence_transformers import SentenceTransformer, util
model = SentenceTransformer('all-MiniLM-L6-v2')

def calculate_file_name_similarity(file_names):
	embeddings = model.encode(file_names, convert_to_tensor=True)
	return util.cos_sim(embeddings, embeddings).cpu().numpy()