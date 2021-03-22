# 이제 파이썬 프로그래밍 능력을 높여 줄 더 큰 날개를 달아보자. 전 세계의 파이썬 사용자들이 만든 유용한 프로그램을 모아 놓은 것이
# 바로 파이썬 라이브러리이다. "라이브러리"는 "도서관"이라는 뜻 그대로 원하는 정보를 찾아보는 곳이다. 모든 라이브러리를 다 알 필요는 없고
# 어떤 일을 할 때 어떤 라이브러리를 사용해야 한다는 정도만 알면 된다. 그러기 위해 어떤 라이브러리가 존해하고 어떻게 사용하는지 알아야 한다. 
# 자주 사용되고 꼭 알아 두면 좋은 라이브러리를 중심으로 하나씩 살펴보자.

"""
목차
1. sys
2. pickle
3. os
4. shutil
5. glob
6. tempfile
7. time
8. calendar
9. random
10. webbrowser
"""



# ==============================================================================================================================
### sys
# sys 모듈은 파이썬 인터프리터가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈이다.

# 1. 명령 행에서 인수 전달하기 - sys.argv
"""
C:/User/home>python test.py abc pey guido
"""
# 명령 프롬프트 창에서 위 예처럼 test.py 뒤에 또 다른 값을 넣어주면 sys.argv 리스트에 그 값이 추가된다. 
# 예제를 따라 하며 확인해보자. 우선 다음과 같은 파이썬 프로그램을 작성하자. argv_test.py 파일은 C:/doit/MYmod 디렉터리에 저장했다고 가정한다. 

# 명령 프롬프트 창에서 Mymod 디렉터리로 들어간 뒤 다음과 같이 실행해보자.

"""
D:\Study\Python_study\Jump to Python\Mymod>python argv_test.py you need python
['argv_test.py', 'you', 'need', 'python']
"""
# python 명령어 뒤의 모든 것들이 공백을 기준으로 나뉘어서 sys.argv 리스트의 요소가 된다.
# >> 명령 프롬프트 창에서는 /, \ 든 상관없지만, 소스코드 안에서는 반드시 / 또는 \\ 기호를 사용해야 한다. 


# 2. 강제로 스크립트 종료하기 - sys.exit
"""
sys.exit()
"""
# sys.exit는 Crtl+Z나 Ctrl+D를 눌러서 대화형 인터프리터를 종료하는 것과 같은 기능을 한다. 
# 프로그램 파일 안에서 사용하면 프로그램을 중단시킨다.


# 3. 자신이 만든 모듈 불러와 사용하기 - sys.path
# sys.path는 파이썬 모듈들이 저장되어 있는 위치를 나타낸다. 즉 이 위치에 있는 파이썬 모듈은 경로에 상관없이 어디에서나 불러올 수 있다.
# 다음은 그 실행 결과이다.
"""
import sys
sys.path
[ "d:/pravite/python/Python_study/Jump to Python/practice_5-6 라이브러리.py" ]
"""
# 위 예에서 ""는 현재 디렉터리를 말한다. 

"""
# path_append.py
import sys
sys.path.append("d:/pravite/python/Python_study/Jump to Python/Mymod")
"""
# 위와 같이 파이썬 프로그램 파일에서 sys.path.append를 사용해 경로 이름을 추가할 수 있다. 이렇게 하고 난 후에는 
# d:/pravite/python/Python_study/Jump to Python/Mymod/ 디렉터리에 있는 파이썬 모듈을 불러와서 사용할 수 있다. 



# ==============================================================================================================================
### pickle
# pickle은 객체의 형태를 그대로 유지하면서 파일에 저장하고 불러올 수 있게 하는 모듈이다. 
# 다음 예는 pickle 모듈의 dump 함수를 사용하여 딕셔너리 객체인 data를 그대로 파일에 저장하는 방법을 보여준다.

"""
import pickle
f = open("test.txt", "wb")
data = {1: 'Python', 2: 'you need'}
pickle.dump(data, f)
f.close
"""
# 다음은 pickle.dump로 저장한 파일을 pickle.load를 사용해서 원래 있던 딕셔너리 객체(data) 상태 그대로 불러오는 예이다.

"""
import pickle
f = open("test.txt", 'rb')
data = pickle.load(f)
print(data)
"""
# 위 예에서는 딕셔너리 객체를 사용했지만 어떤 자료형이든 저장하고 불러올 수 있다.



# ==============================================================================================================================
### os
# OS 모듈은 환경 변수나 디렉터리, 파일 등의 OS 지원을 제어할 수 있게 해주는 모듈이다.

# 1. 내 시스템의 환경 변수값을 알고 싶을 때 - os.environ
# 시스템은 제각기 다른 환경 변수 값을 가지고 있는데, os.environ은 현재 시스템의 환경 변수 값을 보여 준다. 다음을 따라 해보자.

import os
# print(os.environ)
# 위 결괏값은 시스템 정보이다. os.environ은 환경 변수에 대한 정보를 딕셔너리 객체로 돌려준다. 자세히 보면 여러가지 유용한 정보를 찾을 수 있다.
# 돌려받은 객체가 딕셔너리이기 때문에 다음과 같이 호출할 수 있다. 다음은 시스템의 PATH 환경 변수 내용이다.

# a = os.environ['PATH']
# print(a)


# 2. 디렉터리 위치 변경하기 - os.chdir
# os.chdir를 사용하면 다음과 같이 현재 디렉터리 위치를 변경할 수 있다.

# os.chdir("C:\WINDOWS")


# 3. 디렉터리 위치 돌려받기 - os.getcwd
# os.getcwd는 현재 자신의 디렉터리 위치를 돌려준다.
"""
a = os.getcwd()
print(a)    # 'C:\WINDOWS'를 돌려줌
"""

# 4. 시스템 명령어 호출하기 - os.system 
# 시스템 자체의 프로그램이나 기타 명령어를 파이썬에서 호출할 수도 있다. os.system("명령어")처럼 사용한다.
# 다음은 현재 디렉터리에서 시스템 명령어 dir을 실행하는 예이다.
"""
os.system("dir")
os.system("dir/w")
"""

# 5. 실행한 시스템 명령어의 결괏값 돌려받기 - os.popen
# os.popen은 시스템 명령어를 실행한 결괏값을 읽기 모드 형태의 파일 객체로 돌려준다.
"""
f = os.popen("dir")
print(f.read())
"""
# 기타 유용한 os 관련 함수
"""
함수                ||          설명
os.mkdir(디렉터리)      디렉터리를 생성한다.
os.rmdir(디렉터리)      디렉터리를 삭제한다. 단, 디렉터리가 비어있어야 삭제가 가능하다.
os.unlink(vkdlf)        파일을 지운다.
os.rename(src, dst)     src라는 이름의 파일을 dst라는 이름으로 바꾼다.
"""


# ==============================================================================================================================
### shutil
# shutil은 파일을 복사해 주는 파이썬 모듈이다.

# 다음 예시는 src라는 이름의 파일을 dst로 복사한다. 만약 dst가 디렉터리 이름이라면 src라는 파일 이름으로 dst 디렉터리에 복사하고 동일한 파일 이름이 있을 경우 덮어쓴다.

"""
import shutil
shutil.copy("src.txt", "dst.txt")
"""
# 위 예를 실행해보면 src.txt 파일과 동일한 내용의 파일이 dst.txt로 복사되는 것을 확인할 수 있다.



# ==============================================================================================================================
### glob
# 가끔 파일을 읽고 쓰는 기능이 있는 프로그램을 만들다 보면 특정 디렉터리에 있는 파일 이름 모두를 알아야 할 때가 있다.
# 이럴때 사용하는 모듈이 바로 glob이다.


# 1. 디렉터리에 있는 파일들을 리스트로 만들기 - glob(pathname)
# glob 모듈은 디렉터리 안의 파일들을 읽어서 돌려준다. *, ? 등 메타 문자를 써서 원하는 파일만 읽어 들일 수도 있다.
# 다음 디렉터리에 있는 파일 중 이름이 mark로 시작하는 파일을 모두 찾아서 읽어들이는 예이다.

"""
import glob
a = glob.glob("D:\pravite\python\Python_study\Jump to Python\mark*")
print(a)
"""



# ==============================================================================================================================
### tempfile
# 파일을 임시로 만들어서 사용할 때 유용한 모듈이 바로 tempfile이다. tempfile.mkstemp()는 중복되지 않는 임시 파일의 이름을 무작위로 만들어서 돌려준다.

"""
import tempfile
filename = tempfile.mkstemp()
print(filename)    # (3, 'C:\\Users\\ethan\\AppData\\Local\\Temp\\tmpmhea2mx6')
"""
# tempfile.TemporaryFile()은 임시 저장 공간으로 사용할 파일 객체를 돌려준다. 이 파일은 기본적으로 바이너리 쓰기 모드(wb)를 갖는다.
# f.close()가 호출되면 이 파일 객체는 자동으로 사라진다. 

"""
import tempfile
f = tempfile.TemporaryFile()
f.close()
"""



# ==============================================================================================================================
### time
# 시간과 관련된 time 모듈에는 함수가 굉장히 많다. 그중 가장 유용한 몇 가지만 알아보자.

# 1. time.time
# time.time()는 UTC를 사용하여 현재 시간을 실수 형태로 돌려주는 함수이다. 1970년 1월 1일 0시 0분 0초를 기준으로 지난 시간을 초 단위로 돌려준다.

"""
import time
a = time.time()
print(a)    # 1616377837.8341794    현재 시간이 '초'단위로 출력된 상태
"""

# 2. time.localtime
# time.localtime은 time.time()이 돌려준 실수 값을 사용해도 "연도, 월, 일, 시 분, 초" 의 형태로 바꾸어 주는 함수이다. 
"""
import time
a = time.localtime(time.time())
print(a)    # time.struct_time(tm_year=2021, tm_mon=3, tm_mday=22, tm_hour=11, tm_min=12, tm_sec=9, tm_wday=0, tm_yday=81, tm_isdst=0) 돌려줌
"""

# 3. time.asctime
# 위 time.localtime에 의해서 반환된 튜플 형태의 값을 인수로 받아서 날짜와 시간을 알아보기 쉬운 형태로 돌려주는 함수이다.

"""
import time
a = time.asctime(time.localtime(time.time()))
print(a)    # Mon Mar 22 11:14:24 2021, "요일 / 월 / 날짜 / 시간 / 연도"순으로 출력됨
"""


# 4. time.ctime
# time.asctime(time.localtime(time.time()))은 time.ctime()을 사용해 간편하게 표시할 수 있다. asctime과 다른 점은 ctime은 항상 현재 시간만 돌려준다는 점이다. 

"""
import time
a = time.ctime()
print(a)    # 현재 시간을 돌려준다. Mon Mar 22 11:59:32 2021
"""


# 5. time.strftime
# time.strftime('출력할 형식 포맷 코드', time.localtime(time.time()))
# strftime 함수는 시간에 관계된 것을 세밀하게 표현하는 여러 가지 포맷 코드를 제공한다.

import time
# 요일 줄임말
a = time.strftime('%a', time.localtime(time.time()))
print(a)

# 요일 줄임말
a = time.strftime('%a', time.localtime(time.time()))
print(a)