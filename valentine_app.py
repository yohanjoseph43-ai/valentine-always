import streamlit as st
import time

# 1. Page & Metadata Configuration
st.set_page_config(
    page_title="Love.OS | v2.0 Deployment", 
    page_icon="🥋", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Professional Anime-Tech Styling (CSS)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@400;600&family=Varela+Round&display=swap');
    
    html, body, [class*="css"] { 
        font-family: 'Varela Round', sans-serif; 
    }
    
    .stApp {
        background: linear-gradient(180deg, #ffdde1 0%, #ee9ca7 100%);
        background-attachment: fixed;
    }

    /* Glassmorphism Card Design */
    .glass-card {
        background: rgba(255, 255, 255, 0.4);
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        border: 2px solid rgba(255, 255, 255, 0.6);
        border-radius: 30px;
        padding: 35px;
        box-shadow: 0 10px 30px rgba(255, 182, 193, 0.4);
        color: #5d5d5d;
        text-align: center;
        margin-bottom: 20px;
        transition: transform 0.3s ease;
    }

    .glass-card:hover {
        transform: translateY(-5px);
    }

    /* Anime Floating Animation */
    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-15px); }
        100% { transform: translateY(0px); }
    }
    .anime-icon { 
        font-size: 80px; 
        display: block; 
        margin: 0 auto; 
        animation: float 3s infinite ease-in-out; 
    }

    /* Custom Progress Bar Color */
    .stProgress > div > div > div > div {
        background-image: linear-gradient(to right, #ff758c , #ff7eb3);
    }

    /* Styled Buttons */
    div.stButton > button {
        border-radius: 30px;
        height: 3.8em;
        background: linear-gradient(90deg, #ff758c 0%, #ff7eb3 100%);
        color: white;
        border: none;
        font-weight: 600;
        width: 100%;
        box-shadow: 0 4px 15px rgba(255, 117, 140, 0.4);
        transition: 0.3s ease;
    }

    /* Song Link Styling */
    .song-card {
        text-decoration: none;
        color: inherit;
        display: block;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. State Management Logic
if 'step' not in st.session_state:
    st.session_state.step = "security"
if 'strikes' not in st.session_state:
    st.session_state.strikes = 0

def move_to(step_name):
    st.session_state.step = step_name
    st.rerun()

# --- TOP NAVIGATION / PROGRESS ---
if st.session_state.step != "security":
    steps_list = ["proposal", "karate", "memories", "soundtrack", "date", "finale"]
    try:
        current_idx = steps_list.index(st.session_state.step)
        st.progress((current_idx + 1) / len(steps_list))
    except ValueError:
        pass

# --- STEP 1: SECURITY GATE ---
if st.session_state.step == "security":
    st.write("##")
    col1, col2, col3 = st.columns([1, 1.5, 1])
    with col2:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.write("🔒 **SECURE SERVER ACCESS**")
        st.write("To proceed, enter the city where we first met.")
        password = st.text_input("Answer:", type="default", placeholder="Type here...")
        if st.button("Unlock Module"):
            # CURRENTLY SET TO KOCHI BASED ON YOUR CONTEXT
            if password.lower() == "kochi
