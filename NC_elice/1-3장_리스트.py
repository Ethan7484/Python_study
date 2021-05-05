### [이론1] 리스트 활용

"""
a = []
a.append(10)
print(a)
"""

"""
c = [1, 2, 4, 5]
c.insert(2, 3)
print(c)    # [1, 2, 3, 4, 5]
"""

"""
d = [3, 1, 2, 3]
d.remove(3)
print(d)
"""

"""
# list.sort()
e = [6, 2, 4, 1]
f = ['carrot', 'apple', 'banana']
e.sort()
f.sort()
print(e, f)
"""

"""
twice = ["모모", "쯔위", "사나", "지효", "미나", "다현", "나연", "정연", "채영"]

blackpink = ["지수", "제니", "리사", "로제"]

# 1. 트와이스와 블랙핑크의 멤버는 각각 몇 명일까요? 한 번 알아봅시다!

twice_member = len(twice)
blackpink_member = len(blackpink)
print(twice_member)
print(blackpink_member)

# 2. 멤버 수가 많아 헷갈리네요! 누가 어디 그룹의 소속인지 알아보고 각각 출력해봅시다.
# 2-1. 모모는 블랙핑크 소속일까요? in을 써서 알아봅시다.
momo = '모모' in blackpink
print(momo)

# 2-2. 쯔위는 트와이스 소속일까요?
Tzu = '쯔위' in twice
print(Tzu)

# 2-3 지수는 블랙핑크 소속일까요?
jisu = '지수' in blackpink
print(jisu)
"""

"""
a = ['ring']
b = ['ding']
c = ['dong']
d = ['diggi']
# 연결 연산자를 이용해서 ['ring', 'ding', 'dong']를 lyric에 대입해봅시다.
lyric = a + b + c 
print(lyric)

# 수능을 하루 앞둔 친구에게 수능 금지곡을 들려줍시다!
# 변수 shinee에 다음 리스트를 담아봅시다.
# ['ring', 'ding', 'dong', 'ring', 'ding', 'dong']
shinee1 = lyric * 2
print(shinee1)

# 노래가 좀 짧네요! 뒷부분도 불러봅시다!
#['ring','diggi','ding','diggi','ding','ding','ding']
shinee2 = a + d + b + d + b + b + b
print(shinee1 + shinee2)
"""

# 과일들이 담긴 리스트 fruits입니다.
fruits = ['Apple', 'Banana', 'Chamwae', 'Durian']

# 지시사항에 맞추어 "Durian"을 fruits에서 지워봅시다.
if 'Durian' in fruits:
    fruits.remove('Durian')
    print(fruits)
else:
    print("'Durian'은 이 안에 없습니다.")


# 지시사항에 맞추어 "Pineapple"을 fruits에서 지워봅시다.

if 'Pineapple' in fruits:
    fruits.remove('Pineapple')
    print(fruits)
else:
    print("'Pineapple'은 이 안에 없습니다.")
