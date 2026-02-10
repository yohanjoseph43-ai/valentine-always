import streamlit as st
import time

# 1. Page Configuration
st.set_page_config(page_title="Love.OS | Full Deployment", page_icon="🥋", layout="wide")

# 2. Professional Anime-Tech Styling (CSS)
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

    /* Special Letter Styling */
    .letter-card {
        background: rgba(255, 255, 255, 0.7);
        border: 2px dashed #ff758c;
        border-radius: 20px;
        padding: 30px;
        margin-top: 20px;
        animation: fadeIn 2s;
        text-align: left;
    }

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
    
    @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
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
                st.error("Access Denied. Hint: Where our story began.")
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
            st.toast("Error: Action 'No' is locked. Try 'Yes' instead!")

# --- STEP 3: KARATE CHALLENGE ---
elif st.session_state.step == "karate":
    st.progress(0.3)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.write("🥋 **KARATE CHALLENGE**")
        st.write("Proof of strength required! Strike the target 10 times.")
        st.progress(st.session_state.strikes / 10)
        if st.button("PUNCH! 👊"):
            st.session_state.strikes += 1
            if st.session_state.strikes >= 10:
                st.success("DOJO CHALLENGE COMPLETE!")
                time.sleep(0.5)
                move_to("memories")
            else:
                st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

# --- STEP 4: VISUAL ARCHIVES ---
elif st.session_state.step == "memories":
    st.progress(0.5)
    st.markdown("<h2 style='text-align:center; color:white;'>📸 Visual Archives</h2>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 4, 1])
    with col2:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        img_c1, img_c2 = st.columns(2)
        try:
            img_c1.image("photo1.jpg", caption="Our First Date", use_container_width=True)
            img_c2.image("photo2.jpg", caption="Special Memory", use_container_width=True)
        except:
            img_c1.image("https://via.placeholder.com/400", caption="Photo 1 Not Found")
            img_c2.image("https://via.placeholder.com/400", caption="Photo 2 Not Found")
        st.markdown("</div>", unsafe_allow_html=True)
        if st.button("Unlock Soundtrack ➡️"): move_to("soundtrack")

# --- STEP 5: SOUNDTRACK (Clickable Cards) ---
elif st.session_state.step == "soundtrack":
    st.progress(0.7)
    st.markdown("<h2 style='text-align:center; color:white;'>🎶 Heart's OST</h2>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        songs = [
            {"t": "Arz Kiya Hai", "a": "Anuv Jain", "u": "https://music.youtube.com/watch?v=-BJt4fCAtZE"},
            {"t": "I think they call this love", "a": "Matthew Ifield", "u": "https://music.youtube.com/watch?v=0k_199YdfX4"},
            {"t": "Perfect", "a": "Ed Sheeran", "u": "https://music.youtube.com/watch?v=2Vv-BfVoq4g"}
        ]
        for s in songs:
            st.markdown(f"""
                <a href="{s['u']}" target="_blank" class="song-link">
                    <div class='glass-card' style='padding: 20px; cursor: pointer;'>
                        <h4 style='color: #ff5e78; margin: 0;'>🎵 {s['t']}</h4>
                        <p style='color: #888; font-size: 0.9em;'>{s['a']}</p>
                    </div>
                </a>
            """, unsafe_allow_html=True)
        if st.button("Read Secret Letter ➡️"): move_to("secret_letter")

# --- STEP 6: SECRET LETTER (Replaces Date Planner) ---
elif st.session_state.step == "secret_letter":
    st.progress(0.9)
    st.markdown("<h2 style='text-align:center; color:white;'>💌 Encrypted Message</h2>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.write("### ✍️ Digital Love Letter")
        # You can hardcode your message here or leave the text area
        custom_note = st.text_area("Write your heart out here...", placeholder="My dearest...")
        
        if st.button("Seal and Send ❤️"):
            st.session_state.final_note = custom_note
            move_to("finale")
        st.markdown("</div>", unsafe_allow_html=True)

# --- STEP 7: FINALE ---
elif st.session_state.step == "finale":
    # Custom Floating Particles (Butterfly Theme)
    st.markdown("""
        <div class="particle p1">🦋</div>
        <div class="particle p2">💖</div>
        <div class="particle p3">🌸</div>
        <div class="particle p4">✨</div>
        <div class="particle p5">🦋</div>
    """, unsafe_allow_html=True)

    st.progress(1.0)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        # Display the Letter the user just wrote (or hardcoded)
        if st.session_state.get('final_note'):
            st.markdown(f"""
                <div class='letter-card'>
                    <h3 style='color: #ff5e78; margin-top:0; text-align:center;'>💌 A Note for You</h3>
                    <p style='font-size: 1.1rem; color: #444; line-height: 1.6;'>"{st.session_state.final_note}"</p>
                </div>
            """, unsafe_allow_html=True)

        # Final Summary
        st.markdown("<div class='glass-card' style='margin-top: 20px;'>", unsafe_allow_html=True)
        st.markdown("<span class='anime-icon'>💖</span>", unsafe_allow_html=True)
        st.write("## Connection Verified: 100% Sync")
        st.write("---")
        st.write("## I Love You Forever.")
        if st.button("Restart Journey 🔄"):
            st.session_state.strikes = 0
            move_to("security")
        st.markdown("</div>", unsafe_allow_html=True)
