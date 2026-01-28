import streamlit as st

tab1, tab2 = st.tabs(['좌측 탭', '우측 탭'])


with tab1:
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

