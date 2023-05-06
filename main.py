from ver import verify
import time 

import streamlit as st
st.title('The Fury speaker reco')
st.text('ONLINE')

st.text('starting predition from main')
s  =  time.time()
v = verify()
e  =  time.time()
st.text(str(v))
st.text(f"with the time {str(e-s)} sec")