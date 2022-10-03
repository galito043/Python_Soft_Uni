lenght = int(input())
width = int(input())
height = int(input())
percent = float(input())
volume = lenght * width * height
volume_in_liters = volume * 0.001
required_liters = volume_in_liters *(1-percent*0.01)
print(required_liters)
