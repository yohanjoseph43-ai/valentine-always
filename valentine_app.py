import streamlit as st
import time

# 1. Page Configuration
st.set_page_config(page_title="Project Love v2.0", page_icon="💖", layout="wide")

# 2. Symmetrical & Clean Styling (CSS)
st.markdown("""
    <style>
    /* Gradient Background */
    .stApp {
        background: linear-gradient(135deg, #ffafbd 0%, #ffc3a0 100%);
    }
    
    /* Center all main headers */
    .header-text {
        text-align: center;
        color: white;
        text-shadow: 2px 2px 8px rgba(0,0,0,0.2);
        font-family: 'Helvetica Neue', sans-serif;
    }

    /* Glassmorphism Card Style */
    .glass-card {
        background: rgba(255, 255, 255, 0.25);
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.1);
        backdrop-filter: blur(4px);
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.18);
        padding: 25px;
        margin-bottom: 20px;
        color: white;
    }
    
    /* Symmetrical button styling */
    div.stButton > button {
        width: 100%;
        border-radius: 25px;
        border: none;
        background-color: #ff4b4b;
        color: white;
        transition: 0.3s;
    }
    div.stButton > button:hover {
        background-color: #ff7575;
        transform: scale(1.02);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar Navigation (Keeps the main UI clean)
with st.sidebar:
    st.markdown("## 💌 Secret Menu")
    page = st.radio("Navigate:", ["The Proposal", "Why I Love You", "Love Analytics", "The Date Pass"])
    st.divider()
    st.write("Status: *Highly Encrypted Love*")

# --- PAGE 1: THE PROPOSAL ---
if page == "The Proposal":
    st.markdown("<h1 class='header-text'>Connection Request... ❤️</h1>", unsafe_allow_html=True)
    
    # Symmetrical layout for the question
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
            <div class='glass-card' style='text-align: center;'>
                <h3>System analysis complete.</h3>
                <p>One question remains for the User:</p>
                <h2>Will you be my Valentine?</h2>
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

# --- PAGE 2: WHY I LOVE YOU (Balanced Cards) ---
elif page == "Why I Love You":
    st.markdown("<h1 class='header-text'>💌 Why You?</h1>", unsafe_allow_html=True)
    
    reasons = [
        ("🌟 Kindness", "You have the kindest soul I've ever met."),
        ("💻 My Support", "You are the best 'User Interface' of my life."),
        ("✨ Magic", "You turn ordinary days into memories."),
        ("🍕 Comfort", "You're my favorite person to do nothing with.")
    ]
    
    # Create 2x2 Symmetrical Grid
    col_left, col_right = st.columns(2)
    for i, (title, body) in enumerate(reasons):
        target_col = col_left if i % 2 == 0 else col_right
        with target_col:
            st.markdown(f"""
                <div class='glass-card'>
                    <h3 style='margin-top:0;'>{title}</h3>
                    <p>{body}</p>
                </div>
            """, unsafe_allow_html=True)

# --- PAGE 3: LOVE ANALYTICS (Interactive) ---
elif page == "Love Analytics":
    st.markdown("<h1 class='header-text'>📊 The Data of Us</h1>", unsafe_allow_html=True)
    
    # Metrics Row
    c1, c2, c3 = st.columns(3)
    c1.metric("Current Love Level", "Infinite", "↑ 100%")
    c2.metric("Patience Level", "Legendary", "Max")
    c3.metric("Happiness Index", "9999+", "🚀")
    
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.write("### Adjust the slider to check my love for you:")
    love_slider = st.select_slider("", options=["A lot", "To the moon", "To the galaxy", "Infinite Loop"])
    if love_slider == "Infinite Loop":
        st.snow()
        st.write("❤️ **CRITICAL ERROR: LOVE OVERFLOW!** ❤️")
    st.markdown("</div>", unsafe_allow_html=True)

# --- PAGE 4: THE DATE PASS ---
elif page == "The Date Pass":
    st.markdown("<h1 class='header-text'>🎟️ Official Admittance</h1>", unsafe_allow_html=True)
    
    col_l, col_m, col_r = st.columns([1, 1.5, 1])
    with col_m:
        st.markdown("""
            <div style="background: white; border: 4px dashed #ff4b4b; padding: 30px; border-radius: 15px; text-align: center; color: #333;">
                <h1 style="color: #ff4b4b; margin-bottom:0;">VALENTINE TICKET</h1>
                <small>VOID IF NOT USED WITH A SMILE</small>
                <hr>
                <p><b>Admits One For:</b><br>A Perfect Romantic Dinner</p>
                <p><b>Location:</b> Our Favorite Spot</p>
                <p><b>Date:</b> Feb 14th, 2026</p>
                <div style="background-color: #ff4b4b; color: white; padding: 10px; border-radius: 10px;">
                    REDEEMABLE FOR UNLIMITED HUGS
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        if st.button("CLAIM RESERVATION"):
            st.toast("Booking Confirmed! I'll see you then!", icon="🎉")
