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
class FourCal:
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
"""
def setdata(self, first, second):    # 1 메서드의 매개변수
    self.first = first               # 2 메서드의 수행문
    self.second = second             # 3 메서드의 수행문
"""
# 1 setdata 메서드의 매개변수
# setdata 메서드는 맥개 변수로 self, first, second 3개 입력값을 받는다. 그런데 일반 함수와는 달리 메서드의 첫 번째 맥개변수 self는 특별한 의미를 가진다.
# 다으뫄 같이 a 객체를 만들고 a 객체를 통해 setdata 메서드를 호출해보자.
a = FourCal()
a.setdata(4, 2)
# 그런데 뭔가 좀 이상하지 않은가? setdata 메서드에는 sefl, first, second 총 3개의 매개변수가 필요한데 실제로는 "a.setdata(4, 2)"처럼 2개 값만 전달했다.
# 왜 그럴까? 그 이유는 "a.setdata(4, 2)"처럼 호출하면 setdata 메서드의 첫번째 매개변수 self에는 setdata메서드를 호출한 객체 a가 자동으로 전달되기 때문이다.
# 파이썬 메서드의 첫 번째 매개변수 이름은 관례적으로 self를 사용한다. 객체를 호출할 때 호출한 객체 자신이 전달되기 때문에 self를 사용한 것이다.
# 물론 self 말고 다른 이름을 사용해도 상관없다.
# >> 메서드의 첫번째 매개변수 self를 명시적으로 구현하는 것은 파이썬만의 독특한 특징이다. 예를 들어 자바 같은 언어는 첫 번째 매개변수 self가 필요 없다.

# 2 setdata 메서드의 수행문
# a.setdata(4, 2)처럼 호출하면 setdata 메서드의 매개변수 first, second에는 각각 값 4와 2가 전달되어 setdata 메서드의 수행문은 다음과 같이 해석된다.
# self.first = 4 | self.second = 2
# self는 전달된 객체 a이므로 다시 다음과 같이 해석된다.
# a.first = 4 | a.second = 2
# a.first = 4 문장이 수행되면 a 객체에 객체변수 firstㅏ 생성되고 값 4가 저장된다. 마찬가지로 a.second = 2 문장이 수행되면 a 객체에 객체변수 second가 생성되고 값이 2가 저장된다.
# >> 객체에 생성되는 객체만의 변수를 객체변수라고 부른다.
# 다음과 같이 확인해보자.
"""
a = FourCal()
a.setdata(4, 2)
print(a.first)    # 4를 출력
print(a.second)    # 2를 출력
"""
# a 객체에 개체변수 firrst와 second가 생성되었음을 확인할 수 있다.
# 이번에는 다음과 같이 a, b 객체를 만들어보자.
a = FourCal()
b = FourCal()
# 그리고 a 객체의 객체변수 first를 다음과 같이 생성한다.
a.setdata(4, 2)
# print(a.first)
# 이번에는 b 객체의 객ㄱ체변수 first를 다음과 같이 생성한다.
b.setdata(3, 7)
# print(b.first)
# 클래스로 만든 객체의 객체변수는 다른 객체의 객체변수에 상관없이 독립적인 값을 유지한다.
# id 함수를 사용하면 객체변수가 독립적인 값을 유지한다는 점을 좀 더 명확하게 증명해 보일 수 있다. 다시 다음과 같이 따라 해보자.
# >> id 함수는 객체의 주소를 돌려주는 파이썬 내장 함수이다.
"""
a = FourCal()
b = FourCal()
a.setdata(4, 2)
b.setdata(3, 7)
id(a.first)   # a의 first 주소값을 확인
print(id(a.first))
id(b.first)    # b의 first 주소값을 확인
print(id(b.first))
"""
# a 객체의 first 주소값과 b 객체의 first 주소 값이 서로 다르므로 각각 다른 곳에 그 값이 저장된다는 것을 알 수 있다. 객체변수는 그 객체의 고유 값을 저장할 수 있는 공간이다.
# 객체 변수는 다른 객체들 영향받지 않고 독립적으로 그 값을 유지한다는 점을 꼭 기억하자. 클래스에는 이 부분을 이해하는 것이 가장 중요하다.
# 다음은 현재까지 완성된 FourCal 클래스이다.

class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second



"""
더하기 기능 만들기
"""
# 자! 그럼 2개의 숫자 값을 설정해 주었으니 2개의 숫자를 더하는 기능을 방금 만든 클래스에 추가해보자. 우리는 다음과 같이 더하기 기능을 갖춘 클래스를 만들어야 한다.
"""
>>> a = FourCal()
>>> a.setdata(4, 2)
>>> print(a.add())
6
"""
# 이 연산이 가능하도록 다음과 같이 FourCal 클래스를 만들어 보자.

class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
# 새롭게 추가된 것은 add 메서드이다. 이제 클래스를 사용해보자.

a = FourCal()
a.setdata(4, 2)
# 위와 같이 호출하면 앞에서 살펴보았듯이 a객체의 first, second 객체 변수에는 각각 값 4와 2가 저장될 것이다.
# 이제 add 메서드를 호출해 보자.
# print(a.add())
# a.add()라고 호출하면 add 메서드가 호출되어 값 6이 출력될 것이다. 어떤 과정을 거쳐 값이 6이 출력되었는지 add 메서드를 따로 떼어 내서 자세히 살펴보자.


"""
곱하기, 더하기, 나누기, 기능 만들기
"""
"""
class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):  
        result = self.first - self.second
        return result
    def div(self):  
        result = self.first / self.second
        return result

a = FourCal()
b = FourCal()
a.setdata(5, 10)
b.setdata(10, 13)
print(a.div())
print(b.div())
print(a.mul())
print(b.mul())
print(a.sub())
print(b.sub())
"""
# 여기까지 우리가 목표로 한 사칙연산 기능을 가진 클래스를 만들어 보았다.



### 생성자 (Constructor)
# 이번에는 우리가 만든 FourCal 클래스를 다음과 같이 사용해보자.

"""
>>> a = FourCal()
>>> a.add()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 6, in add
AttributeError: 'FourCal' object has no attribute 'first'
"""
# FourCal 클래스의 인스턴스 a에 setdata 메서드를 수행하지 않고 add 메서드를 수행하면 "AttributeError: 'FourCal' object has no attribute 'first'"
# 오류가 발생한다. setdata 메서드를 수행해야 객체 a의 객체 변수 first와 second가 생성되기 때문이다.
# 이렇게 객체에 초깃값을 설정해야 할 필요가 있을 때는 setdata와 같은 메서드를 호출하여 초깃값을 설정하기보다는 생성자를 구현하는 것이 안전한 방법이다. 생성자(Constructor)란
# 객체가 생성될 때 자동으로 호출되는 메서드를 의미한다. 
# 파이썬 메서드의 이름으로 __init__를 사용하면 이 메서드는 생성자가 된다. 다음과 같이 FourCal클래스에 생성자를 추가해보자.
# >> __init__ 메서드의 init 앞뒤로 붙은 _는 언더스코어(_) 두 개를 붙여 쓴 것이다. 

class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):  
        result = self.first - self.second
        return result
    def div(self):  
        result = self.first / self.second
        return result
# 새롭게 추가된 생성자 __init__ 메서드만 따로 떼어 내서 살펴보자.
# __init__ 메서드는 setdata 메서드와 이름만 다르고 모든게 동일하다. 단 메서드 이름을 __init__으로 했기 때문에 생성자로 인식되어 객체가 생성되는 시점에 자동으로 호출되는 차이가 있다.
# 이제 다음처럼 예제를 수행해보자.

# a = FourCal()
# a = FourCal() 수행할 때 생성자 __init__이 호출되어 위와 같은 오류가 발생했다. 오류가 발생한 이유는 생성자의 매개변수 first와 second에 해당하는 값이 전달되지 않았기 때문이다.
# 위 오류를 해결하려면 다음처럼 first와 second에 해당되는 값을 전달하여 객체를 생성해야 한다.

a = FourCal(4, 2)
# 위와 같이 수행하면 __init__ 메서드의 매개변수에는 각각 오른쪽과 같은 값이 대입된다.
"""
매개변수    |    값
self       |   생성되는 객체
first      |    4
second     |    2
"""
# >> __init__ 메서드도 다른 메서드와 마찬가지로 첫 번째 매개변수 self에 생성되는 객체가 자동으로 전달된다는 점을 기억하자.
# 따라서 __init__ 메서드가 호출되면 setdata 메서드를 호출했을 때와 마찬가지로 first와 second라는 객체변수가 생성될 것이다.
# 다음과 같이 객체변수의 값을 확인해보자.

# a = FourCal(4, 2)
# print(a.first)
# print(a.second)
# add나 div 등의 메서드도 잘 동작하는지 확인해보자.
# print(a.add())
# print(a.div())
# print(a.mul())
# print(a.sub())




### 클래스의 상속
# 상속(Inheritance)이란 "물려받다"라는 뜻으로, "재산을 상속받다"라고 할 때의 상속과 같은 의미이다.
# 클래스에도 이 개념을 적용할 수 있다. 어떤 클래스를 만들 때 다른 클래스의 기능을 물려받을 수 있게 만드는 것이다. 
# 이번에는 상속 개념을 사용하여 우리가 만든 FourCal 클래스에 ab (a의 b제곱)을 구할 수 있는 기능을 추가해 보자.

# 앞에서 FourCal 클래스는 이미 만들어 놓았으므로 FourCal 클래스를 상속하는 MoreFourCal 클래스는 다음과 같이 간단하게 만들 수 있다.
class MoreFourCal(FourCal):
    pass
# 클래스를 상속하기 위해서는 다음처럼 클래스 이름 뒤 괄호 안에 상속할 클래스 이름을 넣어주면 된다.
# >> class 클래스 이름(상속할 클래스 이름)
# MoreFourCal 클래스는 FourCal 클래스를 상속했으므로 FourCal 클래스의 모든 기능을 사용할 수 있어야 한다.

"""
a = MoreFourCal(4, 2)
print(a.first)
print(a.second)
print(a.add())
print(a.mul())
print(a.sub())
print(a.div())
"""
# 상속받은 FourCal 클래스의 기능을 모두 사용할 수 있음을 확인할 수 있다.
"""
왜 상속을 해야 할까?

보통 상속은 기존 클래스를 변경하지 않고 기능을 추가하거나 기존 기능을 변경하려고 할 때 사용한다.
"클래스에 기능을 추가하고 싶으면 기존 클래스를 수정하면 되는데 왜 굳이 상속을 받아서 처리해야 하지?" 라는 의문이 들 수도 있다. 
하지만 기존 클래스가 라이브러리 형태로 제공되거나 수정이 허용되지 않는 상황이라면 상속을 사용해야 한다.
"""
# 이제 원래 목적인 a의 b제곱을 계산하는 MoreFourCal 클래스를 만들어 보자.

class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result
# pass 문장은 삭제하고 위와 같이 두 수의 거듭제곱을 구할 수 있는 pow 메서드를 추가해 주었다. 그리고 다음과 같이 pow 메서드를 수행해보자.
a = MoreFourCal(4, 2)
print(a.pow())
# 상속은 MoreFourCal 클래스처럼 기존 클래스(FourCal)는 그대로 놔둔 채 클래스의 기능을 확장시킬 때 주로 사용한다.



### 메서드 오버라이딩
# 이번에는 FourCal 클래스를 다음과 같이 실행해보자.
"""
a = FourCal(4, 0)
print(a.div())
"""
# FourCal 클래스의 객체 a에 4와 0 값을 설정하고 div 메서드를 호출하면 4를 0으로 나누려고 하기 때문에 위와 같은 ZeroDivisionError 오류가 발생한다. 
# 하지만 0으로 나눌 때 오류가 아닌 0을 돌려주도록 만들고 싶다면 어떻게 해야 할까?

# 다음과 같이 FourCal 클래스를 상속하는 SafeFourCal 클래스를 만들어보자.
class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:    # 나누는 값이 0인 경우 0을 리턴하도록 수정
            return 0
        else:
            return self.first / self.second
# SafeFourCal 클래스는 FourCal 클래스에 있는 div 메서드를 동일한 이름으로 다시 작성하였다. 이렇게 부모 클래스(상속한 클래스)에 있는 메서드를 동일한 이름으로 다시 만드는 것을
# 메서드 오버라이딩(Overriding, 덮어쓰기)이라고 한다. 이렇게 메서드를 오버라이딩하면 부모클래스의 메서드 대신 오버라이딩한 메서드를 호출한다.

# SafeFourCal 클래스에 오버라이딩한 div 메서드는 나누는 값이 0인 경우에는 0을 돌려주도록 수정했다. 이제 다시 위에서 수행한 예제를 FourCal 클래스 대신 SafeFourCal 클래스를 사용하여 수행해보자.
a = SafeFourCal(4, 0)
print(a.div())
# FourCal 클래스와는 달리 ZeroDivisionError가 발생하지 않고 의도한 대로 0을 돌려주는 것을 확인할 수 있을 것이다.




### 클래스 변수
# 객체변수는 다른 객체에 영향받지 않고 독립적으로 그 값을 유지한다는 점을 이미 알아보았다. 이번에는 객체변수와는 성격이 다른 클래스 변수에 대해 알아보자.
# 다음 클래스를 작성해보자.
class Family:
    lastname = "김"
# Family 클래스에 선언한 lastname이 바로 클래스 변수이다. 클래스 변수는 클래스 안에 함수를 선언하는 것과 마찬가지로 클래스 안에 변수를 선언하여 생성한다.
# 이제 Family 클래스를 다음과 같이 사용해 보자.

# print(Family.lastname)
# 클래스 변수는 위 예와 같이 클래스이름.클래스변수로 사용할 수 있다.
# 또는 다음과 같이 Family 클래스로 만든 객체를 통해서도 클래스 변수를 사용할 수 있다.
a = Family()
b = Family()
print(a.lastname)
print(b.lastname)

# 만약 Family 크래스의 lastname을 다음과 같이 "박"이라는 문자열로 바꾸면 어떻게 될까?
Family.lastname = "박"
print(a.lastname)
print(b.lastname)
# 클래스 변수 값을 변경했더니 클래스로 만든 객체의 lastname 값도 모두 변경된다는 것을 확인할 수 있다. 즉 클래스 변수는 클래스로 만든 모든 객체에 공유된다는 특징이 있다.

# id 함수를 사용하면 클래스 변수가 공유된다는 사실을 증명할 수 있다.
print(id(Family.lastname))
print(id(a.lastname))
print(id(b.lastname))
# id 값이 모두 같으므로 Family.lastname, a.lastname, b.lastname은 모두 같은 메모리를 가리키고 있다.
# 클래스 변수를 가장 늦게 설명하는 이유는 클래스에서 클래스 변수보다 객체변수가 훨씬 중요하기 때문이다. 실무 프로그래밍을 할 때도 클래스 변수보다는 객체변수를 사용하는 비율이 훨씬 높다.