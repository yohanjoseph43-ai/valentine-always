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

    /* --- THE BOUNCING NO BUTTON ANIMATION --- */
    @keyframes panic-bounce {
        0% { transform: translate(0, 0); }
        20% { transform: translate(30px, -20px); }
        40% { transform: translate(-30px, 20px); }
        60% { transform: translate(40px, 30px); }
        80% { transform: translate(-40px, -30px); }
        100% { transform: translate(0, 0); }
    }

    /* Targeting the second button in the proposal column (the 'No' button) */
    div.stButton > button:active, div.stButton > button:focus {
        outline: none;
    }
    
    /* This applies the bounce to the specific 'No' button container */
    .bounce-box {
        animation: panic-bounce 0.4s infinite;
        display: inline-block;
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

    /* Floating Particles */
    @keyframes float-up {
        0% { transform: translateY(110vh) translateX(0) rotate(0deg); opacity: 1; }
        100% { transform: translateY(-20vh) translateX(50px) rotate(20deg); opacity: 0; }
    }
    .particle {
        position: fixed; bottom: -50px; font-size: 30px;
        user-select: none; pointer-events: none; z-index: 9999;
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
            if password.lower() == "bangalore": 
                st.success("Identity Verified.")
                time.sleep(1)
                move_to("proposal")
            else:
                st.error("Access Denied.")
        st.markdown("</div>", unsafe_allow_html=True)

# --- STEP 2: PROPOSAL (The Bouncing Button) ---
elif st.session_state.step == "proposal":
    st.progress(0.1)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<div class='glass-card'><span class='anime-icon'>🌸</span>", unsafe_allow_html=True)
        st.write("## Will you be Mine Forever?")
        
        c1, space, c2 = st.columns([1, 0.2, 1])
        with c1:
            if st.button("YES! 😍"):
                st.balloons()
                move_to("karate")
        with c2:
            # We wrap the 'No' button in a div that has the bounce animation
            st.markdown('<div class="bounce-box">', unsafe_allow_html=True)
            if st.button("No 😢"):
                st.toast("Nice try! The 'No' button is currently out of service.")
            st.markdown('</div>', unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

# --- STEP 3: KARATE CHALLENGE ---
elif st.session_state.step == "karate":
    st.progress(0.3)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.write("🥋 **KARATE CHALLENGE**")
        st.write("Punch my heart to see what's inside! Strike the target 10 times.")
        st.progress(st.session_state.strikes / 10)
        if st.button("PUNCH! 👊"):
            st.session_state.strikes += 1
            if st.session_state.strikes >= 10:
                st.success("OSS!")
                time.sleep(0.5)
                move_to("memories")
            else:
                st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

# --- STEP 4: VISUAL ARCHIVES ---
elif st.session_state.step == "memories":
    st.progress(0.5)
    st.markdown("<h2 style='text-align:center; color:black;'>📸 Visual Archives</h2>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 4, 1])
    with col2:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        img_c1, img_c2 = st.columns(2)
        try:
            img_c1.image("625978180_910554591451989_1397209579107700988_n.jpg", caption="Special Memory", use_container_width=True)
            img_c2.image("627368267_1196088558998310_7517174288371660696_n.jpg", caption="Special Memory", use_container_width=True)
        except:
            img_c1.image("https://via.placeholder.com/400", caption="Photo 1 missing")
            img_c2.image("https://via.placeholder.com/400", caption="Photo 2 missing")
        st.markdown("</div>", unsafe_allow_html=True)
        if st.button("Unlock Soundtrack ➡️"): move_to("soundtrack")

# --- STEP 5: SOUNDTRACK ---
elif st.session_state.step == "soundtrack":
    st.progress(0.7)
    st.markdown("<h2 style='text-align:center; color:white;'>🎶 Songs that remind me of you</h2>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        songs = [
            {"t": "Naan Pogiren", "a": "S.P. Balasubrahmanyam & K.S. Chitra", "u":"https://open.spotify.com/track/16jOVIIrpo7XV8KOnx4ZwX?si=f56bf10b577242ac"},
            {"t": "I think they call this love", "a": "Matthew Ifield", "u": "https://open.spotify.com/track/14mT8BCOXiUUcGlb7KujkT?si=b374b595daa74786"},
            {"t": "Arz Kiya Hai", "a": "Anuv Jain", "u": "https://open.spotify.com/track/1bMkimTb47umgNP6xCi4A1?si=cf336cbbe95343dd"}
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

# --- STEP 6: THE SECRET LETTER ---
elif st.session_state.step == "secret_letter":
    st.progress(0.9)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        secret_letter_text = """
        My Dearest Anu,<br><br>
        I wanted to take a moment to tell you how much you mean to me. 
        From our first meet in Kochi to every training session we've shared, 
        you have been the best part of my days.<br><br>
        Thank you for being my teammate, my best friend, and my favorite person. 
        I love you forever.<br><br>
        Yours always.
        """
        st.markdown(f"""
            <div class='letter-card'>
                <h2 style='color: #ff758c; text-align: center;'>💌 To My Valentine</h2>
                {secret_letter_text}
            </div>
        """, unsafe_allow_html=True)
        if st.button("The Final Step ➡️"): move_to("finale")
        st.markdown("</div>", unsafe_allow_html=True)

# --- STEP 7: FINALE ---
elif st.session_state.step == "finale":
    st.markdown("""
        <div class="particle p1">🦋</div>
        <div class="particle p2">💖</div>
        <div class="particle p3">🌸</div>
        <div class="particle p4">✨</div>
        <div class="particle p5">🦋</div>
    """, unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.markdown("<span class='anime-icon'>💖</span>", unsafe_allow_html=True)
        st.write("## Connection Verified: 100% Sync")
        st.write("## I Love You Forever.")
        if st.button("Restart Journey 🔄"):
            st.session_state.strikes = 0
            move_to("security")
        st.markdown("</div>", unsafe_allow_html=True)
