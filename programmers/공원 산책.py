# 공원 배열 = park
# 로봇 명령 배열 = routes
# 모든 명령 수행 후 놓인 위치를 return하는 solution 함수

# 예시
# park, routes, result
# ["SOO","OOO","OOO"] ["E 2","S 2","W 1"]	[2,1]
# ["SOO","OXX","OOO"]	["E 2","S 2","W 1"]	[0,1]
# ["OSO","OOO","OXO","OOO"]	["E 2","S 3","W 1"]	[0,0]

park = ["SOO","OOO","OOO"]
routes = ["E 2","S 2","W 1"]

# print(routes[0].split(' '))
park_matrix = []
for p in park:
    park_matrix.append(list(p))

print(park_matrix.index())
# def solution(park, routes):
#     answer = []
#     return answer