firstName = input("What is your first name ")
if len(firstName) < 5:
    lastName = input("What is your Last Name? ")
    joinedName = firstName + lastName
    print(joinedName.upper())
else:
    print(firstName.lower())