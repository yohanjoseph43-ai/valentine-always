import streamlit as st
import time

# 1. Page Configuration
st.set_page_config(page_title="Love.OS | Fixed Edition", page_icon="🥋", layout="wide")

# 2. Force-Applied Styling (CSS)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@400;600&family=Varela+Round&display=swap');
    
    .stApp {
        background: linear-gradient(180deg, #ffdde1 0%, #ee9ca7 100%);
        background-attachment: fixed;
    }

    /* THE GLASS CARD */
    .glass-card {
        background: rgba(255, 255, 255, 0.4);
        backdrop-filter: blur(15px);
        border: 2px solid rgba(255, 255, 255, 0.6);
        border-radius: 30px;
        padding: 40px;
        box-shadow: 0 10px 30px rgba(255, 182, 193, 0.4);
        color: #5d5d5d;
        text-align: center;
    }

    /* REASON HEADERS */
    .reason-header { color: #ff5e78; font-size: 1.8rem; font-weight: 700; margin-top: 20px; }
    .reason-text { font-size: 1.1rem; color: #555; margin-bottom: 25px; }

    /* THE HYPER-PANIC ANIMATION */
    @keyframes hyper-panic {
        0% { transform: translate(0, 0) rotate(0deg); }
        10% { transform: translate(-50px, -30px) rotate(-10deg); }
        20% { transform: translate(50px, 30px) rotate(10deg); }
        30% { transform: translate(-60px, 40px) rotate(-5deg); }
        40% { transform: translate(60px, -40px) rotate(5deg); }
        50% { transform: translate(-70px, 20px) rotate(-10deg); }
        100% { transform: translate(0, 0) rotate(0deg); }
    }

    /* SELECTOR OVERRIDE: Targets the button that says 'No' specifically */
    button[kind="secondary"], button:contains("No") {
        transition: none !important;
    }

    /* We target the div containing the button to make the whole thing jump */
    div.stButton > button:has(div:contains("No")) {
        animation: hyper-panic 0.1s infinite !important;
        background: #ccc !important; /* Makes it look 'glitched' */
        color: #666 !important;
    }

    /* THE SWARM */
    @keyframes swarm {
        0% { transform: translateY(110vh) scale(0.5); opacity: 0; }
        10% { opacity: 1; }
        100% { transform: translateY(-20vh) translateX(100px) rotate(360deg) scale(2.5); opacity: 0; }
    }
    .butterfly {
        position: fixed; bottom: -100px; font-size: 45px;
        z-index: 9999; animation: swarm var(--duration) infinite linear;
        left: var(--left); animation-delay: var(--delay);
    }

    div.stButton > button {
        border-radius: 30px; height: 3.5em; font-weight: 600; width: 100%;
        background: linear-gradient(90deg, #ff758c 0%, #ff7eb3 100%);
        color: white; border: none;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. State Management
if 'step' not in st.session_state: st.session_state.step = "security"
if 'strikes' not in st.session_state: st.session_state.strikes = 0

def move_to(step_name):
    st.session_state.step = step_name
    st.rerun()

# --- STEP 1: SECURITY ---
if st.session_state.step == "security":
    col1, col2, col3 = st.columns([1, 1.5, 1])
    with col2:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.write("🔒 **ENCRYPTED FILE: OPEN_HEART.EXE**")
        pw = st.text_input("Secret Key (City?):")
        if st.button("Decrypt"):
            if pw.lower() == "kochi": move_to("proposal")
            else: st.error("Access Denied.")
        st.markdown("</div>", unsafe_allow_html=True)

# --- STEP 2: PROPOSAL (The 'Jump' Logic) ---
elif st.session_state.step == "proposal":
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<div class='glass-card'><span style='font-size:70px;'>🌸</span>", unsafe_allow_html=True)
        st.write("## Will you be my Valentine?")
        c1, c2 = st.columns(2)
        with c1:
            if st.button("YES! 😍"): st.balloons(); move_to("karate")
        with c2:
            # The CSS targets any button with "No" in it.
            if st.button("No 😢"):
                st.toast("How did you even click that?!")
        st.markdown("</div>", unsafe_allow_html=True)

# --- STEP 3: KARATE ---
elif st.session_state.step == "karate":
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<div class='glass-card'>🥋 **STRIKE 10 TIMES**", unsafe_allow_html=True)
        st.progress(st.session_state.strikes / 10)
        if st.button("PUNCH! 👊"):
            st.session_state.strikes += 1
            if st.session_state.strikes >= 10: move_to("memories")
            else: st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

# --- STEP 4: MEMORIES ---
elif st.session_state.step == "memories":
    col1, col2, col3 = st.columns([1, 4, 1])
    with col2:
        st.markdown("<div class='glass-card'>### 📸 Memories", unsafe_allow_html=True)
        # Add your image paths here
        st.image("https://via.placeholder.com/400") 
        if st.button("Next ➡️"): move_to("reasons")
        st.markdown("</div>", unsafe_allow_html=True)

# --- STEP 5: REASONS (Headers) ---
elif st.session_state.step == "reasons":
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.markdown("<div class='reason-header'>✨ Your Smile</div><div class='reason-text'>It brightens my darkest days.</div>", unsafe_allow_html=True)
        st.markdown("<div class='reason-header'>🥋 Your Strength</div><div class='reason-text'>The way you never give up.</div>", unsafe_allow_html=True)
        if st.button("Next ➡️"): move_to("soundtrack")
        st.markdown("</div>", unsafe_allow_html=True)

# --- STEP 6: SOUNDTRACK ---
elif st.session_state.step == "soundtrack":
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<div class='glass-card'>### 🎶 Soundtrack", unsafe_allow_html=True)
        st.write("[Song Link](https://music.youtube.com/watch?v=-BJt4fCAtZE)")
        if st.button("Read Letter ➡️"): move_to("letter")
        st.markdown("</div>", unsafe_allow_html=True)

# --- STEP 7: LETTER ---
elif st.session_state.step == "letter":
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.write("My Dearest, I love you. OSS!")
        if st.button("Final Step ➡️"): move_to("finale")
        st.markdown("</div>", unsafe_allow_html=True)

# --- STEP 8: FINALE ---
elif st.session_state.step == "finale":
    swarm = ""
    for i in range(40):
        swarm += f'<div class="butterfly" style="--left:{(i*2.5)%100}%; --duration:{3+(i%3)}s; --delay:{i*0.1}s;">🦋</div>'
    st.markdown(swarm, unsafe_allow_html=True)
    st.markdown("<div class='glass-card'><h1>💖 I LOVE YOU 💖</h1></div>", unsafe_allow_html=True)
