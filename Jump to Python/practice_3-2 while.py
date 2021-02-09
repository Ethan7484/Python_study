### while문의 기본 구조
# 반복해서 문장을 수행해야 할 경우 while문을 사용한다. 그래서 while문을 반복문이라고도 부른다.
# 다음은 while문의 기본 구조이다.

"""
while <조건문>:
    <수행할 문장1>
    <수행할 문장2>
    <수행할 문장3>
    <수행할 문장4>
    ......
"""
# while문은 조건문이 참인 동안에 while문 아래의 문장이 반복해서 수행된다.
# "열번 찍어 안 넘어가는 나무 없다"는 속담을 파이썬 프로그램으로 만든다면 다음과 같이 될 것이다.
"""
treeHit = 0
while treeHit < 10:
    treeHit = treeHit + 1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
      print("나무는 넘어갑니다")
"""
# 위 예에서 while문의 조건문은 "treeHit < 10"이다. 즉 treeHit 10보다 작은 동안에 while문 안의 문장을 계속 수행한다.
# while문 안의 문장을 보면 제일 먼저 "treeHit = treeHit + 1"로 treeHit값이 계속 1씩 증가 한다.
# 그리고 나무를 treeHit번만큼 찍었음을 알리는 문장을 출력하고 treeHit이 10이 되면 "나무 넘어갑니다"라는 문장을 출력한다.
# 그러고 나면 "treeHit < 10" 조건문이 거짓이 되므로 while문을 빠져나가게 된다.
# treeHit = treeHit + 1은 자주 사용하는 기법. 값을 1만큼 증가시킬 목적일 때, treeHit += 1처럼 사용하기도 함



### while문 만들기
# 이번에는 여러가지 선택지 중 하나를 선택해서 입력받는 예제를 만들어 보자. 먼저 다음과 같이 여러 줄짜리 문자열을 입력한다.
prompt = """
1. Add
2. Del
3. List
4. Quit
Enter number:
"""
# 이어서 number 변수에 0을 먼저 대입한다. 이렇게 변수를 먼저 설정해 놓지 않으면 다음에 나올 while문의 조건문인
# "number != 4"에서 변수가 존재하지 않는다는 오류가 발생한다.
"""
number = 0
while number != 4:
    print(prompt)
    number = int(input())
"""
# while문을 보면 number가 4가 아닌 동안 prompt를 출력하고 사용자로부터 번호를 입력받는다. 다음 결과 화면처럼
# 사용자가 값 4를 입력하지 않으면 계속해서 prompt를 출력한다.
# *여기에서 number = int(input())은 사용자의 숫자 입력을 받아들이는 것으로만 알아두자.



### while문 강제로 빠져나가기
# while문은 조건문이 참인 동안 계속해서 while문 안의 내용을 반복적으로 수행한다.
# 하지만 강제로 while문을 빠져나가고 싶을 때가 있다. 예를 들어 커피 자판기를 생각해보자.
# 자판기 안에 커피가 충분히 있을 때에는 동전을 넣으면 커피가 나온다. 그런데 자판기가 제대로 동작하려면
# 커피가 얼마나 남아 있는지 항상 검사해야 한다. 만약 커피가 떨어졌다면 판매를 중단하고 "판매 중지" 문구를
# 사용자에게 보여주어야 한다. 이렇게 판매를 강제로 멈추게 하는 것이 바로 break문이다.
"""
coffee = 10
money = 300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee -= 1
    print("남은 커피의 양은 %d입니다." % coffee)
    if coffee == 0:
      print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
      break
"""

# coffee.py
coffee = 10
while True:
    money = int(input("돈을 넣어주세요: "))
    if money == 300:
      print("커피를 줍니다.")
      coffee -= 1
    elif money > 300:
      print("거스름돈 %d를 주고 커피를 줍니다." % (money - 300))
      coffee -= 1
    else:
      print("돈을 다시 돌려주고 커피를 주지 않습니다.")
      print("남은 커피의 양은 %d개 입니다. " % coffee)
    if coffee == 0:
      print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
      break


### while문의 맨 처음으로 돌아가기