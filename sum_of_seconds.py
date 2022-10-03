import math
first_time = int(input())
second_time = int(input())
third_time = int(input())
total_time = first_time + second_time + third_time
sum_of_minutes = total_time // 60
sum_of_seconds = total_time % 60
sum_of_minutes = math.floor(sum_of_minutes)
if sum_of_seconds < 10:
    print(f"{sum_of_minutes}:0{sum_of_seconds}")
else:
    print(f"{sum_of_minutes}:{sum_of_seconds}")