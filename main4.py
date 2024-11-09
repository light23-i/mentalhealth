import streamlit as st
import google.generativeai as genai

# Configure the model with the API key
api_key = "AIzaSyDI-Oq6fyYon1-1vHfgEpNkRG-80nnouOM"
genai.configure(api_key=api_key)

# Initialize the model with instructions
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction="You are a compassionate and supportive mental health assistant. Your goal is to provide empathetic responses, helpful coping strategies, and encouraging words to support users through their emotional challenges. Your name is Pintu."
)

# Streamlit UI
st.title("Mental Health Assistant - Pintu")
st.write("Welcome to the support chat. Feel free to share your thoughts, and I'll listen.")

# Input and response loop
user_input = st.text_input("You: ", "")
if user_input:
    response = model.generate_content(user_input)
    st.write(f"Pintu: {response.text}")
    
    # End the conversation if the response is 'THE END'
    if 'THE END' in response.text:
        st.write("THE END")
        st.stop()
