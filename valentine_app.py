import streamlit as st
import time

# 1. Page Configuration
st.set_page_config(page_title="Love.OS | Full Deployment", page_icon="🥋", layout="wide")

# 2. Professional Anime-Tech Styling
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
    </style>
    """, unsafe_allow_html=True)

# 3. State Management
if 'step' not in st.session_state: st.session_state.step = "security"
if 'strikes' not in st.session_state: st.session_state.strikes = 0

def move_to(step_name):
    st.session_state.step = step_name
    st.rerun()

# --- SECURITY GATE ---
if st.session_state.step == "security":
    st.write("##")
    col1, col2, col3 = st.columns([1, 1.5, 1])
    with col2:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.write("🔒 **ENCRYPTED FILE: OPEN_HEART.EXE**")
        password = st.text_input("Enter Secret Key (Where did we first meet?):", type="default")
        if st.button("Decrypt"):
            # CHANGE 'Kochi' to your actual answer!
            if password.lower() == "kochi": 
                st.success("Identity Verified. Welcome back.")
                time.sleep(1)
                move_to("proposal")
            else:
                st.error("Access Denied. Hint: The location of our first meet.")
        st.markdown("</div>", unsafe_allow_html=True)

# --- PROPOSAL ---
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
            st.toast("Error: System override initialized.")

# --- KARATE CHALLENGE ---
elif st.session_state.step == "karate":
    st.progress(0.3)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.write("🥋 **KARATE CHALLENGE**")
        st.write("Strike the target 10 times to break through to my heart!")
        st.progress(st.session_state.strikes / 10)
        if st.button("PUNCH! 👊"):
            st.session_state.strikes += 1
            if st.session_state.strikes >= 10:
                st.success("WALL BROKEN!")
                move_to("memories")
            else:
                st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

# --- MEMORIES & PHOTOS ---
elif st.session_state.step == "memories":
    st.progress(0.5)
    st.markdown("<h2 style='text-align:center; color:white;'>📸 Visual Archives</h2>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 4, 1])
    with col2:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        img_c1, img_c2 = st.columns(2)
        # REPLACE THESE WITH YOUR FILENAMES
        img_c1.image("https://via.placeholder.com/400", caption="Moment A")
        img_c2.image("https://via.placeholder.com/400", caption="Moment B")
        st.markdown("</div>", unsafe_allow_html=True)
        if st.button("Continue to Soundtrack ➡️"): move_to("soundtrack")

# --- SOUNDTRACK ---
elif st.session_state.step == "soundtrack":
    st.progress(0.7)
    st.markdown("<h2 style='text-align:center; color:white;'>🎶 Heart's OST</h2>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        songs = ["Arz Kiya Hai - Anuv Jain", "I think they call this love - Matthew Ifield", "Perfect - Ed Sheeran"]
        for s in songs:
            st.markdown(f"<div class='glass-card'><h4>{s}</h4></div>", unsafe_allow_html=True)
        if st.button("Choose Our Date ➡️"): move_to("date")

# --- DATE PLANNER ---
elif st.session_state.step == "date":
    st.progress(0.9)
    st.markdown("<h2 style='text-align:center; color:white;'>🎟️ Date Selector</h2>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        choice = st.radio("Pick your favorite adventure:", ["Fancy Dinner 👗", "Arcade & Pizza 🍕", "Cozy Movie Night 🍿"])
        if st.button("Confirm Choice"):
            st.session_state.date_choice = choice
            move_to("finale")
        st.markdown("</div>", unsafe_allow_html=True)

# --- FINALE ---
elif st.session_state.step == "finale":
    st.progress(1.0)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.markdown("<span class='anime-icon'>💖</span>", unsafe_allow_html=True)
        st.write("### FINAL ANALYSIS")
        st.write(f"Identity: Verified | Sync: 100% | Date: {st.session_state.get('date_choice', 'TBD')}")
        st.write("## I Love You Forever.")
        if st.button("Restart Magic"): move_to("security")
        st.markdown("</div>", unsafe_allow_html=True)
        st.snow()
