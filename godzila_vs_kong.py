budget = float(input())
extras = int(input())
price_of_clothing = float(input())
decor = budget * 0.1
clothing_final = extras * price_of_clothing
if extras > 150:
    clothing_final =  clothing_final - (clothing_final * 0.1)
final_sum = clothing_final + decor
leftover_or_missing = abs(budget - final_sum)
if final_sum > budget:
    print(f"Not enough money!")
    print(f"Wingard needs {leftover_or_missing:.2f} leva more.")
elif final_sum <= budget:
    print(f"Action!")
    print(f"Wingard starts filming with {leftover_or_missing:.2f} leva left.")




