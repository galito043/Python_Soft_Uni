trip_price = float(input())
number_of_jigsaws = int(input())
number_of_dolls = int(input())
number_of_teddy_bears = int(input())
number_of_minions = int(input())
number_of_trucks = int(input())
discount = 0
sum = (2.60 * number_of_jigsaws) + (3 * number_of_dolls) + (4.1 * number_of_teddy_bears) + (8.20 * number_of_minions) + (2 * number_of_trucks)
if number_of_jigsaws + number_of_dolls + number_of_teddy_bears + number_of_minions + number_of_trucks >= 50:
    discount = (sum * 0.25)
final_price = sum - discount
rent = (final_price * 0.10)
profit = final_price - rent
difference = abs(trip_price - profit)
if profit >= trip_price:
    print(f"Yes! {difference:.2f} lv left.")
else:
    print(f"Not enough money! {difference:.2f} lv needed.")



