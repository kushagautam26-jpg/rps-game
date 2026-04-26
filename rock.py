import streamlit as st
import random

st.title("Rock Paper Scissors")

choice = st.selectbox("Choose:", ["rock", "paper", "scissors"])

if st.button("Play"):
    computer = random.choice(["rock", "paper", "scissors"])

    if choice == computer:
        result = "Draw!"
    elif (choice == "rock" and computer == "scissors") or \
         (choice == "paper" and computer == "rock") or \
         (choice == "scissors" and computer == "paper"):
        result = "You Win!"
    else:
        result = "Computer Wins!"

    st.write("Computer chose:", computer)
    st.write(result)