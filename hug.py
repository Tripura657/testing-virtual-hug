import streamlit as st

# Page config
st.set_page_config(page_title="Virtual Hug 🤗", layout="wide")

# Center-align using columns
st.markdown("<h1 style='text-align: center;'>🤗 Here's a virtual hug for you!</h1>", unsafe_allow_html=True)

# Full-width layout using columns
left, center, right = st.columns([1, 3, 1])

with center:
    st.video("https://media1.tenor.com/m/0bp-O3e9disAAAAd/allen-ma-cravity-allen-ma.gif")

# Heartwarming message centered
st.markdown("""
<div style='text-align: center; font-size: 20px; padding-top: 20px;'>
You're doing great.<br>
Take a deep breath.<br>
Everything will be okay. 💙
</div>
""", unsafe_allow_html=True)
