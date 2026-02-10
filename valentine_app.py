import streamlit as st
import time

# 1. Page Configuration
st.set_page_config(page_title="Project Love v2.0", page_icon="💖", layout="wide")

# 2. Symmetrical & Clean Styling (CSS)
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #ffafbd 0%, #ffc3a0 100%);
    }
    .header-text {
        text-align: center;
        color: white;
        text-shadow: 2px 2px 8px rgba(0,0,0,0.2);
        font-family: 'Helvetica Neue', sans-serif;
    }
    .glass-card {
        background: rgba(255, 255, 255, 0.25);
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.1);
        backdrop-filter: blur(4px);
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.18);
        padding: 30px;
        margin-bottom: 25px;
        color: white;
        text-align: center;
        min-height: 220px; /* Symmetrical box heights */
    }
    div.stButton > button {
        width: 100%;
        border-radius: 25px;
        border: none;
        background-color: #ff4b4b;
        color: white;
        font-weight: bold;
        transition: 0.3s;
    }
    div.stButton > button:hover {
        background-color: #ff7575;
        transform: scale(1.03);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar Navigation
with st.sidebar:
    st.markdown("## 💌 Menu")
    page = st.radio("Navigate:", ["The Proposal", "Why I Love You", "Our Soundtrack", "Love Analytics"])
    st.divider()
    st.write("Status: *Highly Encrypted Love*")

# --- PAGE 1: THE PROPOSAL ---
if page == "The Proposal":
    st.markdown("<h1 class='header-text'>Incoming Request... ❤️</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
            <div class='glass-card'>
                <h3>System analysis complete.</h3>
                <p style='font-size: 1.2em;'>One question remains for the User:</p>
                <h2 style='font-size: 2.5em;'>Will you be my Valentine?</h2>
            </div>
        """, unsafe_allow_html=True)
        btn_col1, btn_col2 = st.columns(2)
        with btn_col1:
            if st.button("YES! 😍"):
                st.balloons()
                st.toast("Access Granted!", icon="❤️")
        with btn_col2:
            if st.button("No 😢"):
                st.toast("Error 404: Option Not Found", icon="🚫")

# --- PAGE 2: WHY I LOVE YOU ---
elif page == "Why I Love You":
    st.markdown("<h1 class='header-text'>💌 Why You?</h1>", unsafe_allow_html=True)
    reasons = [
        ("🌟 Your Kindness", "You have the kindest soul I've ever met."),
        ("💻 Your Support", "You are the best 'User Interface' of my life."),
        ("✨ Your Magic", "You turn ordinary days into beautiful memories."),
        ("🍕 Your Presence", "You're my favorite person to do absolutely nothing with.")
    ]
    col_left, col_right = st.columns(2)
    for i, (title, body) in enumerate(reasons):
        target_col = col_left if i % 2 == 0 else col_right
        with target_col:
            st.markdown(f"<div class='glass-card' style='text-align: left;'><h3 style='margin-top:0; color: #ffefef;'>{title}</h3><p style='font-size: 1.1em;'>{body}</p></div>", unsafe_allow_html=True)

# --- PAGE 3: OUR SOUNDTRACK ---
elif page == "Our Soundtrack":
    st.markdown("<h1 class='header-text'>🎶 Songs That Remind Me of You</h1>", unsafe_allow_html=True)
    
    songs = [
        {"title": "Arz Kiya Hai", "artist": "Anuv Jain", "note": "Because you're the poetry I always wanted to write."},
        {"title": "I Think They Call This Love", "artist": "Elliot James Reay", "note": "That old-school feeling I get whenever I'm with you."},
        {"title": "Perfect", "artist": "Ed Sheeran", "note": "Because you are, in every single way."},
        {"title": "A Thousand Years", "artist": "Christina Perri", "note": "I've loved you for a thousand more."}
    ]

    col_l, col_r = st.columns(2)
    for i, song in enumerate(songs):
        target_col = col_l if i % 2 == 0 else col_r
        with target_col:
            st.markdown(f"""
                <div class='glass-card'>
                    <h4 style='margin:0; color: #ffefef;'>🎵 {song['title']}</h4>
                    <p style='font-style: italic;'>{song['artist']}</p>
                    <hr style='border: 0.5px solid rgba(255,255,255,0.2);'>
                    <p style='font-size: 0.9em;'>"{song['note']}"</p>
                </div>
            """, unsafe_allow_html=True)

# --- PAGE 4: LOVE ANALYTICS ---
elif page == "Love Analytics":
    st.markdown("<h1 class='header-text'>📊 The Data of Us</h1>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    c1.metric("Current Love Level", "Infinite", "↑ 100%")
    c2.metric("Patience Level", "Legendary", "Max")
    c3.metric("Happiness Index", "9999+", "🚀")
    
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.write("### Interactive Love Gauge")
    love_slider = st.select_slider("", options=["A lot", "To the moon", "To the galaxy", "Infinite Loop"])
    if love_slider == "Infinite Loop":
        st.snow()
        st.write("### ❤️ **CRITICAL ERROR: LOVE OVERFLOW!** ❤️")
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: white; opacity: 0.7;'>Built with ❤️ by your favorite programmer</p>", unsafe_allow_html=True)
