# https://wikidocs.net/42528

"""
Q1
주어진 자연수가 홀수인지 짝수인지 판별해주는 함수 (is_odd)를 작성해보자.
"""
# A1
def in_odd(a):
    if a < 0:
        print("자연수가 아닙니다.")
    elif a % 2 == 0:
        print("짝수 입니다.")
    else:
        print("홀수 입니다.")
in_odd(5)


"""
Q2
입력으로 들어오는 모든 수의 평균 값을 계산해 주는 함수를 작성해 보자.
(단, 입력으로 들어오는 수릐 개수는 정해져 있지 않다.)
* 평균 값을 구할 때 len 함수를 사용해 보자
"""
# A2
def a2(*args):
    result = 0
    for i in args:
        result = result + i
    return print(result/len(args))
a2(1,5)


"""
Q3
다음은 두 개의 숫자를 입력받아 더하여 돌려주는 프로그램이다.

input1 = input("첫번째 숫자를 입력하세요:")
input2 = input("두번째 숫자를 입력하세요:")

total = input1 + input2
print("두 수의 합은 %s 입니다" % total)
이 프로그램을 수행해 보자.

첫번째 숫자를 입력하세요:3
두번째 숫자를 입력하세요:6
두 수의 합은 36 입니다
3과 6을 입력했을 때 9가 아닌 36이라는 결괏값을 돌려주었다. 이 프로그램의 오류를 수정해 보자.

※ int 함수를 사용해 보자.
"""