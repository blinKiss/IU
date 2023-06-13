players=["mumu", "soe", "poe", "kai", "mine"]
callings = ["kai", "kai", "mine", "mine"]

# 만년걸린 답
def solution(players, callings):
    to_dict = {player : i for i, player in enumerate(players)}
    for name in callings:
        index = to_dict[name]
        # players.insert(index-1, players.pop(index))
        players[index-1], players[index] = players[index], players[index-1]
        to_dict[players[index]] = index
        to_dict[players[index-1]] = index -1
        # print(to_dict)
    return players


print(solution(players, callings))