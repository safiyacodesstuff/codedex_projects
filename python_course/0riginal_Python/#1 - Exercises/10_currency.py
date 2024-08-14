# this code belongs to https://www.codedex.io/python/10-currency

import math

pesos = int(input("Please enter the amount of pesos you have left: "))
soles = int(input("Please enter the amount of soles you ahve left: "))
reais = int(input("Please enter the amount of reais you have left: "))

usd_1 = pesos*0.00025 
usd_2 = soles*0.27 
usd_3 = reais*0.18 

total_amount = usd_1 + usd_2 + usd_3

print("Your total amount of money amounts to $", round(total_amount, 2))