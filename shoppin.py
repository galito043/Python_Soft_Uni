budget = float(input())
number_of_gpus = int(input())
number_of_cpus = int(input())
number_of_rams = int(input())
sum_for_gpus = number_of_gpus * 250
sum_for_cpus = (sum_for_gpus * 0.35) * number_of_cpus
sum_for_rams = (sum_for_gpus * 0.10) * number_of_rams
total_sum = sum_for_gpus + sum_for_cpus + sum_for_rams
if number_of_gpus > number_of_cpus:
    total_sum = total_sum - (total_sum * 0.15)
left_over_budget = abs(budget - total_sum)
if total_sum <= budget:
    print(f"You have {left_over_budget:.2f} leva left!")
elif total_sum > budget:
    print(f"Not enough money! You need {left_over_budget:.2f} leva more!")



