import streamlit as st
import time

# -------------------------------Expander------------------------------------------#
st.subheader('Expander')

with st.expander('Expander 공간 1'):
    st.write('햄스터1')
    st.image('../../data/hamster.jpg', width = 300)


with st.expander('Expander 공간 2'):
    st.write('햄스터2')
    st.image('../../data/hamster.jpg', width = 300)


""
"---"
# -------------------------------empty------------------------------------------#
st.subheader('empty')

empty = st.empty()
empty.write('여기는 empty 공간입니다.')

c1, c2 = st.columns(2)
start_btn = c1.button('시작', key='empty_start')
clear_btn = c2.button('초기화', key='clear_start')

# 시작 버튼 클릭 시, empty 공간에 카운트다운이 1초 간격으로 진행
if start_btn:
    with empty:
        for i in range(6):
            cnt = 5 - i
            st.write(f":red[{cnt}]초 남았습니다.")
            time.sleep(1)
        st.write('empty 내부 카운트다운 실행 완료')


if clear_btn:
    empty.empty()
    empty.write('초기화 중입니다.')
    time.sleep(2)

    empty.write('empty 공간 초기화 완료')
    time.sleep(2)

    empty.write('empty.write() 작성 예시입니다.')
    st.write('st.write() 작성 예시입니다.')


""
"---"
# -------------------------------container------------------------------------------#
st.subheader('container')

cont = st.container()
cont.write('여기는 container 공간입니다.')

# container 외부 공간
c1, c2 = st.columns(2)

start_btn_c = c1.button('시작', key='const_start')
clear_btn_c = c2.button('초기화', key='const_clear')

if start_btn_c:
    with cont:
        for i in range(6):
            cnt = 5 - i
            st.write(f":red[{cnt}]초 남았습니다.")
            time.sleep(1)
        st.write('container 내부 카운트다운 실행 완료')


if clear_btn_c:
    cont.container()
    cont.write('초기화 중입니다.')
    time.sleep(2)

    cont.write('empty 공간 초기화 완료')
    time.sleep(2)

    cont.write('empty.write() 작성 예시입니다.')
    st.write('st.write() 작성 예시입니다.')
