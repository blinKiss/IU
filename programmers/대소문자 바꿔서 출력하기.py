# swapcase나 upper lower쓰지 않고 결과 얻기
def convert_case(string):
    converted = ''
    for char in string:
        ascii_val = ord(char)  # 문자의 ASCII 값을 가져옵니다.
        if 65 <= ascii_val <= 90:  # 대문자인 경우
            converted += chr(ascii_val + 32)  # ASCII 값에 32를 더하여 소문자로 변환합니다.
        elif 97 <= ascii_val <= 122:  # 소문자인 경우
            converted += chr(ascii_val - 32)  # ASCII 값에 32를 빼서 대문자로 변환합니다.
        else:  # 알파벳이 아닌 경우
            converted += char  # 변환하지 않고 그대로 추가합니다.
    return converted

# 예시 실행
input_str = "aBcDeFg"
output_str = convert_case(input_str)
print(output_str)  # AbCdEfG

