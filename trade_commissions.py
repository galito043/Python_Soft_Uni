city = input()
sales = float(input())
commission = 0
flag = True
if city == "Sofia":
    if 0 <= sales <= 500:
        commission = sales * 0.05
    elif sales <= 1000:
        commission = sales * 0.07
    elif 1000 < sales <= 10000:
        commission = sales * 0.08
    elif sales > 10000:
        commission = sales * 0.12
elif city == "Varna":
    if 0 <= sales <= 500:
        commission = sales * 0.045
    elif sales <= 1000:
        commission = sales * 0.075
    elif 1000 < sales <= 10000:
        commission = sales * 0.10
    elif sales > 10000:
        commission = sales * 0.13
elif city == "Plovdiv":
    if 0 <= sales <= 500:
        commission = sales * 0.055
    elif sales <= 1000:
        commission = sales * 0.08
    elif 1000 < sales <= 10000:
        commission = sales * 0.12
    elif sales > 10000:
        commission = sales * 0.145
else:
    flag = False
if flag:
    print(f"{commission:.2f}")
else:
    print("error")