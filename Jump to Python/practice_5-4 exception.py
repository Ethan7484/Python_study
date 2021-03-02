# f = open("나없는파일", 'r')    # 없는 파일을 열려고 시도할 때 출력되는 에러

# print( 4 / 0)    # 0으로 다른 숫자를 나누려고 할 때 출력되는 에러

# a = [1, 2, 3]
# print(a[4])    # a 리스트에 없는 인덱스를 호출할 때 발생하는 에러



### 오류 예외 처리 기법

"""
try, except문
"""
# 다음은 오류 처리를 위한 try, except문의 기본 구조이다.
"""
try:
    ....
except [발생 오류[as 오류 메시지 변수]]:
    ....
"""
# try 블록 수행 중 오류가 발생하면 except 블록이 수행된다. 하지만 try 블록에서 오류가 발생하지 않는다면
# except 블록은 수행되지 않는다.
# except 구문을 자세히 살펴보자.
"""
except [발생 오류[as 오류 메시지 변수]]:
"""
# 위 구문을 보면 [] 기호를 사용하는데, 이 기호는 괄호 안의 내용을 생략할 수 있다는 관례 표기법이다. 즉 except 구문은 다음 3가지 방법으로 사용할 수 있다.

"""
1. try, except만 쓰는 방법
try:
    ....
except:
    .....
"""
# 이 경우는 오류 종류에 상관없이 오류가 발생하면 except 블록을 수행한다.

"""
2. 발생 오류만 포함한 except문
try:
    ...
except 발생 오류:
    ....
"""
# 이 경우는 오류가 발생했을 때 except문에 미리 정해 놓은 오류 이름과 일치할때만 except 블록을 수행한다는 뜻이다.

"""
3. 발생 오류와 오류 메시지 변수까지 포함한 except문
try:
    ...
except 발생 오류 as 오류 메시지 변수:
    ...
"""
# 이 경우는 두번째 경우에서 오류 메시지의 내용까지 알고 싶을 때 사용하는 방법이다.
# 이 방법의 예를 들어 보면 다음과 같다.
"""
try:
    4 / 0
except ZeroDivisionError as e:
    print(e)
# 결괏값: dicision by zero
"""


"""
try.. finally
"""
# try문에는 finally 절을 사용할 수 있다. finally절은 try문 수행 도중 예외 발새 ㅇ여부에 상관없이 항상 수행된다.
# 보통 finally절은 사용한 리소스를 close해야 할 때에 많이 사용한다.
# 다음 예를 보자.
"""
f = open('foo.txt', 'a')
try:
    # 무언가 수행한다.
    print("#무언가 수행한다.")
finally:    # try에 내용이 없으면 "expected an indented block" 에러가 출력됨
    f.close()
"""

"""
여러개의 오류처리하기
"""
# try문 안에서 여러 개의 오류를 처리하기 위해 다음 구문을 사용한다.
"""
try:
    ...
except 발생 오류1:
    ...
except 발생 오류2:
    ...
"""
# 즉 0으로 나누는 오류와 인덱싱 오류를 다음과 같이 처리할 수 있다.
"""
try:
    a = [1, 2]
    print(a[3])
    4/0
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except IndexError:
    print("인덱싱 할 수 없습니다.")
"""
# a는 2개의 요솟값을 가지고 있기 때문에 a[3]는 IndexError를 발생시키므로 "인덱싱할 수 없습니다"라는 문자열이 출력될 것이다.
# 인덱싱 오류가 먼저 발생했으므로 4/0으로 발생되는 ZeroDivisionError 오류는 발생하지 않았다.
# 앞에서 알아본 것과 마찬가지로 오류 메시지도 다음과 같이 가져올 수 있다.
"""
try:
    a = [1, 2]
    print(a[3])
    4 / 0
except ZeroDivisionError as e:
    print(e)
except IndexError as e:
    print(e)
"""
# 프로그램을 실행하면 "list index out of range" 오류 메시지가 출력될 것이다.

# 다음과 같이 ZeroDivisionError와 IndexError를 함께 처리할 수도 있다.
"""
try:
    a = [1, 2]
    print(a[3])
    4 / 0
except (ZeroDivisionError, IndexError) as e:
    print(e)
"""
# 2개 이상의 오류를 동일하게 처리하기 위해서는 위와 같이 괄호를 사용하여 함께 묶어 처리하면 된다.

"""
try문에 else절 사용하기
try문에는 다음처럼 else절을 사용할 수 있다.

try:
    ...
except [발생 오류[as 오류 메시지 변수]]:
    ...
else:    # 오류가 없을 경우에만 수행된다.
    ...

try문 수행중 오류가 발생하면 except절이 수행되고 오류가 없으면 else절이 수행된다.
다음은 try문에 else절을 활용하는 간단한 예이다.


try:
    age = int(input("나이를 입력하세요: "))
except:
    print("입력이 정확하지 않습니다.")
else:
    if age <= 18:
        print("미성년자는 출입금지 입니다.")
    else:
        print("환영합니다.")
"""
# 만약 '나이를 입력하세요:'라는 질문에 숫자가 아닌 다른 값을 입력하면 오류가 발생하여 '입력이 정확하지 않습니다.'라는 문장을 출력한다.
# 오류가 없을 경우에만 else절이 수행된다.



### 오류 회피하기
# 프로그래밍을 하다 보면 특정 오류가 발생할 경우 그냥 통과시켜야 할 때가 있다. 다음 예를 보자.
"""
try:
    f = open("나없는파일", "r")
except FileNotFoundError:
    pass
"""
# try문 안에서 FileNotFoundError가 발생할 경우에 pass를 사용하여 오류를 그냥 회피하도록 작성한 예제이다.



### 오류 일부러 발생시키기
# 이상하게 들리겠지만 프로그래밍을 하다 보면 종종 오류를 일부러 발생시켜야 할 경우도 생긴다. 파이썬은 raise 명령어를 사용해 오류를 강제로 발생시킬 수 있다.
# 예를 들어 Bird 클래스를 상속받는 자식 클래스는 반드시 fly라는 함수를 구현하도록 만들고 싶은 경우(강제로 그렇게 하고 싶은 경우)가 있을 수 있다. 다음 예를 보자.

class Bird:
    def fly(Self):
        raise NotImplementedError
# 위 예제는 Bird 클래스를 상속 받는 자식 클래스는 반드시 fly 함수를 구현해야 한다는 의지를 보여 준다. 만약 자식 클래스가 fly 함수를 구현하지 않은 상태로  fly 함수를 호출한다면 어떻게 될까?
# >> NotImplementError는 파이썬 내장 오류로, 꼭 작성해야 하는 부분이 구현되지 않았을 경우 일부러 오류를 일으키기 위해 사용한다.
"""
class Eagle(Bird):
    pass
eagle = Eagle()
eagle.fly()
"""
# Eagle 클래스는 Bird 클래스를 상속받는다. 그런데 Eagle 클래스에서 fly 함수를 구현하지 않았기 때문에 Bird 클래스의 fly 함수가 호출된다.
# 그리고 raise문에 의해 NotImplemented Error가 발생할 것이다.
# >> 상속받는 클래스에서 함수를 재구현하는 것을 메서드 오버라이딩이라고 부른다.
# NotImplementedError가 발생되지 않게 하려면 다음과 같이 Eagle 클래스에 fly 함수를 반드시 구현해야 한다.
"""
class Eagle(Bird):
    def fly(self):
        print("very fast")

eagle = Eagle()
eagle.fly()
"""
# 위 예처럼 fly 함수를 구현한 후 프로그램을 실행하면 오류없이 다음 문장이 출력된다.
# very fast



### 예외 만들기
# 프로그램 수행 도중 특수한 경우에만 예외 처리를 하기 위해서 종종 예외를 만들어서 사용한다. 직접 예외를 만들어 보자. 
# 예외는 다음과 같이 파이썬 내장 클래스인 Exception 클래스를 상속하여 만들 수 있다.

class MyError(Exception):
    pass
# 그리고 별명을 출력해 주는 함수를 다음과 같이 작성한다.

def say_nick(nick):
    if nick == "바보":
        raise MyError()
    print(nick)
# 그리고 다음과 같이 say_nick 함수를 호출해 보자.
"""
say_nick("천사")
say_nick("바보")
"""
# 이번에는 예외 처리 기법을 사용하여 MyError 발생을 예외 처리해 보자.

try:
    say_nick("천사")
    say_nick("바보")
except MyError:
    print("허용되지 않는 별명입니다.")
# 만약 오류 메시지를 사용하고 싶다면 다음처러 예외 처리를 하면 된다.

try:
    say_nick("천사")
    say_nick("바보")
except MyError as e:
    print(e)
# 하지만 프로그램을 실행해 보면 print(e)로 오류 메시지가 출력되지 않는 것을 확인할 수 있다.
# 오류 메시지를 출력했을 때 오류 메시지가 보이게 하려면 오류 클래스에 다음과 같은 __str__메서드를 구현해야 한다.
# __str__ 메서드는 print(e)처럼 오류 메시지를 print문으로 출력할 경우에 호출되는 메서드이다.

class MyError(Exception):
    def __str__(self):
        return "허용되지 않는 별명입니다."

try:
    say_nick("천사")
    say_nick("바보")
except MyError as e:
    print(e)
# 프로그램을 다시 실행해 보면 "허용되지 않는 별명입니다."라는 오류메시지가 출력 되는 것을 확인할 수 있다. 