num_char = len(input('What is your name?'))

# print('Your name has ' + num_char + ' characters.')
# 오류 // 문자열 사이에 정수를 넣을 수 없음

new_num_char = str(num_char)

print('Your name has ' + new_num_char + ' characters.')
