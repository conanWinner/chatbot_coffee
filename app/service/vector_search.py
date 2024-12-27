from .embedding_service import get_embedding

def vector_search(user_query, collection):
    """Perform a vector search in the MongoDB collection."""
    query_embedding = get_embedding(user_query)
    if query_embedding is None:
        return "Invalid query or embedding generation failed."

    vector_search_stage = {
        "$vectorSearch": {
            "index": "vector_index",
            "queryVector": query_embedding,
            "path": "embedding",
            "numCandidates": 150,
            "limit": 1
        }
    }
    unset_stage = {"$unset": "embedding"}
    project_stage = {
        "$project": {
            "_id": 0,
            "thoitiet": 1,  # Thêm trường thoitiet vào project_stage
            "score": {"$meta": "vectorSearchScore"}
        }
    }
    pipeline = [vector_search_stage, unset_stage, project_stage]
    results = collection.aggregate(pipeline)
    return list(results)

def get_search_result(query, collection):

    get_knowledge = vector_search(query, collection)

    search_result = ""
    for result in get_knowledge:
        # print('---result', result)
        search_result += f"Title: {result.get('thoitiet', 'N/A')}, Plot: {result.get('noidung', 'N/A')}\n"

    return search_result