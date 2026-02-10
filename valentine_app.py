import streamlit as st
import time

# 1. Page Configuration
st.set_page_config(page_title="A Message From My Heart", page_icon="💖")

# 2. Custom CSS for a Romantic, Soft Background
st.markdown("""
    <style>
    /* This creates the romantic gradient background */
    .stApp {
        background: linear-gradient(135deg, #ffafbd 0%, #ffc3a0 100%);
    }
    
    /* Styling for the "Love Letter" cards */
    .reason-card {
        background-color: rgba(255, 255, 255, 0.9);
        padding: 20px;
        border-radius: 20px;
        border: 1px solid #ff4b4b;
        margin-bottom: 15px;
        box-shadow: 4px 4px 15px rgba(0, 0, 0, 0.1);
        color: #d32f2f;
        font-family: 'Georgia', serif;
        font-size: 1.1em;
        line-height: 1.5;
    }
    
    /* Center the title and make it pop */
    .header-text {
        text-align: center;
        color: white;
        font-family: 'Brush Script MT', cursive;
        font-size: 3em;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
        padding-top: 20px;
    }

    /* Styling the buttons to look more "Valentine" */
    div.stButton > button:first-child {
        background-color: #ff4b4b;
        color: white;
        border-radius: 50px;
        border: none;
        padding: 10px 30px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# Initialize session state
if 'answered' not in st.session_state:
    st.session_state.answered = False

# --- APP LOGIC ---

if not st.session_state.answered:
    # LANDING PAGE
    st.markdown("<h1 class='header-text'>To My Favorite Person... ❤️</h1>", unsafe_allow_html=True)
    st.write("### I built something special for you because you mean the world to me.")
    st.write("Before you enter, I have one very important question:")
    
    st.markdown("## Will you be my Valentine?")
    
    col1, col2 = st.columns(2)

    with col1:
        if st.button("YES! 😍"):
            st.session_state.answered = True
            st.rerun()

    with col2:
        if st.button("No 😢"):
            st.warning("Error: This choice is currently unavailable. Please select 'YES' to continue! 😉")
            time.sleep(1)

else:
    # SUCCESS PAGE
    st.balloons()
    st.markdown("<h1 class='header-text'>She Said Yes! ❤️</h1>", unsafe_allow_html=True)
    
    st.write("### 💌 Reasons why I'm so lucky to have you:")

    # Updated Reasons (Purely Romantic)
    reasons = [
        "🌹 You have the kindest heart I've ever known.",
        "✨ You make every day feel brighter just by being in it.",
        "⭐ You're the first person I want to talk to when I wake up and the last before I sleep.",
        "💫 Your laugh is my favorite sound in the entire world.",
        "❤️ You support my dreams and make me want to be a better person every single day."
    ]

    # Display Reasons
    for reason in reasons:
        st.markdown(f"<div class='reason-card'>{reason}</div>", unsafe_allow_html=True)

    st.write("---")
    st.markdown("### I can't wait for our Valentine's date! 🍷🍝")
    
    if st.button("Click for a little extra magic"):
        st.snow()
