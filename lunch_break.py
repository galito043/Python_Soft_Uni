import math
name_of_tv_series = input()
lenght_of_tv_series = int(input())
lenght_of_break = int(input())
time_for_lunch = lenght_of_break / 8
chill_time = lenght_of_break / 4
left_over_time = lenght_of_break - (time_for_lunch + chill_time)
time_after_watching_tv_series = math.ceil(abs(lenght_of_tv_series - left_over_time))
if left_over_time >= lenght_of_tv_series:
    print(f"You have enough time to watch {name_of_tv_series} and left with {time_after_watching_tv_series} minutes free time.")
elif lenght_of_tv_series > left_over_time:
    print(f"You don't have enough time to watch {name_of_tv_series}, you need {time_after_watching_tv_series} more minutes.")
