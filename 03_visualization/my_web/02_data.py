import streamlit as st
import pandas as pd

st.title('📌Data 출력 방식')
""
""

# df생성

df = pd.DataFrame({
    'col1':[1,2,3],
    'col2':['a','b','c'],
    'col3':[True,False,True]
})

df
""

st.write(df)

st.table(df)

st.json([
    {'name':'희윤', 'age':26, 'gender':'female'},
    {'name':'재찬', 'age':26, 'gender':'male'}
])

st.metric(label='온도', value='10°c', delta='1.2') # alt + 0176
st.metric(label='삼성전자', value='61,000', delta="+1,000")
st.metric(label='삼성전자', value='61,000', delta='-1,200')
st.metric(label='현재 사용자', value='25,000')
