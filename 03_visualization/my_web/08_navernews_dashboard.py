
from bs4 import BeautifulSoup
import requests
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from PIL import Image
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()
client_id = os.getenv('NAVER_CLIENT_ID')
client_secret = os.getenv('NAVER_CLIENT_SECRET')

# 함수 설정: 네이버 검색 API를 활용한 뉴스 검색 결과를 반환해주는 함수
def get_requests(query, display, start):
    headers = {'X-Naver-Client-Id':client_id, 'X-Naver-Client-Secret': client_secret}

    params = {'query':query, 'dispaly':display, 'start':start}

    url = 'https://openapi.naver.com/v1/search/news.json'

    response = requests.get(url, headers=headers, params=params)

    news_json = json.loads(response.text)

    return news_json['items']


# 워드 클라우드 시각화 함수
def wc_chart(corpus, back_mask, max_words, emp):
    if back_mask == '타원':
        img = Image.open('../../data/background_1.png')
    elif back_mask == '말풍선':
        img = Image.open('../../data/background_2.png')
    else:
        img = Image.open('../../data/background_3.png')

    my_mask = np.array(img)

    wc = WordCloud(
        font_path = 'C:/Windows/Fonts/malgun.ttf',
        background_color = 'black',
        max_words = max_words,
        random_state = 99,
        stopwords = ['등', '있다', '및', '수', '이', 'the', 'a', 'of', 'to', 'in', 'and', 'said', 'was', 'by'],
        mask = my_mask
    )
    wc.generate(corpus) #corpus 말주머니?

    fig = plt.figure(figsize=(10,10))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    st.pyplot(fig)
    emp.success(':orange[**워드 클라우드 이미지 생성 완료**]', icon='✅')

# 세선 설정

if 'client_id' not in st.session_state:
    st.session_state['client_id'] = client_id

if 'client_secret' not in st.session_state:
    st.session_state['client_secret'] = client_secret


# 사이드바 설정

with st.sidebar.form(key='form1', clear_on_submit=False):
    st.header('네이버 API 설정')
    client_id = st.text_input('Client ID:', value=st.session_state['client_id'])
    client_secret = st.text_input('Client Secret:', value=st.session_state['client_secret'])

    if st.form_submit_button(label='OK'):
        st.session_state['client_id'] = client_id
        st.session_state['client_secret'] = client_secret
        st.write('설정 완료!')

# 메인화면 설정
chart_emp = st.empty()

try:
    with st.form(key='Search', clear_on_submit=False):
        search_keyword = st.selectbox('키워드:', ['경제', '정치', '사회', '국제', '연예', 'IT', '문화'])
        data_amount = st.slider('분량(1당 100개)', min_value=1, max_value=5, value=1, step=1)
        back_mask = st.radio('워드 클라우드 출력 형태:', ['기본', '타원', '말풍선', '하트'], horizontal=True)

        if st.form_submit_button('출력'):
            chart_emp.info(':red[데이터 가져오는 중...]')

            # 데이터 수집
            corpus = ''# 수집된 문자열이 담길 변수 선언
            items = []

            for i in range(data_amount):
                items.extend(get_requests(search_keyword, 100, 100*i+1))

            for item in items:
                if 'n.news.naver' in item['link']:
                    news_url = item['link']
                    response = requests.get(news_url)
                    soup = BeautifulSoup(response.text, 'lxml')
                    body_area = soup.select_one('#dic_area')
                    if body_area:
                        news_text_list = body_area.find_all(string=True, recursive=False)
                        news_text = "".join(text.strip() for text in news_text_list)
                        corpus += news_text + " "
            st.write(f'수집된 corpus 글자수: {len(corpus)}')


            # 워드 클라우드 생성
            if len(corpus) >= 100: # corpus 길이가 너무 짧으면 워드클라우드의 출력이 적절하지 않기 때문에 조건 설정
                chart_emp.info(':red[이미지 생성 중...]')
                wc_chart(corpus, back_mask, 70, chart_emp)
            else:
                chart_emp.error(':red[워드클라우드를 생성하기에 데이터가 충분하지 않습니다.]')
except Exception as e:
    st.write(e)
    chart_emp.error('ID와 Secret를 입력해주세요.')
