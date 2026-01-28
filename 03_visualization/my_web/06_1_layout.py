import streamlit as st
import time

# -------------------------------side bar------------------------------------------#

with st.sidebar:
    st.title('야식 선택')
    multi_select = st.multiselect('오늘 야식은?', options=['치킨','피자','햄버거'])
    multi_select = ", ".join(multi_select)
    st.write(f"결과: {multi_select}")


"---"

st.title('spinner')
if st.button('진행'):
    with st.spinner('데이터 전달 중 ...'):
        time.sleep(3)
        st.success('전달 완료')


# -------------------------------columns------------------------------------------#

col1, col2, col3 = st.columns(3)

with col1:
    st.header('칼럼1', divider = 'red')
    st.image('../../data/hamster.jpg', caption='cute')

with col2:
    st.header('칼럼2', divider = 'green')
    st.image('../../data/hamster.jpg', caption='cute')

with col3:
    st.header('칼럼3', divider = 'rainbow')
    st.image('../../data/hamster.jpg', caption='cute')
