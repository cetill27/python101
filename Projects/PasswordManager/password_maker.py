import streamlit as st
import string
import random

st.title("🔑 Password Manager")
length = st.number_input("Enter the password length", min_value=4, max_value=50, value=8)
count = st.number_input("How many passwords", min_value=1, max_value=10, value=1)

characters = string.ascii_letters + string.digits + string.punctuation

for i in range(count):
    password = ""

    for j in range(length):
        password +=random.choice(characters)
    st.write("Password" , i+1, ":",password)