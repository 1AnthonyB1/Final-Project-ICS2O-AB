print()
x = input("Hello There, I'm ... What's your name? ")
print()
print("Hello",x,"nice to meet you...")

#The adventure begins
while True:
    y = input("\nAre you ready to begin now? \nYes or No... ")
    y = str.upper(y)
    if y == "NO" or y == "N":
        print("\nOk then... I guess you'll never witness this epic story...")
    elif y == "YES" or y == "Y":
        break

print("\nGreat! The adventure begins... \n\nYou find yourself on a grassy beach, ahead of you there \nis a sandy hill and to your left the remains of crashed \nshipwreck.")

print("\nYou feel an ache in your back as you stand up and you soon \nrelize that you could get a better view of the sourounding\nland if you went up the hill. However you also notice\nsomething glimmering in the hull of the deserted ship. What \ndo you achoose?\n\nOption 1: Climb atop the sandy hill\n\nOption 2: Walk into the hull of the broken ship")
z = int(input("\nWhat option do you choose (Must be a number):"))

while True:
    if z == 1:
        print("\nnice choice")
        break

    elif z == 2:
        print("\nInteresting choice")
        break

    else:
        print("Flubby Chubb")
        break