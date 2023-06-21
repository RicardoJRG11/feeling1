import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt

st.subheader('WordCloud App')
st.set_option('deprecation.showPyplotGlobalUse', False)
text = st.text_input('Enter text and press enter')
if text:
    w = WordCloud().generate(text)

    plt.imshow(w)
    plt.axis('off')
    st.pyplot()
