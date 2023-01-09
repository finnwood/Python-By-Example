isRaining = str(input("Is it currently Raining? "))
if isRaining == "Yes" or isRaining == "YES" or isRaining =="yes":
    isWindy = str(input("Is it windy out? "))
    if isWindy == "Yes" or isWindy == "YES" or isWindy =="yes":
        print("It is Too windy to take an Umbrella")
    else:
        print("Take an Umbrella")
else:
    print("Have a nice day!")