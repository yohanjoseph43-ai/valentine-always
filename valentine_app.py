import streamlit as st
import time

# 1. Page & Metadata Configuration
st.set_page_config(
    page_title="Love.OS | v2.0 Deployment", 
    page_icon="🥋", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Professional Anime-Tech Styling (CSS)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@400;600&family=Varela+Round&display=swap');
    
    html, body, [class*="css"] { 
        font-family: 'Varela Round', sans-serif; 
    }
    
    .stApp {
        background: linear-gradient(180deg, #ffdde1 0%, #ee9ca7 100%);
        background-attachment: fixed;
    }

    /* Glassmorphism Card Design */
    .glass-card {
        background: rgba(255, 255, 255, 0.4);
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        border: 2px solid rgba(255, 255, 255, 0.6);
        border-radius: 30px;
        padding: 35px;
        box-shadow: 0 10px 30px rgba(255, 182, 193, 0.4);
        color: #5d5d5d;
        text-align: center;
        margin-bottom: 20px;
        transition: transform 0.3s ease;
    }

    .glass-card:hover {
        transform: translateY(-5px);
    }

    /* Anime Floating Animation */
    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-15px); }
        100% { transform: translateY(0px); }
    }
    .anime-icon { 
        font-size: 80px; 
        display: block; 
        margin: 0 auto; 
        animation: float 3s infinite ease-in-out; 
    }

    /* Custom Progress Bar Color */
    .stProgress > div > div > div > div {
        background-image: linear-gradient(to right, #ff758c , #ff7eb3);
    }

    /* Styled Buttons */
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

    /* Song Link Styling */
    .song-card {
        text-decoration: none;
        color: inherit;
        display: block;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. State Management Logic
if 'step' not in st.session_state:
    st.session_state.step = "security"
if 'strikes' not in st.session_state:
    st.session_state.strikes = 0

def move_to(step_name):
    st.session_state.step = step_name
    st.rerun()

# --- TOP NAVIGATION / PROGRESS ---
if st.session_state.step != "security":
    steps_list = ["proposal", "karate", "memories", "soundtrack", "date", "finale"]
    try:
        current_idx = steps_list.index(st.session_state.step)
        st.progress((current_idx + 1) / len(steps_list))
    except ValueError:
        pass

# --- STEP 1: SECURITY GATE ---
if st.session_state.step == "security":
    st.write("##")
    col1, col2, col3 = st.columns([1, 1.5, 1])
    with col2:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.write("🔒 **SECURE SERVER ACCESS**")
        st.write("To proceed, enter the city where we first met.")
        password = st.text_input("Answer:", type="default", placeholder="Type here...")
        if st.button("Unlock Module"):
            # CURRENTLY SET TO KOCHI BASED ON YOUR CONTEXT
            if password.lower() == "kochi": 
                st.success("Identity Verified.")
                time.sleep(1)
                move_to("proposal")
            else:
                st.error("Access Denied. Hint: Check our first chat location!")
        st.markdown("</div>", unsafe_allow_html=True)

# --- STEP 2: PROPOSAL ---
elif st.session_state.step == "proposal":
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<div style='text-align:center;'><span class='anime-icon'>🌸</span></div>", unsafe_allow_html=True)
        st.markdown("""
            <div class='glass-card'>
                <h1 style='color: #ff5e78;'>// INITIALIZING_HEART_LINK</h1>
                <p style='color: #7a7a7a;'>Connection Status: <b>Strong</b></p>
                <hr style='border: 0.5px solid rgba(255,255,255,0.5); margin: 25px 0;'>
                <h2 style='color: #ff5e78;'>Will you be my Valentine?</h2>
            </div>
        """, unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        if c1.button("YES! 😍"):
            st.balloons()
            time.sleep(1)
            move_to("karate")
        if c2.button("No 😢"):
            st.toast("Warning: Selection disabled for your own happiness.")

# --- STEP 3: KARATE CHALLENGE ---
elif st.session_state.step == "karate":
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.markdown("<div class='anime-icon'>🥋</div>", unsafe_allow_html=True)
        st.write("### BREAK THE WALL!")
        st.write("Strike the target 10 times to unlock our memories.")
        st.progress(st.session_state.strikes / 10)
        if st.button("STRIKE! 👊"):
            st.session_state.strikes += 1
            if st.session_state.strikes >= 10:
                st.success("Target Broken! Level Up.")
                time.sleep(1)
                move_to("memories")
            else:
                st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

# --- STEP 4: VISUAL ARCHIVES ---
elif st.session_state.step == "memories":
    st.markdown("<h1 style='text-align:center; color:white;'>📸 Visual Archives</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 4, 1])
    with col2:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        img_c1, img_c2 = st.columns(2)
        # TIP: Upload images to your repo and use the filenames here
        img_c1.image("https://via.placeholder.com/500", caption="A Special Day", use_container_width=True)
        img_c2.image("https://via.placeholder.com/500", caption="A Happy Memory", use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
        if st.button("Unlock Soundtrack ➡️"):
            move_to("soundtrack")

# --- STEP 5: SOUNDTRACK (CLICKABLE) ---
elif st.session_state.step == "soundtrack":
    st.markdown("<h1 style='text-align:center; color:white;'>🎶 Heart's OST</h1>", unsafe_allow_html=True)
    st.write("<p style='text-align:center; color:white;'>Tap any card to play on YouTube Music</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        songs = [
            {"t": "Arz Kiya Hai", "a": "Anuv Jain", "u": "https://music.youtube.com/watch?v=-BJt4fCAtZE"},
            {"t": "I think they call this love", "a": "Matthew Ifield", "u": "https://music.youtube.com/watch?v=0k_199YdfX4"},
            {"t": "Perfect", "a": "Ed Sheeran", "u": "https://music.youtube.com/watch?v=2Vv-BfVoq4g"}
        ]
        for s in songs:
            st.markdown(f"""
                <a href="{s['u']}" target="_blank" class="song-card">
                    <div class='glass-card' style='padding: 20px;'>
                        <h4 style='color: #ff5e78; margin: 0;'>🎵 {s['t']}</h4>
                        <p style='color: #888; font-size: 0.9em; margin: 5px 0;'>{s['a']}</p>
                    </div>
                </a>
            """, unsafe_allow_html=True)
        
        if st.button("Proceed to Date Selection ➡️"):
            move_to("date")

# --- STEP 6: DATE SELECTOR ---
elif st.session_state.step == "date":
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.write("### 🎟️ PICK OUR ADVENTURE")
        choice = st.radio("Choose the flavor of our next date:", 
                          ["Fancy Dinner 👗", "Arcade & Pizza 🍕", "Cozy Movie Night 🍿"])
        if st.button("Confirm Selection"):
            st.session_state.date_choice = choice
            move_to("finale")
        st.markdown("</div>", unsafe_allow_html=True)

# --- STEP 7: FINALE ---
elif st.session_state.step == "finale":
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.markdown("<div class='anime-icon'>💖</div>", unsafe_allow_html=True)
        st.write("### ANALYSIS COMPLETE")
        st.write(f"**Sync Rate:** 100% | **Next Quest:** {st.session_state.get('date_choice', 'TBD')}")
        st.write("## I Love You More Than Code.")
        if st.button("Start Story Again 🔄"):
            st.session_state.strikes = 0
            move_to("security")
        st.markdown("</div>", unsafe_allow_html=True)
        st.snow()
