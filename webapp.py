import streamlit as st
import random
import string

st.title("Password Generator ")
st.subheader("By Ronin Barker")

st.write("What kind of password would you like?")

if "mode" not in st.session_state:
    st.session_state.mode = None

if st.button("Weak"):
    st.session_state.mode = "weak"

if st.button("Strong"):
    st.session_state.mode = "strong"

if st.session_state.mode == "weak":
    words = ["copper", "monkey", "blueberry", "yogurt", "green", "leopard", "pizza", "lemon", "iron",
             "lime", "brown", "deck", "clock", "yellow", "blue", "door", "apple", "banana", "noodle", "blue", "television",
             "vehicle", "germany", "canada", "america", "octopus", "beer", "emerald", "koala", "kangaroo", "pill", "window",
             "plane", "backflip", "vitamin", "figure", "dance", "music", "piano", "bird", "ostrich", "giraffe"]
    numbers = [str(i) for i in range(1000)]
    password = random.choice(words) + random.choice(numbers)
    st.error("Maybe consider the other option there")
    st.success(password)

if st.session_state.mode == "strong":
    length = st.number_input("How many characters would you like in your password? (Maximum 50)", min_value=5, max_value=50, value=15)
    user_choice1 = st.checkbox("Letters", value=True)
    user_choice2 = st.checkbox("Numbers", value=True)
    user_choice3 = st.checkbox("Symbols", value=True)
    chars = ""
    if user_choice1:
        chars += string.ascii_letters

    if user_choice2:
        chars += string.digits

    if user_choice3:
        chars += string.punctuation

    if chars == "":
        st.error("You can't really make a password without any characters")
    else:
        password = "".join(random.choice(chars) for _ in range(length))
        st.write("**Here is your password:**")
        st.success(password)
        st.write("Enjoy your password, keep it in a safe place where you will remember it. :)")
        st.write("**If the password does not meet your site's requirements try adding characters to the password to meet the requirements**")
        st.write("<span style='color:red;'>**NEVER SHARE YOUR PASSWORD WITH OTHERS!**</span>", unsafe_allow_html=True)


