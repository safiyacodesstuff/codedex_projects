# this code belongs to https://www.codedex.io/python/13-ph-levels

ph = int(input("Enter the ph level: "))

if ph > 7:
    print("basic")
elif ph < 7:
    print("acidic")
else:
    print("neutral")