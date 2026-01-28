import streamlit as st


st.header('아래는 `.code()` 함수에 대한 예시', divider='yellow')

st.write("1. `.code()` 예제1")
my_code = """\
    total = 0
    for i in range(5):
        total += 1
    print(total)\

"""

my_code2 = """\
    def my_functions():
        print('hellow')\
"""

st.code(my_code)
st.code(my_code2)


# 예제2

st.write('1. `.code()` 예제2')
def get_user_name():
    return 'John'
def get_punctuation():
    return '!!!'

st.code(get_user_name())
st.code(get_punctuation())

st.header('아래는 `.echo()` 함수에 대한 예시', divider='yellow')

st.write('1. 아래 부분의 함수 정의부는 화면에 출력되지 않음')

st.write('1. `.code()` 예제2')
def get_user_name():
    return 'John'
def get_punctuation():
    return '!!!'

user_name = get_user_name()
punctuation = get_punctuation()
greeting = 'Hi, there!'

st.write(user_name, punctuation)

st.write("--DONE!--")
""
""

# 예제2
st.write("2. 아래 코드는 함수의 정의부까지 모두 화면에 출력됨")
with st.echo():
    # 이 코드블럭 내의 모든 코드는 화면에 출력되고 실행됨
    user_name = get_user_name()
    punctuation = get_punctuation()
    greeting = 'Hi, there!'

    st.write(user_name, punctuation)


