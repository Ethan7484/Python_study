### 6-6 하위 디렉터리 검색하기
# 특정 디렉터리부터 시작해서 그 하위 모든 파일 중 파이썬 파일(*.py)만 출력해 주는 프로그램을 만들려면 어떻게 해야 할까?

# 1. 다음과 같이 sub_dir_search.py 파일을 작성해 보자.

"""
sub_dir_search.py

def search(dirname):
    print (dirname)

search("c:/")
"""
# search 함수를 만들고 시작 디렉터리를 입력받도록 코드를 작성했다.


# 2. 이제 이 디렉터리에 있는 파일을 검색할 수 있도록 소스를 변경해 보자.
"""
import sys

def search(dirname):
    filenames = os.listdir(dirname)
    for filename in filenames:
        full_filename = os.path.join(dirname, filename)
        print(full_filename)

search("D:/Study/Python_study/Jump to Python/")
"""
# os.listdir를 사용하면 해당 디렉터리에 있는 파일들의 리스트를 구할 수 있다. 여기에서 구하는 파일 리스트는
# 파일 이름만 포함되어 있으므로 경로를 포함한 파일 이름을 구하기 위해서는 입력으로 받은 dirname을 앞에 덧붙여 주어야 한다.
# os 모듈에는 디렉터리와 파일 이름을 이어 주는 os.path.join 함수가 있으므로 이 함수를 사용하면 디렉터리를 포함한 전체 경로를 쉽게 구할 수 있다.
# 위 코드를 수행하면 디렉터리에 있는 파일이 다음과 비슷하게 출력될 것이다.