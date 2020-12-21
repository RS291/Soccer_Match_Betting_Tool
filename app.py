import streamlit as st
import pandas as pd
import sklearn
import pickle

st.title("Soccer Match Betting Tool")

st.header("A match result predictor for making educated gambling decisions.")

st.markdown("""<a href="https://projects.fivethirtyeight.com/global-club-soccer-rankings/">Real-time SPI Rankings</a>""",
            unsafe_allow_html=True)

st.subheader("Input match data below:")

spi1 = st.slider("What is the home team's ESPN SPI rating?", 
                 min_value=1, max_value=100)

spi2 = st.slider("What is the away team's ESPN SPI rating?",
                 min_value=1, max_value=100)

prob1 = st.slider("What are the bookmaker odds on the home team winning?",
                 min_value=0.001, max_value=1.000)

prob2 = st.slider("What are the bookmaker odds on the away team winning?",
                 min_value=0.001, max_value=1.000)

probtie = round((1.000 - (prob1 + prob2)), 3)

if st.button("Click here to run!"):
    st.subheader("Modeling match results off these SPIs and odds:")
    st.write(f"Home SPI: {spi1}")
    st.write(f"Away SPI: {spi2}")
    st.write(f"Bookmaker odds for home win: {prob1}")
    st.write(f"Bookmaker odds for away win: {prob2}")
    st.write(f"Bookmaker odds for tie: {probtie}")
    
    model = pickle.load(open('model.sav', 'rb'))
    
    data = pd.DataFrame(columns = ['spi1', 'spi2', 'prob1', 'prob2', 'probtie'])
    data = data.append({'spi1': spi1,
                        'spi2': spi2,
                        'prob1': prob1,
                        'prob2': prob2,
                        'probtie': probtie},
                       ignore_index=True)
    pred = model.predict(data)
    
    if pred[0] == 0:
        st.subheader("Predicted match result: Draw")
    elif pred[0] == 1:
            st.subheader("Predicted match result: Home Win")
    else:
        st.subheader("Predicted match result: Away Win")
            