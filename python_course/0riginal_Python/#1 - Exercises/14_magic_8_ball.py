# this code belongs to https://www.codedex.io/python/14-magic-8-ball

import random

y = input("What's your question?: ")

x = random.randint(1, 9)

if x == 1:
    print("Yes - definitely.")
elif x == 2:
    print("It is decidedly so.")
elif x == 3:
    print("Without a doubt.")
elif x == 4:
    print("Reply hazy, try again.")
elif x == 5:
    print("Ask again later.")
elif x == 6:
    print("Better not tell you now.")
elif x == 7:
    print("My sources say no.")
elif x == 8:
    print("Outlook not so good.")
elif x == 9:
    print("Very doubtful.")