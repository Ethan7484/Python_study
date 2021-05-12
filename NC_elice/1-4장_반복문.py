### [이론1] 반복문 for문

"""
sum = 0
for i in range(100):
    print("*" * i)
    i = i + 1
"""

"""
length = 0
for x in 'abcdefg':
    length = length + 1
    print(length)
"""

"""
for i in range(10):
    print(i)
"""



###[이론2] 반복문 for-range문
"""
a = range(0, 9)
print(list(a))
"""

"""
a = [1]
for i in range(2, 4):
    a.append(i)
print(a)
"""

"""
count = 0
for i in range(10):
    count = count + 1
print(count)
"""


###[이론3] 반복문 while문

i = 5
while i > 0:
    print(i)
    i = i - 1
print("Launch!")