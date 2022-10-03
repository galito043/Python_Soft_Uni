import math
number_of_pages = int(input())
pages_per_day = int(input())
number_of_days = int(input())
hours_needed_for_amount_of_pages = number_of_pages / pages_per_day
hours_per_day = hours_needed_for_amount_of_pages / number_of_days

print(math.floor(hours_per_day))