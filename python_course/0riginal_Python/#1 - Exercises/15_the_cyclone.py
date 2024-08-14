# this code belongs https://www.codedex.io/python/15-the-cyclone

height = int(input("How tall are you? (Please enter your height in cm): "))
credits = int(input("How many credits do you have?: "))

if height >= 137 and credits >= 10:
    print("Enjoy the ride!")
elif height < 137 and credits >= 10:
    print("You are not tall enough to ride.")
elif height >= 137 and credits < 10:
    print("You don't have enough credits to ride.")
else:
    print("You are neither tall enough nor have enough credits to ride.")