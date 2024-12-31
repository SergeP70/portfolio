import streamlit as st

st.header("Contact Us")

with st.form(key='frm_email'):
    txt_email = st.text_input("Your email address:")
    txt_message = st.text_area("Your message")
    btn_email = st.form_submit_button()
    if btn_email:
        print("Button was pressed")
        