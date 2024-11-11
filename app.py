# app.py
import streamlit as st
import json

# Load responses from JSON files
def load_responses():
    with open('responses_en.json', 'r', encoding='utf-8') as f:
        en_responses = json.load(f)
    with open('responses_fr.json', 'r', encoding='utf-8') as f:
        fr_responses = json.load(f)
    with open('responses_ar.json', 'r', encoding='utf-8') as f:
        ar_responses = json.load(f)
    return en_responses, fr_responses, ar_responses

# Custom CSS for purple and blue theme
def set_custom_theme():
    st.markdown("""
        <style>
        .stApp {
            background: linear-gradient(135deg, #6B46C1 0%, #3182CE 100%);
        }
        .stTextInput {
            background-color: rgba(255, 255, 255, 0.1);
        }
        .stButton button {
            background-color: #805AD5;
            color: white;
        }
        .chat-message {
            padding: 1rem;
            border-radius: 0.5rem;
            margin: 1rem 0;
            background-color: rgba(255, 255, 255, 0.1);
        }
        </style>
    """, unsafe_allow_html=True)

def get_response(query, responses):
    # Simple keyword matching
    query = query.lower()
    for key, value in responses.items():
        if any(keyword in query for keyword in key.split("|")):
            return value
    return responses["default"]

def main():
    set_custom_theme()
    
    st.title("FST Tanger - Mechanical Engineering Chatbot")
    
    # Language selector
    language = st.selectbox(
        "Select Language / Choisir la langue / اختر اللغة",
        ["English", "Français", "العربية"]
    )
    
    # Load responses
    en_responses, fr_responses, ar_responses = load_responses()
    
    # Set responses based on language
    if language == "English":
        responses = en_responses
        placeholder = "Ask your question about mechanical engineering..."
    elif language == "Français":
        responses = fr_responses
        placeholder = "Posez votre question sur le génie mécanique..."
    else:
        responses = ar_responses
        placeholder = "...اطرح سؤالك حول الهندسة الميكانيكية"
    
    # Chat interface
    st.write("---")
    
    # Display greeting based on language
    st.markdown(f"<div class='chat-message'>{responses['greeting']}</div>", unsafe_allow_html=True)
    
    # User input
    user_question = st.text_input("", placeholder=placeholder)
    
    if user_question:
        response = get_response(user_question, responses)
        st.markdown(f"<div class='chat-message'>{response}</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
