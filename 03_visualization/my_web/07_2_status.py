import streamlit as st
import numpy as np
import pandas as pd
import time 

st.title('Form 예제')

# 함수 생성
@st.cache_data
def get_data(name, age, gender):
    my_dict = {'name':[name], 'age':[age], 'gender':[gender]}
    df = pd.DataFrame(my_dict)
    time.sleep(3)

    return df

st.markdown('---')


st.header('폼 미적용')

name1 = st.text_input('이름을 입력하세요')
age1 = st.number_input('나이를 입력하세요', min_value=0, max_value=100, value=50, step=1)
gender1 = st.radio('성별은 선택하세요', ['male', 'female'])

st.write(get_data(name1, age1, gender1))

with st.form(key='form1', clear_on_submit=True):
    name2 = st.text_input('이름을 입력하세요')
    age2 = st.number_input('나이를 입력하세요')
    gender2 = st.radio('성별을 선택하세요', ['male', 'female'])

    if st.form_submit_button('제출하기'):
        st.write(get_data(name2, age2, gender2))
