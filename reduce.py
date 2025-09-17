from functools import reduce
prices = [120, 250, 300, 150, 80]
x=reduce(lambda a,b:a+b,prices)
print(x)