chicken_menus = int(input())
fish_menus = int(input())
veggie_menus = int(input())
price = chicken_menus * 10.35 + fish_menus * 12.40 + veggie_menus * 8.15
price_of_desert = (price * 20) / 100
total =  price + price_of_desert + 2.50
print(total)