from sentence_transformers import SentenceTransformer

# Khởi tạo mô hình SentenceTransformer
# Tải từ Hugging Face: https://huggingface.co/thenlper/gte-large
embedding_model = SentenceTransformer("thenlper/gte-large")

def get_embedding(text: str) -> list[float]:
    """
    Tạo embedding từ đoạn văn bản.

    Args:
        text (str): Đoạn văn bản cần tạo embedding.

    Returns:
        list[float]: Vector embedding của đoạn văn bản.
    """
    if not text.strip():
        print("Attempted to get embedding for empty text.")
        return []

    # Encode văn bản thành vector
    embedding = embedding_model.encode(text)

    return embedding.tolist()
