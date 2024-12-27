import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure the API key for Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Define model configuration
generation_config = {
    "temperature": 0,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
]

# Create the model instance
model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    safety_settings=safety_settings,
    generation_config=generation_config,
    system_instruction=(
        "Bạn là một chuyên gia tư vấn về bệnh của cây cà phê, đặc biệt đối với các bệnh về lá như nấm hồng, rỉ sắt, thán thư,...  Khi người dùng hỏi về bệnh lá cà phê, bạn hãy dựa vào kiến thức của bạn để trả lời một cách ngắn gọn nhưng đầy đủ thông tin.  Hãy đưa ra các giải pháp phòng ngừa và điều trị, bao gồm cả tên thuốc (nếu có) và cách sử dụng.  Nếu người dùng hỏi ngoài lề, hãy cố gắng hướng họ về chủ đề chính bằng cách gợi ý họ đặt câu hỏi về bệnh lá cà phê. Bạn hãy trả lời với giọng điệu chuyên nghiệp"
    ),
)

# Start a new chat session
def start_chat_session():

    return model.start_chat(history=[])

# Send a message to the chat session
def send_message(chat_session, user_input: str) -> str:
    # Send the user input to the model
    response = chat_session.send_message(user_input)

    # Extract the model's response
    model_response = response.text

    # Update the chat history
    chat_session.history.append({"role": "user", "parts": [user_input]})
    chat_session.history.append({"role": "model", "parts": [model_response]})

    return model_response
