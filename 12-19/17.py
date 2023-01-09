getAge = int(input("What is your age? "))
if getAge >= 18:
    print("You can Vote")
elif getAge == 17:
    print("You can learn how to drive")
elif getAge == 16:
    print("You can buy a lottery ticket")
elif getAge <= 16:
    print("You can go Trick or Treating")