# 1. module 실행 & import 해보기
print('calc 모듈을 import 했습니다.')

# 2. 변수 생성 및 import
name = 'calculator'

def add(a, b):
    return a+b

def sub(a, b):
    return a-b

def dup(a, b):
    return a*b

def div(a, b):
    return a/b


# 4. __name__ 확인해보기
print(f'calc 모듈 이름: {__name__}')