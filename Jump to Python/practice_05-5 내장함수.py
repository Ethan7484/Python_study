### divmod 
# divmod(a, b)는 2개의 숫자를 입력으로 받는다. 그리고 a를 b로 나눈 몫과 나머지를 튜플 형태로 돌려주는 함수이다. 
"""
a = divmod(7, 3)
print(a)    # 몫 = 2, 나머지 = 1
print( 7 // 3)    # 몫 = 2
print( 7 % 3 )    # 나머지 = 1
"""



### enumerate
# enumerate는 "열거하다"라는 뜻이다. 이 함수는 순서가 있는 자료형(리스트, 튜플, 문자열)을 입력으로 받아 인덱스 값을 포함하는 enumerate 객체를 돌려준다.
# >> 보통 enumerate 함수는 다음 예제처럼 for문과 함께 자주 사용한다.
# 잘 이해되지 않으면 다음 예를 보자.

"""
for i, name in enumerate(['body', 'foo', 'bar']):
    print(i, name)
0 body
1 foo
2 bar
"""
# 순서 값과 함께 body, foo, bar가 순서대로 출력되었다. 즉 위 예제와 같이 enumerate를 for문과 함께 사용하면 자료형의 현재 순서(index)와 그 값을 쉽게 알 수 있다.
# for문처럼 반복되는 구간에서 객체가 현재 어느 위치에 있는지 알려주는 인덱스 값이 필요할 때 enumerate 함수를 사용하면 매우 유용하다.



### eval - 와 이거 감이 잘 안온다 ㅋㅋ
# eval(expression)은 실행 가능한 문자열(1+2, 'hi' + 'a' 같은 것)을 입력으로 받아 문자열을 실행한 결괏값을 돌려주는 함수이다.

"""
a = eval('1+2')
print(a)
b = eval("'hi' + 'a'")
print(b)
c = eval('divmod(4, 3)')
print(c)
"""
# 보통 eval은 입력받은 문자열로 파이썬 함수나 클래스를 동적으로 실행하고 싶을 때 사용한다.



### filter
# filter란 무엇인가를 걸러낸다는 뜻으로 filter 함수도 동일한 의미를 가진다.
# filter 함수는 첫 번째 인수로 함수 이름을, 두 번째 인수로 그 함수에 차례로 들어갈 반복 가능한 자료형을 받는다. 
# 그리고 두 번째 인수인 반복 가능한 자료형 요소가 첫 번째 인수인 함수에 입력되었을 때 반환 값이 참이 것만 묶어서(걸래내서) 돌려준다.
# 다음 예를 보자.

"""
# positive.py
def positive(l):
    result = []
    for i in l:
        if i > 0:
            result.append(i)
    return result

print(positive([1, -3, 2, 0, -5, 6]))    # 결괏값 [1, 2, 6]
"""

# 즉 위에서 만든 positive 함수는 리스트를 입력값으로 받아 각각의 요소를 판별해서 양수 값만 돌려주는 함수이다.
# filter 함수를 사용하면 위 내용을 다음과 같이 간단하게 작성할 수 있다.

"""
# filter1.py
def positive(x):
    return x > 0

print(list(filter(positive, [1, -3, 2, 0, -5, 6])))    # 결괏값 [1, 2, 6]
"""
# 여기에서는 두 번째 인수인 리스트의 요소들이 첫 번째 인수인 positive 함수에 입력되었을 때 반환 값이 참인 것만 묶어서 돌려준다.
# 앞의 예에서는 1, 2, 6만 양수여서 x > 0 문장이 참이되므로 [1, 2, 6]이라는 결괏값을 돌려주게 된 것이다.

# 앞의 함수는 lambda를 사용하면 더욱 간편하게 코드를 작성할 수 있다.
"""
a = list(filter(lambda x: x> 0, [1, -3, 2, 0 , -5, 6]))
print(a)    # 결괏값 [1, 2, 6]
"""



### hex
# hex(x)는 정수 값을 입력받아 16진수(hexadecimal)로 변환하여 돌려주는 함수이다.

"""
print(hex(234))    # 0xea
print(hex(3))    # 0x3
"""



### id
# id(object)는 객체를 입력받아 객체의 고유 주소 값(레퍼런스)을 돌려주는 함수이다.

"""
a = 3
print(id(3))    # 140733924509408
print(id(a))    # 140733924509408
b = a
print(id(b))    # 140733924509408
"""

# 위 예의 3, a, b는 고유 주소 값이 모두 140733924509408이다. 즉 3, a, b가 모두 같은 객체를 가리키고 있다.
# 만약 id(4)라고 입력하면 4는 3, a, b와 다른 객체이므로 당연히 다른 고유 주소 값이 출력된다.
"""
print(id(4))    # 140732587050752
"""



### input
# input([prompt])은 사용자 입력을 받는 함수이다. 매개변수로 문자열을 주면 다음 세 번째 예에서 볼 수 있듯이 그 문자열은 프롬프트가 된다.
# >> [] 기호는 괄호 안의 내용을 생략할 수 있다는 관례 표기법임을 기억하자.

"""
a = input("Enter: ")
print(a)
"""



### int
# int(x)는 문자열 형태의 숫자나 소수점이 있는 숫자 등을 형태로 돌려주는 함수로, 정수를 입력으로 받으면 그대로 돌려준다.
"""
print(int('3'))    # 3
print(int(3.4))    # 3
"""
# int(x, radix)는 radix 진수로 표현된 문자열 x를 10진수로 변환하여 돌려준다.
# 2진수로 표현된 11의 10진수 값은 다음과 같이 구한다.
"""
print(int('11', 2))    # 3
"""
# 16진수로 표현된 1A의 10진수 값은 다음과 같이 구한다.
"""
print(int('1A', 16))    # 26
"""



### isinstance
# isinstance(object, class)는 첫 번째 인수로 인스턴스, 두 번째 인수로 클래스 이름을 받는다. 입력으로 받은 인스턴스가 그 클래스의 인스턴스인지를 판단하여 참이면 True, 거짓이면 False를 돌려준다.

"""
class Person: pass
class person: pass

a = Person()
b = isinstance(a, Person)    # True
print(b)
"""
# 위 예는 a가 Person 클래스가 만든 인스턴스임을 확인시켜 준다.
"""
A = 3
c = isinstance(A, Person)    # False
print(c)
"""
# 위 예는 Person 클래스가 만든 인스턴스가 아니므로 False를 돌려준다.



### len
# len(s)은 입력값 s의 길이(요소의 전체 개수)를 돌려주는 함수이다.
"""
print(len("Python"))    # 6
print(len([1, 2, 3]))    # 3
print(len((1, 'a')))     # 2
"""



###  list
# list(s)는 반복 가능한 자료형 s를 입력받아 리스트로 만들어 돌려주는 함수이다.
"""
print(list("Python"))    # ['P', 'y', 't', 'h', 'o', 'n']
print(list((1, 2, 3)))    # [1, 2, 3]
"""
# list 함수에 리스트를 입력으로 주면 똑같은 리스트를 복사하여 돌려준다.
"""
a = [1, 2, 3]
b = list(a)
print(b)    # [1, 2, 3]
"""



### map
# map(f, iterable)은 함수(f)와 반복 가능한(iterable) 자료형을 입력으로 받는다.  map은 입력받은 자료형의 각 요소를 함수 f가 수행한 결과를 묶어서 돌려주는 함수이다.
# 다음 예를 보자

"""
# two_times.py
def two_times(numberList):
    result = [ ]
    for number in numberList:
        result.append(number*2)
    return result

result = two_times([1, 2, 3, 4])
print(result)
"""
# two_times 함수는 리스트 요소를 입력받아 각 요소에 2를 곱한 결괏값을 돌려준다. 실행 결과는 다음과 같다.
# >> 결괏값 [2, 4, 6, 8]
# 위 예제는 map 함수를 사용하면 다음처럼 바꿀 수 있다.

def two_times(x):
    return x*2

print(list(map(two_times, [1, 2, 3, 4])))    # [2, 4, 6, 8]
# 이제 앞 예제를 해석해보자. 먼저 리스트의 첫 번째 요소인 1이 two_times 함수의 입력값으로 들어가고 "1*2"의 과정을 거쳐서 2가 된다.
# 다음으로 리스트의 두 번째 요소인 "2*2"의 과정을 거쳐 4가 된다. 따라서 결괏값 리스트를 이제 [2, 4]가 된다. 총 4개의 요솟값이 모두 수행되면 마지막으로 [2, 4, 6, 8]을 돌려준다.
# 이것이 map 함수가 하는 일이다. 
# >> 위 예에서 map의 결과를 리스트로 보여주기 위해 List 함수를 사용하여 출력하였다.