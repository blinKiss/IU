# my_list = [1, 2, 3, 4, 5]
# element = my_list.pop(4)  # 해당 요소를 제거하고 반환
# my_list.insert(3, element)  # 다른 위치에 요소 삽입
# print(my_list)


players=["mumu", "soe", "poe", "kai", "mine"]
callings = ["kai", "kai", "mine", "mine"]
result = []
# print(players.pop(players.index('kai')))
def solution(players, callings):
    
    for name in callings:
        index = players.index(name)
        players.insert(index-1, players.pop(index))
    return result

print(solution(players, callings))