"""
딕셔너리란?
사람은 누구든지 "이름" = "홍길돌", "생일" = "몇 월 며칠" 등으로 구분
파이썬도 이러한 대응 관계를 나타낼 수 있는 자료형을 가짐
요즘 대부분의 언어도 이러한 대응 관계를 나타내는 자료형을 갖음
이를 연관 배열(Associative array) 또는 해시(Hash)라고 함.

파이썬은 이러한 자료형을 딕셔너리(Dictionary)라고 하는데
사전이라는 뜻으로 딕셔너리는 Key와 Value를 한 쌍으로 갖는 자료형
예를 들어 Key가 "baseball"이라면 Value는 "야구"가 됨

딕셔너리는 리스트나 튜플처럼 순차적으로 해당 요솟값을 구하지 않고 Key를
통해 Value를 얻음. 이것이 딕셔너리의 가장 큰 특징.
baseball이라는 단어의 뜻을 찾기 위해 사전의 내용을 순차적으로 모두 검색
하는 것이 아니라 baseball이라는 단어가 있는 곳만 펼쳐 보는 것과 같음
"""

### 딕셔너리는 어떻게 만들까?
# 기본 딕셔너리 = {key1:Value1, key2:Value2, Key3:Value3}
# Key1:Value1은 한 쌍으로 부른다.
# Key는 변하지 않는 값을 사용하고 Value를 변하는 값과 변하지 않는 값 모두 사용 가능

# dic = {'name':'pey', 'phone':'0119993323', 'birth':'1118'} # name = key, value = pey
# print(dic['name']) 

# a = {1: 'hi'} # 1이라는 key에 'hi' Value를 저장
# print(a[1])

# a = {'a': [1, 2, 3]} # Value 값에는 리스트도 넣을 수 있음.
# print(a['a'])


### 딕셔너리 쌍 추가, 삭제하기
"""
1. 딕셔너리 쌍 추가하기
"""
# a = {1: 'a'}
# a[2] = 'b' # 딕셔너리 a에 Key와 Value가 2와 'b'인 2:'b' 딕셔너리 쌍이 추가됨.
# print(a)
# a['name'] = 'pey' # Key = 'name', Value = 'pey'라는 쌍을 추가
# print(a)
# a[3] = [1, 2, 3] # Key = 3, Value = [1, 2, 3] 이라는 쌍을 추가
# print(a)
# print(a[3])

"""
2. 딕셔너리 요소 삭제하기
"""
# del a[1]  # 딕셔너리 a의 Key 1을 삭제
# print(a)


### 딕셔너리를 사용하는 방법
"""
1. 딕셔너리에서 Key 사용해서 Value 얻기
"""
# grade = {'pey': 10, 'julliet': 99} # grade 딕셔너리에 pey, julliet Key 값 입력
# print(grade['pey']) # grade 딕셔너리에서 'pey'키의 값(Value)를 추출
# print(grade['julliet']) # grade 딕셔너리에서 'julliet' 키의 값(Value)를 추출
# a = {1: 'a', 2: 'b'}
# print(a[1]) # a[1]에서의 [1]은 듀플이나 리스트의 두번째 요소를 의미하는게 아니라, Key에 해당하는 1을 의미함.
# print(a[2])

a = {'a': 1, 'b': 2}
print(a['a'])
print(a['b'])