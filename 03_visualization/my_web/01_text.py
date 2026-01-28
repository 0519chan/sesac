import streamlit as st
import pandas as pd

# 타이틀 출력"
st.title('지금 아주 졸려요 - 대')

st.header('조금 깼어요 - 중')

st.subheader('목이 아파요 - 소')
st.subheader('도넛 뭐 먹지 - 소', divider=True)
st.subheader('금액은?', divider='red' )

"" # 공백 추가

# 일반 텍스트 출력 (단순 텍스트 출력용)
st.text("간단한 텍스트 출력")

# 마크다운 출력
st.markdown("*마크다운* 출력") # italic 적용
st.markdown('**마크다운**') # bold 적용
st.markdown('[마크다운](https://blog.naver.com/anthouse28/221210836545)')
st.markdown(':smile: :100: :ocean:') # 이모지 적용

st.markdown('마크다운 :red[**색상**] 적용')
st.markdown('마크다운 :blue[**색상**] 적용')

'마크다운 :green[**색상**] 적용'

""

# 파이썬 객체 출력
x, y = 1, 2

st.write(1,2)
st.write('x= ',x, "그리고", 'y= ',y)
st.write(f'x={x}, y={y}') # 문자로 인식
# st.text('x=',x) -> text 메소드는 str값만 전달 가능하며 추가적인 매개변수 또는 파이썬 객체는 전달 불가능

st.latex('E = mc^2')
st.latex(r'Area = \pi r^2\ 입니다')

# 캡션

st.caption('짧은 설명')

# 이모티콘 출력

"썬글라스 -> :sunglasses:"
"붐업 -> :+1:"
"웃음 -> :smile:"
