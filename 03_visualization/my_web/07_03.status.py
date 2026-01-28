import streamlit as st

st.title('Seession 예제')

""

st.write('### 현재 세션 상태 session_state 상태 확인')
st.write(st.session_state)



""

st.write('### 현재 세션 상태 session_state에 cnt 추가')

if 'cnt' not in st.session_state:
    st.session_state['cnt'] = 0
st.write(st.session_state)

st.write('button 클릭 시 session 상태가 어떻게 바뀌는지 확인')

col1, col2, col3 = st.columns(3)

if col1.button('1 증가', key='btn_1'):
    st.session_state['cnt'] += 1

if col2.button('1 감소', key='btn_2'):
    st.session_state['cnt'] -= 1

if col3.button('초기화', key='btn_3'):
    st.session_state['cnt'] = 0 


st.write(f'현재 cnt: {st.session_state["cnt"]}')
st.write(st.session_state)

# form을 생성하여 값을 제출할 땐 session 상태가 어떻게 바뀌는지 확인
st.write('button 클릭 시 session 상태가 어떻게 바뀌는지 확인')

st.write('제출을 누르면 초기화 되는 경우')

if st.button('폼 열기', key='btn_4'):
    with st.form(key='form1', clear_on_submit=True):
        name1 = st.text_input('이름을 입력하세요', key='text_input1')
        age1 = st.number_input('나이를 입력하세요', min_value=0, max_value=100, value=50, step=1, key='num_input1')
        gender1 = st.radio('성별은 선택하세요', ['male', 'female'], key='radio1')


        if st.form_submit_button('제출'):
            st.write(f'제출 결과: 이름:{name1}, 나이:{age1}, gender:{gender1}')



st.write('제출을 누르면 초기회 안 되는 경우')

def doc_clicked():
    return st.session_state.get('clicked', False)

if doc_clicked():
    with st.form(key='form2', clear_on_submit=False):
        name2 = st.text_input('이름을 입력하세요', key='text_input2')
        age2 = st.number_input('나이를 입력하세요', min_value=0, max_value=100, value=50, step=1, key='num_input2')
        gender2 = st.radio('성별은 선택하세요', ['male', 'female'], key='radio2')

else:   
    if st.button('폼 열기', key='btn_5'):
        st.session_state['clicked'] = True
        st.return()


