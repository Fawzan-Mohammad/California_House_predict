import streamlit as st

pg = st.navigation([
    st.Page("app.py", title="Home", icon=":material/home:", default=True),
    st.Page("pages/01_about_us.py", icon=":material/info:", title ="About Us"),
    st.Page("pages/02_terms_of_use.py", icon=":material/policy:", title="Terms Of Use"),
    
])
pg.run()







