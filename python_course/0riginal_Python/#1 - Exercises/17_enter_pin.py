# thsi code belongs to https://www.codedex.io/python/17-enter-pin

print('=== BANK OF CODéDEX ===')  

pin = int(input('Enter your PIN: '))

while pin != 1234:
  pin = int(input('Incorrect PIN. Enter your PIN again: '))

if pin == 1234:
  print('PIN accepted!')