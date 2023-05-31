import sys, time, random

typing_speed = 100 #wpm
def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)

print()
x = input(slow_type("Hello There, I'm ... What's your name?"))
print()
print("Hello",x,"nice to meet you...")

#The adventure begins
while True:
    y = input(slow_type("\nAre you ready to begin now? \nYes or No... "))
    y = str.upper(y)
    if y == "NO" or y == "N":
        slow_type("\nOk then... I guess you'll never witness this epic story...")
    elif y == "YES" or y == "Y":
        break

slow_type("\nGreat! The adventure begins... \n\nYou find yourself on a grassy beach, ahead of you there \nis a sandy hill and to your left the remains of crashed \nshipwreck.\n")

slow_type("\nYou feel an ache in your back as you stand up and you soon \nrelize that you could get a better view of the sourounding\nland if you went up the hill. However you also notice\nsomething glimmering in the hull of the deserted ship. What \ndo you achoose?\n\nOption 1: Climb atop the sandy hill\n\nOption 2: Walk into the hull of the broken ship\n")
z = int(input("\nWhat option do you choose (Must be a number):"))

while True:
    if z == 1:
        slow_type("\nnice choice")
        break

    elif z == 2:
        slow_type("\nInteresting choice")
        break

    else:
        slow_type("\nFlubby Chubb")
        break