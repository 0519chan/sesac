
import streamlit as st
import pandas as pd
import time

st.title('나만의 대시보드')
st.header('실습 예제 작성')


st.write('이 대시보드는 Streamlit을 활용하여 만들어졌습니다.')

st.markdown('이곳에서는 다양한 *Streamlit* 함수를 활용할 수 있습니다. [여기](https://www.naver.com)를 클릭해보세요')

st.markdown('---')

df = pd.DataFrame({
    '상품':['A', 'B', 'C', 'D'],
    '판매량':[100, 150, 1200, 50],
    '작년대비 증감비':["+10%", "+5%", '+7%', '-15%']
})


#df
#st.dataframe(df)
st.table(df)

# metric
max_row = df.loc[df['판매량'].idxmax()]
max_sales = int(max_row['판매량'])
max_delta = str(max_row['작년대비 증감비'])


# 2. value와 delta를 각각 metric 메소드에 전달
st.metric('최대 판매량', max_sales, max_delta)

# selectbox
selected = st.selectbox('어떤 상품의 정보를 보시겠습니까?', options=df['상품'], index=0)
selected_sales = int(df.loc[df['상품'] == selected, '판매량'])

st.write(f'{selected}의 판매량은 {selected_sales}입니다.')

st.markdown("---")
st.header('햄스터')

st.image('../../data/hamster.jpg', width=200, caption='Cute')

st.warning('이 텍스트는 경고용')

st.markdown('---')

if st.button('성공 버튼'):
    st.balloons()
    st.success('성공입니다.')


st.markdown('---')
name = st.text_input('이름을 입력하세요:')
st.write(f'안녕하세요, {name}님!')

# 진행버튼

if st.button('진행버튼', key='p_btn'):
    progress_bar = st.progress(0)

    for x in range(0, 101, 10):
        progress_bar.progress(x)
        time.sleep(1)
