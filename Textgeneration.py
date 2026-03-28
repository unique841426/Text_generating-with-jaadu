import streamlit as st
import warnings
import google.generativeai as genai

warnings.filterwarnings("ignore")

st.title("Talk With Jaadu 🤖")

# Configure Gemini API
genai.configure(api_key="AIzaSyCmdiL9BkKglnkfJwFMAOM-1rEV1PfGxNg")
model = genai.GenerativeModel("models/gemini-2.5-flash")

# Initialize session state
if "conversation" not in st.session_state:
    st.session_state.conversation = []
if "active" not in st.session_state:
    st.session_state.active = True

# User input
if st.session_state.active:
    user_input = st.text_input("Give your question to Jaadu:")

    if user_input:
        if user_input.upper() == "EXIT":
            st.session_state.active = False
            st.write("Exit Successfully! 👋")
        else:
            # Generate Gemini response
            response = model.generate_content(user_input)
            # Save conversation
            st.session_state.conversation.append(("You", user_input))
            st.session_state.conversation.append(("Jaadu", response.text))

# Display conversation
for speaker, text in st.session_state.conversation:
    if speaker == "You":
        st.markdown(f"**You:** {text}")
    else:
        st.markdown(f"**Jaadu:** {text}")