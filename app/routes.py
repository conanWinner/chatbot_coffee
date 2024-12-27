from flask import Blueprint, request, jsonify, current_app
from .service.model_service import start_chat_session, send_message
from .service.vector_search import get_search_result
from .service.embedding_service import get_embedding

bp = Blueprint("main", __name__)

# Initialize a chat session
chat_session = start_chat_session()

@bp.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the chatbot API!"})

@bp.route("/predict", methods=["POST"])
def search():
    data = request.get_json()
    user_query = data.get("query", "")

    if not user_query:        
        return jsonify({"error": "Query is required"}), 400

    # Lấy MongoDB collection từ ứng dụng
    client = current_app.mongo_client
    collection = client["disease_coffee"]["disease_collection"]

    # Thực hiện tìm kiếm vector
    # results = get_search_result(user_query, collection)

    # Đem qua model => Trả lời
    # combined_information = f"Query: {user_query} \n {results}."
    combined_information = user_query
    response = send_message(chat_session, combined_information)

    return jsonify({"results": response, "combined_information": combined_information})
