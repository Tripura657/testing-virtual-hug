import streamlit as st

# Streamlit page setup
st.set_page_config(page_title="Virtual Hug 🤗", layout="centered")
st.title("🤗 Here's a virtual hug for you!")

# Show a comforting GIF
st.image("https://media.giphy.com/media/od5H3PmEG5EVq/giphy.gif", width=300)

# Display a kind message
st.markdown("""
You're doing great.  
Take a deep breath.  
Everything will be okay. 💙  
""")
