import streamlit as st
import time

# 1. Page & Metadata Configuration
st.set_page_config(
    page_title="Project Love v2.0 | Deployment", 
    page_icon="💖", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Professional CSS (UI/UX Engineering)
st.markdown("""
    <style>
    /* Importing a clean, professional font */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    /* Background Gradient */
    .stApp {
        background: linear-gradient(145deg, #ff9a9e 0%, #fad0c4 99%, #fad0c4 100%);
    }

    /* Professional Glassmorphism Card */
    .glass-card {
        background: rgba(255, 255, 255, 0.2);
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        border: 1px solid rgba(255, 255, 255, 0.3);
        border-radius: 24px;
        padding: 40px;
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
        color: #4a4a4a;
        margin-bottom: 30px;
        transition: transform 0.3s ease;
    }
    
    .glass-card:hover {
        transform: translateY(-5px);
    }

    /* Pulsing Heart for Landing Page */
    @keyframes pulse {
        0% { transform: scale(1); opacity: 0.9; }
        50% { transform: scale(1.05); opacity: 1; }
        100% { transform: scale(1); opacity: 0.9; }
    }
    .heart-icon {
        font-size: 100px;
        text-align: center;
        animation: pulse 2s infinite ease-in-out;
        margin-bottom: 20px;
    }

    /* Clean Button Styling */
    div.stButton > button {
        border-radius: 12px;
        height: 3.5em;
        background-color: #ff4b4b;
        color: white;
        border: none;
        font-weight: 600;
        letter-spacing: 0.5px;
        box-shadow: 0 4px 15px rgba(255, 75, 75, 0.3);
        transition: all 0.3s ease;
    }
    div.stButton > button:hover {
        background-color: #e63939;
        box-shadow: 0 6px 20px rgba(255, 75, 75, 0.4);
    }

    /* Sidebar Refinement */
    [data-testid="stSidebar"] {
        background-color: rgba(255, 255, 255, 0.1);
        border-right: 1px solid rgba(255, 255, 255, 0.2);
    }

    /* Title Styling */
    .header-text {
        text-align: center;
        color: #ffffff;
        font-weight: 600;
        text-shadow: 0 4px 10px rgba(0,0,0,0.1);
        margin-bottom: 40px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar Navigation
with st.sidebar:
    st.markdown("### 🛠️ Core Modules")
    page = st.radio("Navigation", ["Initialization", "Visual Assets", "Audio Logs", "System Analytics"])
    st.divider()
    st.caption("Version 2.0.4 | Stable Build")
    st.caption("Created with ❤️ by your Developer")

# --- PAGE 1: INITIALIZATION (PROPOSAL) ---
if page == "Initialization":
    st.write("##")
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("<div class='heart-icon'>❤️</div>", unsafe_allow_html=True)
        st.markdown("""
            <div class='glass-card'>
                <h1 style='color: white; font-size: 2.2rem;'>// REQUESTING CONNECTION</h1>
                <p style='color: #616161; font-size: 1.1rem; margin-top: 15px;'>
                    A secure link has been established. 
                    Validation requires one final confirmation.
                </p>
                <hr style='border: 0.5px solid rgba(255,255,255,0.3); margin: 30px 0;'>
                <h2 style='color: #d32f2f; font-size: 1.8rem;'>Will you be my Valentine?</h2>
            </div>
        """, unsafe_allow_html=True)
        
        c1, c2 = st.columns(2)
        with c1:
            if st.button("ACCEPT", use_container_width=True):
                st.balloons()
                st.toast("Success: Connection Stabilized.", icon="💖")
        with c2:
            if st.button("REJECT", use_container_width=True):
                st.toast("Warning: Permission Denied. System override in effect.", icon="🚫")

# --- PAGE 2: VISUAL ASSETS (WHY I LOVE YOU) ---
elif page == "Visual Assets":
    st.markdown("<h1 class='header-text'>💌 Why You?</h1>", unsafe_allow_html=True)
    reasons = [
        ("🌟 Your Kindness", "Your empathy and heart are the foundation of everything we build together."),
        ("💻 Your Support", "You are the most reliable partner, both in life and in my projects."),
        ("✨ Your Magic", "You bring a spark to every ordinary day that I can't explain."),
        ("🍕 Your Presence", "Simply being near you is the best part of my daily routine.")
    ]
    c_l, c_r = st.columns(2)
    for i, (title, body) in enumerate(reasons):
        target = c_l if i % 2 == 0 else c_r
        with target:
            st.markdown(f"<div class='glass-card' style='text-align: left;'><h3 style='color: #d32f2f;'>{title}</h3><p style='color: #4f4f4f;'>{body}</p></div>", unsafe_allow_html=True)

# --- PAGE 3: AUDIO LOGS (SOUNDTRACK) ---
elif page == "Audio Logs":
    st.markdown("<h1 class='header-text'>🎶 Our Soundtrack</h1>", unsafe_allow_html=True)
    songs = [
        {"title": "Arz Kiya Hai", "artist": "Anuv Jain", "note": "The poetry that reminds me of our story."},
        {"title": "I think they call this love", "artist": "Matthew Ifield", "note": "A track that captures our exact frequency."},
        {"title": "Perfect", "artist": "Ed Sheeran", "note": "A timeless classic for a perfect person."},
        {"title": "A Thousand Years", "artist": "Christina Perri", "note": "A promise that scales beyond time."}
    ]
    c_l, c_r = st.columns(2)
    for i, song in enumerate(songs):
        target = c_l if i % 2 == 0 else c_r
        with target:
            st.markdown(f"<div class='glass-card'><h4>🎵 {song['title']}</h4><p style='color: #616161;'>{song['artist']}</p><p style='font-size:0.85em; color: #888;'><i>{song['note']}</i></p></div>", unsafe_allow_html=True)

# --- PAGE 4: SYSTEM ANALYTICS ---
elif page == "System Analytics":
    st.markdown("<h1 class='header-text'>📊 Love Analytics</h1>", unsafe_allow_html=True)
    m1, m2, m3 = st.columns(3)
    m1.metric("Love Level", "Infinite", "↑ 100%")
    m2.metric("System Uptime", "365 Days", "Online")
    m3.metric("Happiness Index", "9999+", "🚀")
    
    st.markdown("<div class='glass-card'><h3>Interactive Love Gauge</h3>", unsafe_allow_html=True)
    val = st.select_slider("", options=["Low", "Medium", "High", "To the Moon", "Infinite"])
    if val == "Infinite":
        st.snow()
        st.write("### ⚠️ **STATUS: OVERFLOW ERROR**")
    st.markdown("</div>", unsafe_allow_html=True)
