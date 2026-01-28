import streamlit as st
import pandas as pd
import datetime
import time

st.subheader('버튼', divider='yellow')
st.button(label='클릭', key='btn1')
st.button(label='클릭', key='btn2')

def my_btn(*args):
    total = sum(args)
    st.write(f"합계: {total}")

# 버튼 동작 방법1: on_click 매개변수 사용
st.button('제출1', key='btn3', on_click=my_btn, args=(1,2,3,4))

# 버튼 동작 방법2: 조건문 사용
if st.button('제출2', key='btn4'):
    my_btn(1,2,3,4)


st.subheader('체크박스', divider='yellow')

st.checkbox('위 내용에 동의합니다')

check_box = st.checkbox('위 내용에 동의합니다2')

st.write(check_box) # 반환값: bool 체크시 True

st.subheader('라디오 박스', divider='yellow')

st.radio(label='다음 중 한 가지를 선택하시오 1', options=['통장에 매일 5만원 입금', '지금 바로 2억원 입금'], key='radio')

select_result = st.radio(label='다음 중 한 가지를 선택하시오 2', options=['통장에 매일 5만원 입금', '지금 바로 2억원 입금'], key='radio2')

st.write(select_result)




# ------------------------------------------------

st.subheader('선택박스', divider='yellow')

st.selectbox(label='다음 중 한 가지를 선택하시오 1', options=['통장에 매일 5만원 입금', '지금 바로 2억원 입금'], key='radio3')
select = st.selectbox(label='다음 중 한 가지를 선택하시오 1', options=['통장에 매일 5만원 입금', '지금 바로 2억원 입금'], key='radio4')


st.write(select)


# ------------------------------------------------

st.subheader('다중선택박스', divider='yellow')

st.multiselect(label='오늘 야식은?', options=['치킨', '피자', '햄버거'], key='multi1')
mul_select = st.multiselect(label='오늘 야식은?', options=['치킨', '피자', '햄버거'], key='multi2')


st.write(mul_select)

# -----------------------------

st.subheader('컬러선택', divider='yellow')

st.color_picker('색상을 선택하세요 1', key='color_pic1')
c = st.color_picker('색상을 선택하세요 2', key='color_pic2')
st.write(f'색상 결과 : {c}')




""
#----------------------------------

st.subheader('슬라이더', divider='yellow')

slider = st.slider('추천 점수', min_value=0, max_value=10, value=5, step=2)
st.write(f'slideer 결과: {slider}')
st.write(type(slider))



#----------------------------------

st.subheader('숫자 입력', divider='yellow')

num_input = st.number_input('점수', min_value=0, max_value=100, value=10, step=10)
st.write(num_input)

#----------------------------------

st.subheader('각종 데이터 입력', divider='yellow')

text = st.text_input('이름:')
date = st.date_input('생일:', max_value=datetime.datetime.now())
time_input = st.time_input('태어난 시간:', step=datetime.timedelta(hours=1))

st.write(f'이름:{text}, 생일:{date}, 시간:{time_input}')



#----------------------------------
import time 

st.subheader('진행 상태 바', divider='yellow')

st.progress(30, text='30%')

progress_bar = st.progress(0)

if st.button('진행', key='btn5'):
    for i in range(0,101,25):
        progress_bar.progress(i, text=f'{i}%')
        time.sleep(1)



# ----------------------------------------------------
st.subheader('spinner', divider='yellow')

if st.button('진행', key='btn6'):
    with st.spinner('실행중...'):
        time.sleep(3)
        st.success('종료', icon='✅')



#----------------------------------------------------------
st.subheader('상태메세지', divider='yellow')
st.success('성공!', icon='✅')
st.error("오류 메세지:", icon='😒')
st.warning('경고!', icon='⚠️')
st.info('정보: ', icon='📋')
