# 그리워하는 사람의 이름을 담은 문자열 배열 name
# 각 사람별 그리움 점수를 담은 정수 배열 yearning
# 각 사진에 찍힌 인물의 이름을 담은 이차원 배열 photo가 매개변수로 주어질 때,
# 사진들의 추억 점수를 photo에 주어진 순서대로 배열에 담아 return하는 solution함수를 완성해주세요

# 예시
name = ["may", "kein", "kain", "radi"]
yearning = [5, 10, 1, 3]
photo =  [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]

# 후잡한 내 답
def solution(name, yearning, photo):
    answer = []
    to_dict = {ny[0] : ny[1] for ny in zip(name, yearning)}
    for p in photo:
        temp = []
        for n in p:
            temp.append(to_dict.get(n, 0))
        answer.append(sum(temp))
    return answer

# 쩌는 답
# def solution(name, yearning, photo):
#     return [sum(yearning[name.index(j)] for j in i if j in name) for i in photo]

print(solution(name, yearning, photo))