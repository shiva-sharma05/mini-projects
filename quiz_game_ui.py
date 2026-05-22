import streamlit as st

st.set_page_config(page_title="Quiz Game", page_icon="🎯")

st.title("🎯 QUIZ GAME")
st.write("Answer the questions and check your score!")

score = 0

# Question 1
st.subheader("1. First ruler of Khilzi dynasty")
q1 = st.radio(
    "Choose your answer",
    ["a) allaudin khilzi",
     "b) niladhvaj khen",
     "c) jalal-ud-din khilzi",
     "d) shihab-ud-bin omar"],
    key="q1"
)

# Question 2
st.subheader("2. Which country had second largest population after 2025?")
q2 = st.radio(
    "Choose your answer ",
    ["a) USA",
     "b) India",
     "c) China",
     "d) Brazil"],
    key="q2"
)

# Question 3
st.subheader("3. Capital of Nepal is")
q3 = st.radio(
    "Choose your answer  ",
    ["a) Lalitpur",
     "b) Bhaktapur",
     "c) Lumbini",
     "d) Kathmandu"],
    key="q3"
)

# Question 4
st.subheader("4. Who is the father of Mughal emperor Jahangir?")
q4 = st.radio(
    "Choose your answer   ",
    ["a) Babar",
     "b) Akbar",
     "c) Humayun",
     "d) Aurangzeb"],
    key="q4"
)

# Question 5
st.subheader("5. Who created Python?")
q5 = st.radio(
    "Choose your answer    ",
    ["a) Dennis Ritchie",
     "b) James Gosling",
     "c) Guido van Rossum",
     "d) Elon Musk"],
    key="q5"
)

# Submit Button
if st.button("Submit Quiz"):

    if q1 == "c) jalal-ud-din khilzi":
        score += 10

    if q2 == "c) China":
        score += 10

    if q3 == "d) Kathmandu":
        score += 10

    if q4 == "b) Akbar":
        score += 10

    if q5 == "c) Guido van Rossum":
        score += 10

    st.success(f"🎉 Your Score is {score} / 50")

    if score == 50:
        st.balloons()
        st.write("🔥 Excellent!")
    elif score >= 30:
        st.write("👍 Good Job!")
    else:
        st.write("😅 Keep Practicing!")