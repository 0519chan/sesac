import streamlit as st
import time
import pandas as pd
import numpy as np

@st.cache_data
def load_df():
    time.sleep(2) 

    df = pd.DataFrame({
        'co1': np.random.randn(100),
        'co2': np.random.randn(100)
    })

    return df


if st.button('데이터불러오기', key='load_df'):
    df = load_df()
    st.write('데이터 로드 완료')
    st.write(df)


st.markdown("---")
st.subheader(" @cache_data 예제2")

@st.cache_data
def get_data(age):
    my_dict = {'name':['최희윤'], 'age':[age], 'gender':['female']}
    df = pd.DataFrame(my_dict)
    time.sleep(3)

    return df

# 나이를 전달할 input widget 설정
age = st.number_input('나이를 입력해주세요:', min_value=0, max_value=100, value=50, step=1)

if st.button('데이터 불러오기', key='load_df2'):
    df = get_data(age)
    st.success('데이터 로드 완료')
    st.write(df)


st.markdown('---')

st.subheader('모든 캐시 삭제')

if st.button('모든 캐시 삭제', key='cache_clear'):
    st.cache_data.clear()
    st.success('모든 캐시가 삭제')

# 삭제할 함수 선택

selected_function = st.selectbox('캐시를 삭제할 함수를 선택하세요:', options=['load_df()', 'get_data()'], placeholder='Choose an Option')
if st.button('캐시 삭제'):
    if selected_function == 'load_df()':
        load_df.clear()
    else:
        get_data.clear()

    st.success(f'{selected_function}의 캐시 삭제 완료')
