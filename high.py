list1=[11,2,3,4,5,6,1,99]
high=list1[0]
for i in list1:
    if i>high:
        high=i
print("Highest Number:",high)