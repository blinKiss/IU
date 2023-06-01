# # 시작 값(a), 등비(r), 몇 번째인지를 나타내는 정수(n)가 입력될 때
# # n번째 수를 출력하는 프로그램을 만들어보자.
# temp = input('시작값, 등비, 숫자위치를 공백을 두고 입력 : ')
# temp2 = temp.split(' ')
# a = temp2[0]
# r = temp2[1]
# n = temp2[2]




# 입력 받기
numbers = input("시작값, 등비, 숫자위치를 공백을 두고 입력 : ")

# 입력된 숫자들을 공백을 기준으로 분리하여 리스트로 변환
number_list = numbers.split(' ')

# 허용된 범위를 설정
min_value = 0
max_value = 10

# 입력된 숫자들을 하나씩 확인하며 범위 체크
for number in number_list:
    # 숫자로 변환
    num = int(number)
    
    # 범위 체크
    if num < min_value or num > max_value:
        print("입력한 숫자는", min_value, "에서", max_value, "사이여야 합니다.")
        exit()

a = int(number_list[0])
r = int(number_list[1])
n = int(number_list[2])

result = a * (r ** (n-1))

print(result)

