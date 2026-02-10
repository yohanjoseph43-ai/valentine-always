import streamlit as st
import time

# 1. Page Configuration
st.set_page_config(page_title="Project Love v2.0", page_icon="💖", layout="wide")

# 2. Symmetrical & Clean Styling (CSS)
st.markdown("""
    <style>
    /* Gradient Background */
    .stApp {
        background: linear-gradient(135deg, #ffafbd 0%, #ffc3a0 100%);
    }
    
    /* Center all main headers */
    .header-text {
        text-align: center;
        color: white;
        text-shadow: 2px 2px 8px rgba(0,0,0,0.2);
        font-family: 'Helvetica Neue', sans-serif;
    }

    /* Glassmorphism Card Style */
    .glass-card {
        background: rgba(255, 255, 255, 0.25);
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.1);
        backdrop-filter: blur(4px);
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.18);
        padding: 25px;
        margin-bottom: 20px;
        color: white;
    }
    
    /* Symmetrical button styling */
    div.stButton > button {
        width: 100%;
        border-radius: 25px;
        border: none;
        background-color: #ff4b4b;
        color: white;
        transition: 0.3s;
    }
    div.stButton > button:hover {
        background-color: #ff7575;
        transform: scale(1.02);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar Navigation (Keeps the main UI clean)
with st.sidebar:
    st.markdown("## 💌 Secret Menu")
    page = st.radio("Navigate:", ["The Proposal", "Why I Love You", "Love Analytics", "The Date Pass"])
    st.divider()
    st.write("Status: *Highly Encrypted Love*")

# --- PAGE 1: THE PROPOSAL ---
if page == "The Proposal":
    st.markdown("<h1 class='header-text'>Connection Request... ❤️</h1>", unsafe_allow_html=True)
    
    # Symmetrical layout for the question
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
            <div class='glass-card' style='text-align: center;'>
                <h3>System analysis complete.</h3>
                <p>One question remains for the User:</p>
                <h2>Will you be my Valentine?</h2>
