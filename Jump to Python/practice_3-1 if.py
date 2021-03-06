### if문은 왜 필요할까?
# "돈이 있으면 택시를 타고, 돈이 없으면 걸어 간다"
money = True
if money:
    print("택시를 타고 가라")
else:
    print("걸어 가라")
# money에 True를 입력했으므로 money는 참이다. 따라서 if문 다음 문장이 수행되어 '택시를 타고 가라'가 출력된다.


### if문의 기본 구조
# 다음은 if와 else를 사용한 조건문의 기본 구조이다.
"""
if 조건문:
  수행할 문장1
  수행할 문장2
else:
  수행할 문장A
  수행할 문장B
"""
# 조건문을 테스트해서 참이면 if문 바로 다음 문자(if 블록)들을 수행하고, 조건문이 거짓이면 else문 다음 문자(else 블록)
# 들을 수행하게 된다. 그러므로 else문은 if문 없이 독립적으로 사용할 수 없다.


### 들여쓰기
# if문을 만들 때는 if 조건문: 바로 아래 문장부터 if문에 속하는 모든 문장에 들여쓰기(indentation)을 해주어야 한다.
# 오른쪽에서 보는 것과 같이 조건문이 참일 경우 "수행할 문자1"을 들여쓰기 했고 "수행할 문장2"와 "수행할 문장3"도 들여쓰기 해주었다.
# 다른 프로그래밍 언어를 사용해 온 사람들은 파이썬에서 "수행할 문장"을 들여쓰기하는 것을 무시하는 경우가 많으니 더 주의해야 한다.



### 조건문이란 무엇인가?
# if 조건문에서 '조건문'이란 참과 거짓을 판단하는 문장을 말한다.
# 앞에서 살펴본 택시 예제에서 조건문은 money가 된다.

"""
비교 연산자
"""
# 이번에는 조건문에 비교연산자(<, >, ==, !=, >=, <=)를 쓰는 방법에 대해 알아보자.
"""
비교연산자	설명
x < y	x가 y보다 작다
x > y	x가 y보다 크다
x == y	x와 y가 같다
x != y	x와 y가 같지 않다
x >= y	x가 y보다 크거나 같다
x <= y	x가 y보다 작거나 같다
"""
x = 3
y = 2
print(x > y)    # x > y가 참이기 때문에 True 값을 돌려준다.
print(x < y)    # x가 y보다 크기 때문에 거짓이므로 False 값을 돌려준다.

# "만약 3000원 이상의 돈을 가지고 있으면 택시를 타고 그렇지 않으면 걸어가라"
money = 2000
if money >= 3000:
    print("택시를 타고 가라")
else:
    print("걸어가라")


"""
and, or, not
"""
# 조건을 판단하기 위해 사용하는 다른 연산자로는 and, or, not이 있다. 각각의 연산자는 다음처럼 동작한다.
"""
연산자   | 설명
x or y  | x와 y 둘중에 하나만 참이어도 참이다
x and y	| x와 y 모두 참이어야 참이다
not x	  | x가 거짓이면 참이다
"""
# 다음 예를 통해 or 연산자의 사용법을 알아보자. "돈이 3000원 이상 있거나 카드가 있다면 택시를 타고 그렇지 않으면 걸어 가라"

money = 2000
card = True
if money >= 3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어가라")
# money가 2천원이지만 card가 True이기 때문에 조건문이 참이 된다. 


"""
x in s, x not in s
"""
# 더 나아가 파이썬은 다른 프로그래밍 언어에서 쉽게 볼 수 없는 재미있는 조건문을 제공한다.
"""
in    |    not in
x in 리스트    |    x not in 리스트
x in 튜플    |    x not in 튜플
x in 문자열    |    x not in 문자열
"""
# 영어 단어 in의 뜻이 "~안에"라는 것을 생각해보면 다음 예까 쉽게 이해될 것이다.
print(1 in [1, 2, 3]) # True. "[1, 2, 3]이라는 리스트에 1이 있는가"라는 조건문
print(1 not in [1, 2, 3]) # False. "[1, 2, 3]이라는 리스트에 1이 없는가"라는 조건문

# 다음은 튜플과 문자열에 적용한 예이다. 각각의 결과가 나온 이뉴는 쉽게 유출할 수 있다.
print('a' in ('a', 'b', 'c')) # 튜플 안에 'a'가 있는가 확인하는 조건문, True를 돌려준다
print('j' not in 'python') # 문자열 'python'에 'j'가 있는가 확인하는 조건문, True를 돌려준다

# 이번에는 우리가 계속 사용해 온 택시 예제에 in을 적용해보자. "만약 주머니에 돈이 있으면 택시를 타고 없으면 걸어 가라"
poket = ['money', 'paper', 'cellphone']
if 'money' in poket:
    print("택시를 타고 가라")
else:
    print("걸어 가라")


# 조건문에서 아무 일도 하지 않게 설정하고 싶다면, pass를 사용하자
poket = ['money', 'paper', 'cellphone']
if 'money' in poket:
    pass
else:
    print("걸어 가라")
# poket 리스트 안에 money가 있기 때문에 if문 다음 문장인 pass가 수행되고 아무 결과값도 출력되지 않는다(pass니까)


"""
다양한 조건을 판단하는 elif
"""
# if와 else 만으로는 다양한 조건을 판단하기 어렵다.
# "주머니에 돈이 있으면 택시를 타고, 주머니에 돈은 없지만 카드가 있으면 택시를 타고, 돈도 없고 카드도 없으면 걸어가라"
# 위 문장을 보면 조건을 판단하는 부분이 두 군데가 있다. 먼저 주머니에 돈이 있는지를 판단해야 하고 주머니에 돈이 없으면 다시 카드가 있는지 판단해야 한다.
# if와 else만으로 위 문장을 표현하려면 다음과 같이 할 수 있다.

poket = ['paper', 'handphone']
card = True
if 'money' in poket:
    print("택시를 타고 가라")
else:
    if card:
        print("택시를 타고 가라")
    else:
        print("걸어 가라")
# 언뜻 보기에도 이해하기 어렵고 산만한 느끼이 든다. 이런 복잡함을 해결하기 위해 파이썬에서는 다중 조건 판단을 가능하게 하는 elif를 사용한다.
# 위 예를 elif를 사용하면 다음과 같이 바꿀 수 있다.
poket = ['paper', 'handphone']
card = True
if 'money' in poket:
    print("택시를 타고 가라")
elif card:
    print("택시를 타고 가라")
else:
    print("걸어 가라")
# elif는 개수에 제한 없이 사용할 수 있다.

# if문을 한 줄로 작성하기
# 앞의 passㄹ르 사용한 예를 보면 if문 다음에 수행할 문장이 한 줄이고, else문 다음에 수행할 문장도 한 줄 밖에 되지 않는다.
if 'money' in poket:
    pass
else:
    print("카드를 꺼내라")
# 이렇게 수행할 문장이 한 줄일 때, 조금 더 간략하게 코드를 작성하는 방법이 있다.
poket = ['paper', 'money', 'cellphone']
if 'money' in poket: pass
else: print("카드를 꺼내라")
# if문 다음 수행할 문장을 콜론(:) 뒤에 바로 적어 주었다. else문 역시 마찬가지이다.



### 조건부 표현식
# 다음과 같은 코드를 보자
score = 59
if score >= 60:
    message = "success"
    print(message)
else:
    message = "failure"
    print(message)
# 위 코드는 score가 60 이상일 경우 messgae에 문자열 "success"를, 아닐 경우에는 "failure"를 대입하는 코드이다.
# 파이썬의 조건부 표현식(conditional expression)을 사용하면 위 코드를 다음과 같이 간단히 표현할 수 있다.
score = 60
message = "success" if score >= 60 else "failure" print()
# 조건부 표현식은 다음과 같이 정의한다.
# "조건문이 참인 경우" if "조건문" else "조건문이 거짓인 경우"
# 조건부 표현식은 가독성이 유리하고 한 줄로 작성할 수 있어 활용성이 좋다.

