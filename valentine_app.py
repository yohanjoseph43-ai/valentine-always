import streamlit as st
import time

# 1. Page & Metadata Configuration
st.set_page_config(
    page_title="💖 Love.OS | v2.0", 
    page_icon="🌸", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Anime-Style Professional CSS
st.markdown("""
    <style>
    /* Professional Anime Font Stack */
    @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@400;600&family=Varela+Round&display=swap');

    html, body, [class*="css"] {
        font-family: 'Varela Round', 'Quicksand', sans-serif;
    }

    /* Dreamy Pastel Anime Background */
    .stApp {
        background: linear-gradient(180deg, #ffdde1 0%, #ee9ca7 100%);
        background-attachment: fixed;
    }

    /* Kawaii Glassmorphism Card */
    .glass-card {
        background: rgba(255, 255, 255, 0.4);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 2px solid rgba(255, 255, 255, 0.6);
        border-radius: 30px;
        padding: 40px;
        box-shadow: 0 10px 30px rgba(255, 182, 193, 0.4);
        color: #5d5d5d;
        margin-bottom: 30px;
        text-align: center;
    }
    
    /* Hover Animation */
    .glass-card:hover {
        transform: translateY(-5px);
        transition: 0.4s ease-in-out;
        background: rgba(255, 255, 255, 0.5);
    }

    /* Floating Anime Sparkle Animation */
    @keyframes float {
        0% { transform: translateY(0px) rotate(0deg); }
        50% { transform: translateY(-20px) rotate(5deg); }
        100% { transform: translateY(0px) rotate(0deg); }
    }
    .anime-icon {
        font-size: 80px;
        display: inline-block;
        animation: float 3s infinite ease-in-out;
    }

    /* Rounded Professional Buttons */
    div.stButton > button {
        border-radius: 30px;
        height: 3.5em;
        background: linear-gradient(90deg, #ff758c 0%, #ff7eb3 100%);
        color: white;
        border: none;
        font-weight: 600;
        letter-spacing: 1px;
        box-shadow: 0 4px 15px rgba(255, 117, 140, 0.4);
        transition: 0.3s;
    }
    div.stButton > button:hover {
        background: linear-gradient(90deg, #ff7eb3 0%, #ff758c 100%);
        transform: scale(1.05);
    }

    /* Clean Sidebar */
    [data-testid="stSidebar"] {
        background-color: rgba(255, 255, 255, 0.2);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar Navigation (Anime Theme)
with st.sidebar:
    st.markdown("## 🌸 User Menu")
    page = st.radio("Access Level:", ["Terminal: Start", "Memory: Gallery", "Audio: Tracks", "Status: Heart Rate"])
    st.divider()
    st.caption("Environment: Dreamy-Vibes-v2")
    st.caption("Developed with ✨ and Code")

# --- PAGE 1: TERMINAL: START (PROPOSAL) ---
if page == "Terminal: Start":
    st.write("##")
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("<div style='text-align:center;'><span class='anime-icon'>🌸</span></div>", unsafe_allow_html=True)
        st.markdown("""
            <div class='glass-card'>
                <h1 style='color: #ff5e78;'>// INITIALIZING_HEART_LINK</h1>
                <p style='color: #7a7a7a; font-size: 1.1rem;'>
                    Connection quality: <b>Perfect</b><br>
                    Encryption: <b>True Love</b>
                </p>
                <hr style='border: 0.5px solid rgba(255,255,255,0.5); margin: 30px 0;'>
                <h2 style='color: #ff5e78; font-family: "Varela Round";'>Will you be my Valentine?</h2>
            </div>
        """, unsafe_allow_html=True)
        
        c1, c2 = st.columns(2)
        with c1:
            if st.button("CONFIRM (YES)"):
                st.balloons()
                st.toast("Access Granted! ✨", icon="🌸")
        with c2:
            if st.button("DENY (NO)"):
                st.toast("Error: Redirecting to 'YES'...", icon="🎀")

# --- PAGE 2: MEMORY: GALLERY (WHY I LOVE YOU) ---
elif page == "Memory: Gallery":
    st.markdown("<h1 style='text-align:center; color:white;'>💌 Captured Memories</h1>", unsafe_allow_html=True)
    reasons = [
        ("✨ The Spark", "You have this magical way of making me smile without saying a word."),
        ("💻 My Support", "You are the 'Admin' of my heart and my biggest motivation."),
        ("🌙 Dreamer", "Every conversation with you feels like a beautiful anime scene."),
        ("🍙 Simple Joys", "I'm happiest just doing life's simple side-quests with you.")
    ]
    c_l, c_r = st.columns(2)
    for i, (title, body) in enumerate(reasons):
        target = c_l if i % 2 == 0 else c_r
        with target:
            st.markdown(f"""
                <div class='glass-card' style='text-align: left;'>
                    <h3 style='color: #ff5e78; margin-top:0;'>{title}</h3>
                    <p style='color: #666;'>{body}</p>
                </div>
            """, unsafe_allow_html=True)

# --- PAGE 3: AUDIO: TRACKS (SOUNDTRACK) ---
elif page == "Audio: Tracks":
    st.markdown("<h1 style='text-align:center; color:white;'>🎶 Heart's OST</h1>", unsafe_allow_html=True)
    songs = [
        {"title": "Arz Kiya Hai", "artist": "Anuv Jain", "note": "Our story in a melody."},
        {"title": "I think they call this love", "artist": "Matthew Ifield", "note": "The perfect theme song for us."},
        {"title": "Perfect", "artist": "Ed Sheeran", "note": "Classic, just like my love for you."},
        {"title": "A Thousand Years", "artist": "Christina Perri", "note": "An eternal loop of affection."}
    ]
    c_l, c_r = st.columns(2)
    for i, song in enumerate(songs):
        target = c_l if i % 2 == 0 else c_r
        with target:
            st.markdown(f"""
                <div class='glass-card'>
                    <h4 style='color: #ff5e78;'>🎵 {song['title']}</h4>
                    <p style='color: #888; font-size: 0.9em;'>{song['artist']}</p>
                    <p style='font-size:0.8em; color: #aaa;'>{song['note']}</p>
                </div>
            """, unsafe_allow_html=True)

# --- PAGE 4: STATUS: HEART RATE (ANALYTICS) ---
elif page == "Status: Heart Rate":
    st.markdown("<h1 style='text-align:center; color:white;'>📊 Connection Stats</h1>", unsafe_allow_html=True)
    m1, m2, m3 = st.columns(3)
    m1.metric("Love Stats", "Infinite", "LVL UP")
    m2.metric("Sync Rate", "100%", "Synched")
    m3.metric("Happiness", "MAX", "✨")
    
    st.markdown("<div class='glass-card'><h3>💖 Synchronize Feelings</h3>", unsafe_allow_html=True)
    val = st.select_slider("", options=["Low", "Medium", "High", "Universe", "Destiny"])
    if val == "Destiny":
        st.snow()
        st.write("### 🌸 **STATUS: PURE HAPPINESS** 🌸")
    st.markdown("</div>", unsafe_allow_html=True)
