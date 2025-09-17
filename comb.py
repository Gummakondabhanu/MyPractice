from functools import reduce
prices = [120, 250, 300, 150, 80]
x=list(map(lambda a:a-(a*0.10),prices))
y=list(filter(lambda b:b<=200,x))
z=reduce(lambda a,b:a+b,y)
print(z)
