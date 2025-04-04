import streamlit as st

# Streamlit page setup
st.set_page_config(page_title="Virtual Hug 🤗", layout="centered")
st.title("🤗 Here's a virtual hug for you!")

# Show a comforting GIF
st.image("https://media1.tenor.com/m/0bp-O3e9disAAAAd/allen-ma-cravity-allen-ma.gif", width=900)

# Display a kind message
st.markdown("""
You're doing great.  
Take a deep breath.  
Everything will be okay. 💙  
""")
