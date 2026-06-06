password = "goa"

guess = ""
while guess != password:
    guess = input("enter the password: ")
    
    if guess != password:
        print("wrong password, try again")
else:
    print("correct password, welcome to the next level")