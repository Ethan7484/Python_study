### 4-1. 문자열
"""
sentence = '나는 소년입니다.'
print(sentence)
sentence2 = "파이썬은 쉬워요."
print(sentence2)
sentence3 = '''
나는 소년이고,
파이썬은 쉬워요.
'''
print(sentence3)
sentence4 = '''
나는 소녀입니다.
파이썬은 쉬워요.
'''
print(sentence4)
"""


### 4-2.슬라이싱

jumin = "990120-1234567"

print("성별 : " + jumin[7])
print("연 : " + jumin[0:2])
print("월: " + jumin[2:4])
print("일: " + jumin[4:6])

print("생년월일: " + jumin[:6])
