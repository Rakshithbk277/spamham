import streamlit as st
import joblib
st.title('SPAM HAM CLASSIFIER')
text_model = joblib.load('spam-ham')
ip = st.text_input('enter your message')
op = text_model.predict([ip])
if st.button('predict'):
  st.title(op[0])
  
 
