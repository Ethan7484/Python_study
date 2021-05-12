###[이론1] 문자열/리스트 활용

"""
my_list = [1, 2, 3, 4, 5]
print(my_list.pop(0))    # 1
print(my_list.pop())    # 5
"""

"""
my_seq = [2, 2, 2, 4, 4]
print(my_seq.count(2))    # 3
"""


# str.split(c)
# c를 기준으로 문자열을 쪼개서 리스트를 반환 (괄호를 비울시 공백)
"""
my_str = "1 2 3 4 5"
print(my_str.split())    # ['1', '2', '3', '4', '5']
element = "Na, Mg, Al, Si"
print(element.split(','))    ['Na', 'Mg', 'Al', 'Si']
"""


# str.join(list) 리스트 -> 문자열
# str을 기준으로 리스트를 합쳐서 문자열을 반환 (괄호를 비울 시 공백)

"""
my_list = ['a', 'p', 'p', 'l', 'e']
print(''.join(my_list))    # apple
friend = ['Pat', 'Mat']
print('&'.join(friend))    # Pat&Mat 
"""


# [실습1] pop, count
"""
# 1. 숫자 1, 2, 2, 3, 3이 담긴 my_list를 선언
my_list = [1, 2, 2, 3, 3, 3]
# 2. my_list 안의 숫자 3의 개수를 변수 var1에 넣어봅시다.
var1 = my_list.count(3)
print(var1)
# 3. 일부 원소를 제거하여 my_list가 [1, 2, 3]되도록 해봅시다.
my_list.pop(1)    # [1, 2, 3, 3, 3]
print(my_list)
my_list.pop(2)    # [1, 2, 3, 3]
print(my_list)
my_list.pop(2)    # [1, 2, 3]
print(my_list)
"""

#[실습2] split, join
"""
# 1. 문자열 "beetea"가 담긴 변수 my_str를 선언해봅시다.
my_str = "beetea"
print(my_str)

# 2. 문자열 'e'를 기준으로 my_str를 리스트로 만든 다음, 이를 변수 var1에 담아봅시다.
var1 = my_str.split("e")
print(var1)

# 3. 리스트 ["Seeing", "is", "Believing"]이 담긴 변수 my_list를 선언해봅시다.
my_list = ["Seeing", "is", "Believing"]
print(my_list)

# 4. 공백()을 기준으로 my_list를 문자열로 만들어보고, 이를 변수 var2에 담아봅시다. 
var2 = " ".join(my_list)
print(var2)
"""

#[실습3] 노래 가사 분석
"""
# 1. 문자열 lyrics를 콤마를 기준으로 나누어 리스트를 만들어 봅시다.
lyrics = "낙엽을,닮은,너의,눈동자를,나는,정말,정말,좋아했었어,가을을,닮은,너의,목소리를,나는,아직,아직,잊지,못했어,같이,걸으면서,들었던,낙엽,소리가,내,귓가에,들려오는,것만,같아,함께,앉아,있던,좁다란,나무,벤치엔,너의,온기가,남아있는,것만,같아,낙엽을,닮은,너의,눈동자를,나는,정말,정말,좋아했었어,가을을,닮은,너의,목소리를,나는,아직,아직,잊지,못했어"
lyrics = lyrics.split(",")
print(lyrics)

# 2. 이 리스트의 46번째 구절을 출력해봅시다.
print(lyrics[45])
"""


### [이론2] Tuple(튜플)
"""
my_list = ['l', 'i', 's', 't']
my_list[1] = 'a'
print(my_list)    # ['l', 'a', 's', 't']
"""

# Tuple의 필요성 -> 값을 바꿀 수 없으면서도 여러 자료형을 담기 위해서
# Tuple(튜플) 여러 자료를 함께 담을 수 있는 자료형. ()-소괄호로 묶어서 표현. 1개만 넣을 때는 (1,) 쉼표를 넣어야 함.
"""
tuple_zero = ()
tuple_one = (1,)
tuple_ = (1, 2, 3, 4, 5)
tuple1 = 1, 2, 3, 4, 5    # 소괄호를 넣지 않아도 자동으로 튜플로 저장
print(tuple_zero)
print(tuple_one)
print(tuple_)
print(tuple1)
"""

# Tuple의 특징
# 시퀀스 자료형으로 index를 이용한 인덱싱, 슬라이싱이 가능
"""
my_tuple = ('t', 'w', 'i', 'c', 'e')
print(my_tuple[1])    # 'w'
print(my_tuple[2:4])    # ('i', 'c')
print('t' in my_tuple)    # true
print(len(my_tuple))    # 5
"""

# + 연산자로 Tuple과 Tuple을 연결. * 연산자로 Tuple을 반복
"""
my_tuple = ('i', 'c', 'e')
print(('e', 'l') + my_tuple)    # ('e', 'l', 'i', 'c', 'e')
print(my_tuple * 2)    #('i', 'c', 'e', 'i', 'c', 'e')
"""

# Tuple의 특징 -> 자료 추가, 삭제, 변경 불가. 한번 만들어지면 고정!
"""
my_tuple = ('t', 'w', 'i', 'c', 'e')
print(my_tuple.append("!"))    # Error
print(my_tuple.remove('w'))
my_tuple[1] = 's'
"""
my_tuple[1] = 's'
my_tupde[1] = 's'
