import streamlit as st
import mailer

st.header("Contact Us")

with st.form(key='frm_email'):
    txt_email = st.text_input("Your email address:")
    txt_message = st.text_area("Your message")
    txt_subject = "Mail from my Portfolio App"
    btn_email = st.form_submit_button()
    if btn_email:
        print("Button was pressed")
        print(btn_email)
        print(txt_email)
        print(txt_message)
        mailer.send(txt_email, txt_subject, txt_message)
        st.info("Your email was sent successfully")
