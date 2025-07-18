import streamlit as st
import random

st.title("guess the number")
# initialize the random number 
if "secret number" not in st.session_state:
    st.session_state.secret_number = random.randint(1,100)
    st.session_state.guesses = [0]
    st.session_sate.feedback = ""
# take input from the user
guess = st.number_input("enter your guess:", min_value =1, max_value=100, step=1)

if st.button("submit guess"):
    if guess<1 or guess>100:
        st.session_sate.feedback = "out of bounds. guess should be between 1 to 100"
    else:
        st.session_state.guess.append(guess)
        num = st.session_state.secret_number 


        if guess == num :
            st.session_state.feedback = f"congaralutations, your guess is right in {len(st.session_state.guesses)-1}: tries !"
            if abs(num-guess) - abs(num-st.session_state.guesses[-2]) :
                st.session_state.feedback = "warmer"
            else:
                st.session_state.feedback = "colder"

        else:
            if st.session_state.guesses[-2]:
                if abs(num-guess) < abs(num-st.session_state.guesses[-2]):
                    st.session_state.feedback = "warmer"
                else:
                    st.session_state.ffedback = "colder"
            else:
                if abs(num-guess) <=10:
                    st.session_state.feedback = "warm"
                else:
                    st.session_state.feedback = "cold"

if st.button("restart game")

                    
        
                        

