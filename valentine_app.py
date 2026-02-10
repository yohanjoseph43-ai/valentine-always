import streamlit as st
import time

# 1. Page Configuration
st.set_page_config(page_title="Special Deployment: Love v1.0", page_icon="💻")

# 2. Custom CSS for a clean, modern "Tech-Valentine" look
st.markdown("""
    <style>
    .stApp {
        background-color: #0e1117;
        color: #ffffff;
    }
    .reason-card {
        background-color: #262730;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #ff4b4b;
        margin-bottom: 15px;
        box-shadow: 0px 4px 15px rgba(255, 75, 75, 0.2);
        color: #fafafa;
        font-family: 'Courier New', Courier, monospace;
    }
    .header-text {
        text-align: center;
        color: #ff4b4b;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    </style>
    """, unsafe_allow_html=True)

# Initialize session state for the interaction
if 'answered' not in st.session_state:
    st.session_state.answered = False

# --- APP LOGIC ---

if not st.session_state.answered:
    # LANDING PAGE: The Question
    st.markdown("<h1 class='header-text'>// Requesting Connection...</h1>", unsafe_allow_html=True)
    st.write("### Hey [Name], my heart is stuck in an infinite loop of thinking about you.")
    st.write("I've finished the build for our future. Do you accept the merge request?")
    
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Accept (YES) 😍"):
            st.session_state.answered = True
            st.rerun()

    with col2:
        # A playful "No" button for a programmer
        if st.button("Reject (No) 😢"):
            st.error("Access Denied: Permission 'No' not granted to current user. Please try 'Accept'.")
            time.sleep(1)

else:
    # SUCCESS PAGE: The Reasons
    st.balloons()
    st.markdown("<h1 class='header-text'>Connection Established! ❤️</h1>", unsafe_allow_html=True)
    st.success("Build Successful: You've made me the happiest dev in the world.")
    
    st.write("### 💌 Why you're my favorite human:")

    # Reasons List (Tech/Programmer flavored)
    reasons = [
        "✨ You're the 'Global Variable' in my life—everything depends on you.",
        "🚀 Every day with you is a 'Successful Deploy' with zero errors.",
        "🌟 You're the only person who can debug my bad mood without a stack trace.",
        "💻 I'd definitely choose you over a dark mode IDE (and that's saying a lot).",
        "🔥 You make my heart rate go higher than a CPU running a heavy render."
    ]

    # Display Reasons as Cards
    for reason in reasons:
        st.markdown(f"<div class='reason-card'>{reason}</div>", unsafe_allow_html=True)

    st.write("---")
    st.info("Let's go offline together for Valentine's Day. No code, just us.")
    
    if st.button("Click for a celebratory snow-fall"):
        st.snow()
