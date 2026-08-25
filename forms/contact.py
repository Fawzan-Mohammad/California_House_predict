import email
from os import name
from urllib import response

import streamlit as st
import re
import requests

WEBHOOK_URL = "https://connect.pabbly.com/webhook-listener/webhook/IjU3NjMwNTZjMDYzMTA0MzU1MjY0NTUzNSI_3D_pc/IjU3NjcwNTY4MDYzNjA0MzU1MjY1NTUzMDUxMzEi_pc"

def validate_email(email):
    # Regular expression for validating an Email
    regex = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.fullmatch(regex, email):
        return True
    else:
        return False

def contact_form():
    st.write("Please fill out the form below to get in touch with us.")
    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    text_area = st.text_area("Message")
    submit_button = st.button("Submit", key="submit-button")

    if submit_button:
        if WEBHOOK_URL =="":
            st.error("We are currently unable to send messages. Please try again later.")
            st.stop()
        elif name == "":
            st.error("Please enter your name.")
        elif email == "":
            st.error("Please enter your email address.")
        elif validate_email(email) != True:
            st.error("Please enter a valid email address.")
        else:
        # PREPARE THE DATA TO BE SENT
            data = {"name": name, "email":email, "message":text_area}
            response = requests.post(WEBHOOK_URL, json=data)

            if response.status_code == 200:
                st.success("Your message have been successfully sent")
            else:
                st.error("There was an error sending your message. Please try again later.")











