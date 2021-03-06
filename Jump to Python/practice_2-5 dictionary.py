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

# a = {'a': 1, 'b': 2}
# print(a['a'])
# print(a['b'])
# print(a)

# dic = {'name':'pey', 'phone':'01099993323','birth':'1118'}
# print(dic['name'])
# print(dic['phone'])
# print(dic['birth'])

"""
2. dictionary를 만들 때 주의할 사항
"""
# a = {1:'a', 1:'b'} # 동일한 Key값을 설정해 놓으면 하나를 제외한 나머지는 무시됨.
# print(a) # 1:'a' 쌍은 무시 되는 결과

# Key에 리스트를 쓸 수 없다. 하지만 튜플은 Key에 쓸 수 있다.

# a = {[1,2]:'hi'} # 리스트는 Key로 쓸 수 없음.
# print(a) # 에러가 출력되며 결과값이 출력되지 않는다.

# a = {(1,):'hi'} # 튜플은 Key로 사용할 수 있다.
# print(a)



### 딕셔너리 관련 함수들
# 딕셔너리를 자유자재로 사용하기 위해 딕셔너리가 자체적으로 가지고 있는 함수를 사용해보자

"""
1. Key 리스트 만들기(Keys)
"""
# a = {'name':'pey', 'phone':'01199993323', 'birth':'1118'}
# a.keys() # a의 Key만 모아서 dict_keys 객체를 돌려준다.
# print(a.keys()) # dict_keys(['name', 'phone', 'birth'])
# print(list(a.keys())) # dict_keys 객체가 필요없고, 리스트만 필요한 경우 list(a.keys())를 사용한다.
# dict_keys 객체는 다음과 같이 사용할 수 있다. 리스트를 사용하는 것과 차이가 없지만, 리스트 고유의 append, insert, pop, remove, sort는 사용 할 수 없음.

# for k in a.keys():
  # print(k)  
# print(list(a.keys()))

"""
2. Value 리스트 만들기(values)
"""
# a = {'name':'pey', 'phone':'01199993323', 'birth':'1118'}
# a.values() # Key를 얻는 것과 마찬가지로 Value만 얻고 싶다면 Values 함수를 사용하면 된다.
# print(a.values())
# print(list(a.values()))

"""
3. Key, Values 쌍 얻기(items)
"""
a = {'name':'pey', 'phone':'01199993323', 'birth':'1118'}
# a.items() # items 함수는 Key와 Value의 쌍을 튜플로 묶은 값을 dict_items 객체로 돌려준다.
# print(a.items())

"""
4. Key: Value 쌍 모두 지우기(clear)
"""
# a.clear() # Clear 함수는 딕셔너리 안의 모든 요소를 삭제함 
# print(a.clear())
# print(a)  # 딕셔너리 안의 모든 요소가 삭제되어 {}로 출력

"""
5. Key로 Value 얻기 (get)
"""
a = {'name':'pey', 'phone':'01199993323', 'birth':'1118'}
# a.get('name')     # get(x) 함수는 x라는 Key에 대응되는 Value를 돌려줌. 
# a.get('phone')
# print(a.get('name'))
# print(a.get('phone'))

# print(a.get('nokey')) # Key값이 없는 'nokey'를 입력했을 때, 'None' 값을 돌려준다
                      # 여기에서 None은 '거짓'이라는 뜻
# print(a['nokey']) # a['nokey']는 키(nokey)가 존재하지 않기 때문에 a['nokey']는 Key 오류를 발생시킴

# 딕셔너리 안에 찾으려는 Key 값이 없을 경우, 미리 정해 둔 디폴트 값을 대신 가져오게 하고 싶을 때에는 get(x, '디폴트값')을 사용
# a.get('foo', 'bar')
# print(a.get('foo','bar')) # a 딕셔너리에 'foo'에 해당하는 Key 값이 없을 경우, 디폴트 값인 'bar'를 돌려줌

"""
6. 해당 Key가 딕셔너리 안에 있는지 조사하기(in)
"""
print('name' in a)  # a 딕셔너리에 'name' Key 값이 존재하는지 조사
print('email' in a) # a 딕셔너리에 'email' Key 값이 존재하는지 조사
