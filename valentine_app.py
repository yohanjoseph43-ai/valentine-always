import streamlit as st
import time

# 1. Page Configuration
st.set_page_config(page_title="Love.OS | v2.0", page_icon="🥋", layout="wide")

# 2. Styling (CSS)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@400;600&family=Varela+Round&display=swap');
    html, body, [class*="css"] { font-family: 'Varela Round', sans-serif; }
    
    .stApp {
        background: linear-gradient(180deg, #ffdde1 0%, #ee9ca7 100%);
        background-attachment: fixed;
    }

    .glass-card {
        background: rgba(255, 255, 255, 0.4);
        backdrop-filter: blur(15px);
        border: 2px solid rgba(255, 255, 255, 0.6);
        border-radius: 30px;
        padding: 40px;
        box-shadow: 0 10px 30px rgba(255, 182, 193, 0.4);
        color: #5d5d5d;
        text-align: center;
        margin-bottom: 25px;
    }

    .anime-icon { font-size: 70px; display: block; margin: 0 auto; }

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
    
    .song-link { text-decoration: none; color: inherit; }

    /* --- BUTTERFLY & HEART PARTICLES --- */
    @keyframes float-up {
        0% { transform: translateY(110vh) translateX(0) rotate(0deg); opacity: 1; }
        100% { transform: translateY(-20vh) translateX(50px) rotate(20deg); opacity: 0; }
    }
    .particle {
        position: fixed;
        bottom: -50px;
        font-size: 30px;
        user-select: none;
        pointer-events: none;
        z-index: 9999;
    }
    .p1 { left: 15%; animation: float-up 8s infinite; }
    .p2 { left: 35%; animation: float-up 11s infinite; animation-delay: 2s; }
    .p3 { left: 55%; animation: float-up 7s infinite; animation-delay: 1s; }
    .p4 { left: 75%; animation: float-up 10s infinite; animation-delay: 4s; }
    .p5 { left: 95%; animation: float-up 9s infinite; animation-delay: 3s; }
    </style>
    """, unsafe_allow_html=True)

# 3. State Management
if 'step' not in st.session_state: st.session_state.step = "security"
if 'strikes' not in st.session_state: st.session_state.strikes = 0

def move_to(step_name):
    st.session_state.step = step_name
    st.rerun()

# --- STEP 1: SECURITY GATE ---
if st.session_state.step == "security":
    st.write("##")
    col1, col2, col3 = st.columns([1, 1.5, 1])
    with col2:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.write("🔒 **ENCRYPTED FILE: OPEN_HEART.EXE**")
        password = st.text_input("Enter Secret Key (City where we first met?):", type="default")
        if st.button("Decrypt"):
            if password.lower() == "kochi": 
                st.success("Identity Verified.")
                time.sleep(1)
                move_to("proposal")
            else:
                st.error("Access Denied. Hint: Where our journey began.")
        st.markdown("</div>", unsafe_allow_html=True)

# --- STEP 2: PROPOSAL ---
elif st.session_state.step == "proposal":
    st.progress(0.1)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<div class='glass-card'><span class='anime-icon'>🌸</span>", unsafe_allow_html=True)
        st.write("### // SYSTEM_PROMPT")
        st.write("## Will you be my Valentine?")
        c1, c2 = st.columns(2)
        if c1.button("YES! 😍"):
            st.balloons()
            move_to("karate")
        if c2.button("No 😢"):
            st.toast("Error: Selection disabled. Connection required.")

# --- STEP 3: KARATE CHALLENGE ---
elif st.session_state.step ==
