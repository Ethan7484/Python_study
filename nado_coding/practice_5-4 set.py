# 집합 (set)
# 집합이란? 중복이 안되고, 순서가 없음

my_set = {1, 2, 3, 3, 3} # 중복이 허용되지 않기 때문에 3은 한번만 출력된다.
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 집합의 성질을 이용하여 교집합을 만들어냄
# java와 python을 모두 할 수 있는 사람을 찾아냄
print(java & python)
print(java.intersection(python)) # 위 &과 동일한 기능을 하는 intersection(교집합)

# 합집합을 해보자
# 즉 java도 할 수 있거나 (or) python도 할 수 있는 개발자
print(java | python)
print(java.union(python)) # | 와 같은 의미인 union(합집합)

# 차집합
# java는 할 수 있지만 python을 할 수 없는 사람 개발자
print(java - python)
print(java.difference(python))

# python 할 수 있는 개발자가 늘어남
python.add("김태호") # python 사전에 "김태호"를 추가
print(python)

# java 를 잊었어요.
java.remove("김태호") # java 사전에 "김태호"를 삭제
print(java)