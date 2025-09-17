a=4 #0100
b=5 #0101
print(a&b) #4 both must be true
print(a|b) #5 either one is true
print(a^b) #1 both the bits are same result 0
print(~b) #it reverses the bits 1->0,0->1 as negative numbers are not stored in memory we'll be converting bit into 2's complement as 1's compliment+1 that gets the result.
#~10=-(10+1)->-11
print(a<<2)#adding 2 zeros 0100.0000 two zeros from left to right i.e.,010000.00->16
print(a>>2)#adding 2 zeros 0100.0000 two zeros from right to left i.e.,01.000000->1
#left shift gaining bits ,right shift loosing bits
#x<<n -> x*2^n
#x>>n -> x/2^n