import requests
import streamlit as st

st.title("💰 Crypto Price Tracker")

coin = st.selectbox(
    "Choose a cryptocurrency",
    ["bitcoin", "ethereum", "dogecoin"]
)



url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd"

response = requests.get(url)

data = response.json()

if coin in data:
    price = data[coin]["usd"]
    st.success(f"{coin.capitalize()} price: ${price}")
else:
    st.error("Could not fetch price. Try again.")