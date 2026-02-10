import streamlit as st
import time
from datetime import datetime

# 1. Page Config
st.set_page_config(page_title="Project: Always Yours", page_icon="💝", layout="wide")

# 2. Symmetrical & Clean Styling
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #ffafbd 0%, #ffc3a0 100%);
    }
    [data-testid="stSidebar"] {
        background-color: rgba(255, 255, 255, 0.3);
    }
    .main-card {
        background-color: rgba(255, 255, 255, 0.9);
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        text-align: center;
        color: #d32f2f;
    }
    .stat-box {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 15px;
        border-bottom: 4px solid #ff4b4b;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar Navigation
with st.sidebar:
    st.title("💖 Navigation")
    menu = st.radio("Go to:", ["The Question", "Our Story", "Reasons Why", "Love Stats", "The Date Ticket"])
    st.write("---")
    st.write("Logged in as: *The Luckiest Guy*")

# --- PAGE 1: THE QUESTION ---
if menu == "The Question":
    st.markdown("<div class='main-card'>", unsafe_allow_html=True)
    st.title("Incoming Request... 💌")
    st.write("### I've been running some tests on my heart, and the results are 100% consistent.")
    st.write("Will you be my Valentine?")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("YES! 😍", use_container_width=True):
            st.balloons()
            st.success("Access Granted! Check the other pages in the sidebar! ✨")
    with col2:
        if st.button("No 😢", use_container_width=True):
            st.toast("Error: System does not support this choice.", icon="🚫")
    st.markdown("</div>", unsafe_allow_html=True)

# --- PAGE 2: OUR STORY (Photo Gallery Placeholder) ---
elif menu == "Our Story":
    st.title("📸 Memory Lane")
    st.write("A few highlights from our 'Production Environment' together.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<div class='stat-box'><h3>First Meet</h3><p>Where the first commit happened.</p></div>", unsafe_allow_html=True)
        # st.image("photo1.jpg") # Uncomment and add your photo path
    with col2:
        st.markdown("<div class='stat-box'><h3>Favorite Date</h3><p>The best uptime we've ever had.</p></div>", unsafe_allow_html=True)
        # st.image("photo2.jpg") # Uncomment and add your photo path

# --- PAGE 3: REASONS WHY ---
elif menu == "Reasons Why":
    st.title("💌 5 Reasons I Love You")
    
    reasons = {
        "User Interface": "Your smile is the most beautiful UI I've ever seen.",
        "Reliability": "You are the most dependable person in my life.",
        "Optimization": "You make me a better version of myself every day.",
        "Security": "I feel completely safe whenever I'm with you.",
        "Open Source": "You're always honest and open with me, and I love that."
    }
    
    for title, text in reasons.items():
        with st.expander(f"✨ {title}"):
            st.write(text)

# --- PAGE 4: LOVE STATS ---
elif menu == "Love Stats":
    st.title("📊 Love Analytics")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Love Level", value="Infinite", delta="100%")
    with col2:
        st.metric(label="Arguments Won", value="0", delta="-100%")
    with col3:
        st.metric(label="Happiness Index", value="Max", delta="🚀")
    
    st.write("### How much do you love me?")
    slider_val = st.select_slider("", options=["A little", "A lot", "To the moon", "To the galaxy", "Infinite Loop"])
    if slider_val == "Infinite Loop":
        st.snow()

# --- PAGE 5: THE DATE TICKET ---
elif menu == "The Date Ticket":
    st.title("🎟️ Official Reservation")
    
    st.markdown("""
        <div style="border: 5px dashed white; padding: 40px; border-radius: 20px; text-align: center;">
            <h1 style="color: white;">VALENTINE'S DAY PASS</h1>
            <hr>
            <h3>Reserved for: [Girlfriend's Name]</h3>
            <p>This ticket entitles the holder to one full evening of 
            romance, delicious food, and absolutely no bug reports.</p>
            <h2>📍 Location: [Your Favorite Restaurant]</h2>
            <h2>⏰ Time: 7:00 PM</h2>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("Confirm Attendance"):
        st.toast("Reservation Confirmed! I'll see you then! ❤️", icon="🍕")
