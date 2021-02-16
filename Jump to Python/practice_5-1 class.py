# 여러분 모두 계산기를 사용해 보았을 것이다. 계산기에 숫자 3을 입력하고 + 기호를 입력한 후 4를 입력하면 결괏값으로 7을 보여 준다. 
# 다시 한 번 + 기호를 입력한 후 3을 입력하면 기존 결괏값 7에 3을 더해 10을 보여 준다. 
# 즉 계산기는 이전에 계산한 결괏값을 항상 메모리 어딘가에 저장하고 있어야 한다

# 이런 내용을 우리가 앞에서 익힌 하무를 이용해 구현해 보자. 계산기의 "더하기" 기능을 구현한 파이썬 코드는 다음과 같다.

"""
result = 0

def add(num):
    global result
    result += num
    return result

print(add(3))
print(add(4))
"""

# * add 함수는 매개변수 num에 받은 값을 이전에 계산한 결괏값에 더한 후 돌려주는 함수이다.
# 이전에 계산한 결괏값을 유지하기 위해서 result 전역 변수(global)을 사용했다. 프로그램을 실행하면 예상한 대로 다음과 같은 결괏값이 출력된다.

# 그런데 만일 한 프로그램에서 2대의 계산기가 필요한 상황이면 어떻게 해야 할까?
# 각 계산기는 각각의 결괏값을 유지해야 하기 때문에 위와 같이 add 함수 하나만으로는 결괏값을 유지할 수 없다.
# 이런 상황을 해결하려면 다음과 같이 함수를 각각 따로 만들어야 한다.

"""
result1 = 0
result2 = 0

def add1(num):
    global result1
    result1 += num
    return result1

def add2(num):
    global result2
    result2 += num
    return result2

print(add1(3))
print(add1(4))
print(add2(5))
print(add2(10))
"""

# 똑같은 일을 하는 add1과 add2 함수를 만들었고 각 함수에서 계산한 결괏값을 유지하면서 저장하는 전역 변수 result1, result2가 필요하게 되었다.
# 결괏값은 다음과 같이 의대한 대로 출력된다.

# 계산기 1의 결괏값이 계산기 2에 아무 영향을 끼치지 않음을 확인할 수 있다. 하지만 계산기가 3개, 5개, 10개로 점점 더 많이 필요해진다면 어떻게 해야 할까?
# 그때마다 전역 변수와 함수를 추가할 것인가? 여기에 빼기나 곱하기 등의 기능을 추가해야 한다면 상황은 점점 더 어려워질 것이다.
# 아직 클래스에 대해 배우지 않았지만, 위와 같은 경우에 클래스를 사용하면 다음과 같이 간단하게 해결할 수 있다.

"""
class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()
cal3 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(10))
"""



### 사칙연산 클래스 만들기
"""
클래스를 어떻게 만들지 먼저 구상하기
"""
# 사칙연산을 가능하게 하는 FourCal 클래스가 다음처럼 동작한다고 가정해 보자.

"""
클래스 구조 만들기
"""
class FourCal:
    pass
a = FourCal()

"""
객체에 숫자 지정할 수 있게 만들기
"""
# a.setdata(4, 2)과 같이 연산을 수행할 대상(4, 2)을 객체에 지정할 수 있게 만들어 보자.
# 위 문장을 수행하려면 다음과 같이 소스 코드를 작성해야 한다.
class Fourcal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
# 앞에서 만든 Fourcal 클래스에서 pass 문장을 삭제하고 그 대신 setdata 함수를 만들었다. 클래스 안에 구현된 함수는 다른 말로
# 메서드(Method)라고 부른다. 앞으로 클래스 내부의 함수는 항상 메서드라고 표현할테니 메서드라는 용어를 기억해두자.
# 일반적인 함수를 만들 때 다음과 같이 작성한다. 
"""
def 함수명(매개변수):
    수행할 문장
"""

