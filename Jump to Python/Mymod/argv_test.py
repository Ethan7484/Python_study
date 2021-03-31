# argv_test.py

import sys
# print(sys.argv)

# print("프로그램 시작")
# sys.exit('error!!')

# print("실행 안됨")

import sys

numbers = sys.argv[1:] # 파일 이름을 제외한 명령 행의 모든 입력

result = 0
for number in numbers:
    result += int(number)
print(result)