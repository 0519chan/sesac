import streamlit as st
import pandas as pd
import time

st.title('나만의 작고 소중한 대시보드')
st.header('실습 예제 작성중!')
st.write('이 대시보드는 streamlit을 활용하여 만들어졌습니다.')
st.markdown('이곳에서는 다양한 *Streamlit* 함수를 활용할 수 있습니다. [여기](https://docs.streamlit.io/)를 클릭하세여 더 알아보세요.')

"---"

data_df = pd.DataFrame({
    "상품": ["A", "B", "C", "D"],
    "판매량": [100, 150, 200, 50],
    "작년대비 증감비": ["+10%", "+5%", "+7%", "-15%"]
})

st.table(data_df)
max_row = data_df.loc[data_df['판매량'].idxmax()]
max_sales = max_row['판매량']
max_delta = max_row['작년대비 증감비']

st.metric(label='최대판매량', value=max_sales, delta=max_delta)

select = st.selectbox(label='어떤 상품을 보시겠습니가?', options=data_df['상품'], key='product')

selected_data = int(data_df.loc[data_df['상품'] == select, '판매량'].iloc[0])
st.write(f'{select}의 판매량은 {selected_data}입니다.')

st.markdown("---")
st.latex(r"l = 2\pi r")

"---"
st.header('냥이!')
st.image("../../data/hamster.jpg", caption='냥이 이미지', width=200)

"---"
code_basic = """\
    print('Hello, Streamlit!')\
"""

st.code(code_basic)
st.warning('이 텍스트는 경고용 메시지입니다')

"---"
if st.button(label='성공 버튼', key='success_btn'):
    st.success('성공!')

"---"
name_input = st.text_input('이름을 입력하세요:')
st.write(f'안녕하세요, {name_input}님!')

"---"
st.write('색상을 선택하세요')
color_basic = st.color_picker('색상을 선택하세요', key='color_pic_basic')
st.write(f'선택한 색상은 {color_basic}입니다.')

"---"
if st.button('진행버튼', key='prog_btn'):
    progress_bar = st.progress(0)
    for i in range(0,101,10):
        progress_bar.progress(i)
        time.sleep(1)


