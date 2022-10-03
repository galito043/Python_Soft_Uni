fee = int(input())
basketball_shoes = fee - (fee * 40 / 100)
basketball_tracksuit = basketball_shoes - (basketball_shoes * 20 / 100)
basketball_ball = basketball_tracksuit - (basketball_tracksuit * 75 / 100)
basketball_accessories = basketball_ball - (basketball_ball * 80 / 100)
total_sum = basketball_shoes + basketball_tracksuit + basketball_ball + basketball_accessories + fee
print(total_sum)