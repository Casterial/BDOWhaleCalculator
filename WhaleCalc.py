import math
print("Black Desert Online Whale Calculator")

HR = int(input("What is your $hour rate? "))
SN = int(input("What is your silver goal? "))
SH = int(input("What is your avg Silver/Hour "))


outfit_price = "1020000000"
OA = int(20)
print("\n\n****CURRENT MARKET OUTFIT PRICE****")
print(outfit_price, 'silver')
print("Average $USD Outfit Price: $20")
O = int(outfit_price)

print("\n\nCalculating....")

T = SN/SH
TU = HR * T
ON = SN/O
HoW = math.floor(((ON*OA)/HR))
DT = math.floor(T - HoW)

if HoW < T:
    print("Swiping may better....Its {0} hours faster.".format(DT))
else:
    print("Grinding may be better than swiping... Its {0} hours faster.".format(DT))

print("\nHOURS NEEDED TO WORK: {0}".format(HoW))
print("HOURS NEEDED TO GRIND: {0}".format(T))

