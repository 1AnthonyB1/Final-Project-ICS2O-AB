print()
x = input("Hello There, I'm ... What's your name? ")
print()
print("Hello",x,"nice to meet you...")

#The adventure begins
while True:
    y = input("\nAre you ready to begin now? \nYes or No... ")
    y = str.upper(y)
    if y == "NO":
        True
        print("\nOk then... I guess you'll never witness this epic story...")
    elif y == "YES":
        False
        break

z = print("\nGreat! The adventure begins... \n\nYou find yourself on a grassy beach, ahead of you there \nis a sandy hill and to your left the remains of \ncrashed shipwreck.")