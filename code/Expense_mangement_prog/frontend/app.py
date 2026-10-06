from datetime import datetime
import requests
import streamlit as st
from add_update_tab import add_update_tab_function

API_URL = "http://127.0.0.1:8000"

st.title('Expense Management App')

tab1,tab2 = st.tabs(["Add/Update","Analytics"])
with tab1:
    add_update_tab_function(tab1)

with tab2:
    