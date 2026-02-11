import streamlit as st
import time

# 1. Page Configuration
st.set_page_config(page_title="Love.OS | Grand Finale", page_icon="🥋", layout="wide")

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

    .reason-header {
        color: #ff5e78;
        font-size: 1.8rem;
        margin-top: 20px;
        margin-bottom: 5px;
        font-weight: 700;
    }

    .reason-text {
        font-size: 1.1rem;
        color: #555;
        margin-bottom: 25px;
        line-height: 1.4;
    }

    /* --- THE GRAND SWARM EFFECT --- */
    @keyframes swarm {
        0% { transform: translateY(110vh) translateX(0) rotate(0deg) scale(0.5); opacity: 0; }
        10% { opacity: 1; }
        90% { opacity: 1; }
        100% { transform: translateY(-20vh) translateX(150px) rotate(720deg) scale(2.5); opacity: 0; }
    }

    .butterfly {
        position: fixed; bottom: -100px; font-size: 45px;
        user-select: none; pointer-events: none; z-index: 9999;
        animation: swarm var(--duration) infinite ease-in;
        left: var(--left); animation-delay: var(--delay);
    }

    /* --- FIXED: THE HYPER-PANIC NO BUTTON --- */
    @keyframes hyper-panic {
        0% { transform: translate(0, 0); }
        10% { transform: translate(-40px, -20px); }
        30% { transform: translate(40px, 20px); }
        50% { transform: translate(-40px, 30px); }
        100% { transform: translate(0, 0); }
    }

    div[data-testid="column"]:nth-child(2) div.stButton {
        animation: hyper-panic 0.1s infinite;
    }

    div.stButton > button {
        border-radius: 30px;
        height: 3.5em;
        background: linear-gradient(90deg, #ff758c 0%, #ff7eb3 100%);
        color: white;
        border: none;
        font-weight: 600;
        width: 100%;
    }
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
    col1, col2, col3 = st.columns([1, 1.5, 1])
    with col2:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.write("🔒 **ENCRYPTED FILE: OPEN_HEART.EXE**")
        password = st.text_input("Enter Secret Key (City where we first met?):", type="default")
        if st.button("Decrypt"):
            if password.lower() == "kochi": move_to("proposal")
            else: st.error("Access Denied.")
        st.markdown("</div>", unsafe_allow_html=True)

# --- STEP 2: PROPOSAL ---
elif st.session_state.step == "proposal":
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<div class='glass-card'><span style='font-size:70px;'>🌸</span>", unsafe_allow_html=True)
        st.write("## Will you be my Valentine?")
        c1, c2 = st.columns(2)
        with c1:
            if st.button("YES! 😍"): st.balloons(); move_to("karate")
        with c2:
            if st.button("No 😢"): st.toast("Error: Selection disabled.")
        st.markdown("</div>", unsafe_allow_html=True)

# --- STEP 3: KARATE CHALLENGE ---
elif st.session_state.step == "karate":
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.write("🥋 **KARATE CHALLENGE**")
        st.progress(st.session_state.strikes / 10)
        if st.button("PUNCH! 👊"):
            st.session_state.strikes += 1
            if st.session_state.strikes >= 10: move_to("memories")
            else: st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

# --- STEP 4: VISUAL ARCHIVES ---
elif st.session_state.step == "memories":
    col1, col2, col3 = st.columns([1, 4, 1])
    with col2:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.write("### 📸 Visual Archives")
        c1, c2 = st.columns(2)
        c1.image("https://via.placeholder.com/400", caption="Photo 1")
        c2.image("https://via.placeholder.com/400", caption="Photo 2")
        if st.button("Analyze Connection ➡️"): move_to("reasons")
        st.markdown("</div>", unsafe_allow_html=True)

# --- STEP 5: REASONS WHY (With Headers) ---
elif st.session_state.step == "reasons":
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.write("### 🔍 System Analysis: Core Reasons")
        
        # Reason 1
        st.markdown("<div class='reason-header'>✨ Your Radiance</div>", unsafe_allow_html=True)
        st.markdown("<div class='reason-text'>The way your smile reboots my entire day. It's the highlight of my digital world.</div>", unsafe_allow_html=True)
        
        # Reason 2
        st.markdown("<div class='reason-header'>🥋 Your Spirit</div>", unsafe_allow_html=True)
        st.markdown("<div class='reason-text'>You're the strongest person I know. Whether in the dojo or in life, you never back down.</div>", unsafe_allow_html=True)
        
        # Reason 3
        st.markdown("<div class='reason-header'>🧠 Your Mind</div>", unsafe_allow_html=True)
        st.markdown("<div class='reason-text'>I love the way you think and how smart you are. Every conversation with you is an adventure.</div>", unsafe_allow_html=True)
        
        # Reason 4
        st.markdown("<div class='reason-header'>🌸 Your Kindness</div>", unsafe_allow_html=True)
        st.markdown("<div class='reason-text'>The way you care for others makes me want to be a better person every single day.</div>", unsafe_allow_html=True)

        if st.button("Unlock Soundtrack ➡️"): move_to("soundtrack")
        st.markdown("</div>", unsafe_allow_html=True)

# --- STEP 6: SOUNDTRACK ---
elif st.session_state.step == "soundtrack":
    st.progress(0.7)
    st.markdown("<h2 style='text-align:center; color:white;'>🎶 Heart's OST</h2>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        songs = [
            {"t": "Arz Kiya Hai", "a": "Anuv Jain", "u": "https://music.youtube.com/watch?v=-BJt4fCAtZE"}
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

# --- STEP 7: SECRET LETTER ---
elif st.session_state.step == "secret_letter":
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.markdown("""<div style='background: white; border: 2px dashed #ff758c; padding: 30px; text-align: left; border-radius: 15px; color: #444;'>
        My Dearest,<br><br>
        I love you forever. You are my favorite teammate and my best friend.<br><br>
        OSS!<br>
        Yours always.</div>""", unsafe_allow_html=True)
        if st.button("The Final Step ➡️"): move_to("finale")
        st.markdown("</div>", unsafe_allow_html=True)

# --- STEP 8: THE GRAND SWARM FINALE ---
elif st.session_state.step == "finale":
    swarm_html = ""
    emojis = ["🦋", "💖", "🌸", "✨", "🦋", "🌷"]
    for i in range(40): # Increased to 40 for a truly grand effect
        left = f"{(i * 2.5) % 100}%"
        duration = f"{3 + (i % 3)}s"
        delay = f"{i * 0.08}s"
        emoji = emojis[i % 6]
        swarm_html += f'<div class="butterfly" style="--left:{left}; --duration:{duration}; --delay:{delay};">{emoji}</div>'
    
    st.markdown(swarm_html, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.markdown("<h1 style='color: #ff758c;'>💖 YES! 💖</h1>", unsafe_allow_html=True)
        st.write("## Connection Verified: 100% Sync")
        st.write("### I Love You Forever.")
        if st.button("Restart Journey 🔄"): st.session_state.strikes = 0; move_to("security")
        st.markdown("</div>", unsafe_allow_html=True)
