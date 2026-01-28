import streamlit as st
from PIL import Image

st.title("미디어 입출력")
""
""

st.header('이미지 입력', divider='yellow')
image_input = st.camera_input('사진을 찍어주세요 :smile:')

if image_input:
    img = Image.open(image_input)
    st.image(img, width=500)


# 이미지 출력
st.header('이미지 출력', divider='yellow')
st.image("../../data/hamster.jpg", caption='로또 당첨 되게 해주세요...', width=500)

# 음성 출력
st.header('음성 출력', divider='yellow')
with open('../../data/clockbell.wav', 'rb') as f:
    audio_data = f.read()
st.audio(audio_data)

# 영상 출력
st.header('영상 출력', divider='yellow')
with open('../../data/wave.mp4', 'rb') as f:
    video_data = f.read()
st.video(video_data)
