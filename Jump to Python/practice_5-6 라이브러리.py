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



### pickle
# pickle은 객체의 형태를 그대로 유지하면서 파일에 저장하고 불러올 수 있게 하는 모듈이다. 
# 다음 예는 pickle 모듈의 dump 함수를 사용하여 딕셔너리 객체인 data를 그대로 파일에 저장하는 방법을 보여준다.