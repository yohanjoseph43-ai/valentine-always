import streamlit as st
import time

# 1. Page Configuration
st.set_page_config(page_title="Love.exe | Special Deployment", page_icon="💖", layout="centered")

# 2. Advanced Romantic Styling
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #ffafbd 0%, #ffc3a0 100%);
    }
    .reason-card {
        background-color: rgba(255, 255, 255, 0.85);
        padding: 20px;
        border-radius: 15px;
        border: 2px solid #ff4b4b;
        margin-bottom: 15px;
        color: #d32f2f;
        font-family: 'Helvetica', sans-serif;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    .header-text {
        text-align: center;
        color: white;
        font-family: 'Trebuchet MS', sans-serif;
        text-shadow: 2px 2px 8px rgba(0,0,0,0.3);
    }
    .ticket {
        background-color: #fff;
        border: 2px dashed #ff4b4b;
        padding: 20px;
        text-align: center;
        border-radius: 10px;
        color: #333;
    }
    </style>
    """, unsafe_allow_html=True)

# Initialize Session State
if 'page' not in st.session_state:
    st.session_state.page = "question"

# --- INTERACTIVE LOGIC ---

# PAGE 1: THE PROPOSAL
if st.session_state.page == "question":
    st.markdown("<h1 class='header-text'>Incoming Transmission... ❤️</h1>", unsafe_allow_html=True)
    st.write("### Someone is trying to reach you. Do you accept the connection?")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("YES! 😍", use_container_width=True):
            with st.spinner('Loading my heart...'):
                time.sleep(1.5)
            st.session_state.page = "main"
            st.rerun()
    with col2:
        if st.button("No 😢", use_container_width=True):
            st.toast("Error: Permission denied by your boyfriend's heart. Try again!", icon="🚫")

# PAGE 2: THE FULL EXPERIENCE
elif st.session_state.page == "main":
    st.balloons()
    st.markdown("<h1 class='header-text'>You're My Favorite Person!</h1>", unsafe_allow_html=True)
    
    # --- INTERACTIVE ELEMENT 1: TABS ---
    tab1, tab2, tab3 = st.tabs(["💌 Reasons Why", "📊 Love Meter", "🎟️ Your Ticket"])

    with tab1:
        st.write("### Why you are so special:")
        reasons = [
            "🌹 You have the kindest soul I've ever met.",
            "💻 You're the best part of my 'User Interface' every day.",
            "🌟 You make even the simplest moments feel like magic.",
            "🍕 You're my favorite person to do absolutely nothing with."
        ]
        for r in reasons:
            st.markdown(f"<div class='reason-card'>{r}</div>", unsafe_allow_html=True)

    with tab2:
        st.write("### How much do I love you today?")
        love_level = st.select_slider(
            "Slide to check the level:",
            options=["A lot", "To the moon", "To the next galaxy", "To the end of the universe", "More than Code"]
        )
        
        if love_level == "More than Code":
            st.error("WOW! That's a lot of love! ❤️🚀")
        else:
            st.write(f"Level: **{love_level}**")

    with tab3:
        st.write("### Admittance for One")
        st.markdown("""
            <div class="ticket">
                <h2>🎟️ VALENTINE'S DATE PASS</h2>
                <p><b>Valid for:</b> One Romantic Dinner & Zero Debugging</p>
                <p><b>Location:</b> Our Favorite Spot</p>
                <p><b>Expires:</b> Never</p>
            </div>
        """, unsafe_allow_html=True)
        
        if st.button("Claim Ticket"):
            st.snow()
            st.toast("Ticket Saved to your Heart!", icon="✅")

    # --- INTERACTIVE ELEMENT 2: SIDEBAR ---
    with st.sidebar:
        st.header("Surprise Settings")
        if st.checkbox("Send more hearts?"):
            st.toast("❤️ I love you!", icon="💖")
            st.toast("✨ You are amazing!", icon="💖")
            st.toast("🌹 Happy Valentine's!", icon="💖")
        
        st.write("---")
        st.write("Created with ❤️ by your favorite programmer.")

# --- FOOTER ---
if st.session_state.page == "main":
    if st.button("Click to Restart the Magic"):
        st.session_state.page = "question"
        st.rerun()
