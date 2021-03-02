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
