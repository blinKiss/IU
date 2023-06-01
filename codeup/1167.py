# 문제 설명
# 세 개의 숫자가 주어질 때 작은 순서로 나열 했을 때, 두번째 수를 출력해보자.
# 예를 들어, 5 9 2 가 있다면, 작은 순서로 나열하면 2 5 9이고 두번째 수는 5이다.

# 입력
# 세 개의 정수가 공백으로 구분되어 입력된다. 

# 출력
# 세 개의 정수를 작은 순서로 나열 했을 때, 두번째 수를 출력한다.

# 입력 예시
# 201 20 3

# 출력 예시
# 20

numbers = input('세 개의 수를 공백을 두고 입력 : ')
numbers_split = numbers.split(' ')

for i in enumerate(numbers_split):
    temp = 0
    if( int(numbers_split[i]) > int(numbers_split[i+1]) ):
        temp = int(numbers_split[i+1])
        
    
    