import streamlit as st
import random
import time

# Page configuration
st.set_page_config(page_title="A Special Message for You", page_icon="❤️")

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        background-color: #fff5f5;
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        height: 3em;
        background-color: #ff4b4b;
        color: white;
    }
    .title-text {
        text-align: center;
        color: #d32f2f;
        font-family: 'Comic Sans MS', cursive;
    }
    </style>
    """, unsafe_allow_html=True)

# Session state to track if she said YES!
if 'answered' not in st.session_state:
    st.session_state.answered = False

# Title
st.markdown("<h1 class='title-text'>Hey [Girlfriend's Name]! ❤️</h1>", unsafe_allow_html=True)

if not st.session_state.answered:
    st.write("### I have a very important question to ask you...")
    
    # Use columns for buttons
    col1, col2 = st.columns(2)

    with col1:
        if st.button("YES! 😍"):
            st.session_state.answered = True
            st.balloons()
            st.rerun()

    with col2:
        # A little humor: The "No" button logic
        no_button = st.button("No 😢")
        if no_button:
            st.warning("Error 404: 'No' option not found. Please try the other button! 😉")
            time.sleep(1)

else:
    # This shows after she clicks YES
    st.success("## WOO-HOO! You made me the happiest programmer alive! 🚀")
    
    # You can add a link to a photo or a GIF here
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHFpZzF4NXp6ZzR4ZzR4ZzR4ZzR4ZzR4ZzR4ZzR4ZzR4ZzR4JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCBmcm9tX2dpZmh5X2NvbS80SDB4ZzR4ZzR4ZzR4L2dpZmh5LmdpZg/v1.Y2lkPTc5MGI3NjExNHFpZzF4NXp6ZzR4ZzR4ZzR4ZzR4ZzR4ZzR4ZzR4ZzR4ZzR4JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCBmcm9tX2dpZmh5X2NvbS80SDB4ZzR4ZzR4ZzR4L2dpZmh5LmdpZg/L4lvBpHnJdcED0m7qO/giphy.gif")
    
    st.write("""
    Every line of code I write is better because of you. 
    Thanks for being my favorite person! 
    
    **Plan for Feb 14th:**
    - [ ] Fancy Dinner 🍝
    - [ ] No debugging allowed ❌
    - [ ] Lots of laughs ❤️
    """)
    
    st.snow()
