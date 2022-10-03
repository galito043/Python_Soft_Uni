hour = int(input())
minutes = int(input())
total_time_in_min = (60 * hour) + minutes + 15

real_hour = total_time_in_min // 60
real_minutes = total_time_in_min % 60

if real_hour > 23:
    real_hour = 0

if real_minutes < 10:
    print(f"{real_hour}:0{real_minutes}")
else :
    print(f"{real_hour}:{real_minutes}")
