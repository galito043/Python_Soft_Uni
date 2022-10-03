naylon = int(input())
paint = int(input())
paint_thinner = int(input())
work_time = int(input())
final_price_for_materials = naylon  * 1.50 + paint * 14.5  + paint_thinner * 5
extra_paint = (paint * 10 / 100) * 14.5 +(naylon + 2) * 1.50
pay = (final_price_for_materials * 30 / 100) * work_time
extreme_price = pay + final_price_for_materials + extra_paint
print(extra_paint)

