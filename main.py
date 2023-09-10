import streamlit as st
import time

st.title('Stream 入門')

#progress
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!!!'    

#expander
expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ')
expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせ')














