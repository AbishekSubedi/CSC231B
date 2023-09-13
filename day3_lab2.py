# Write a program that asks the user for a number, and then says if they entered 7 or not.

'''user_number = input("Enter a number: ")
user_number = int(user_number)

 if(user_number == 7):
     print("Congrats, your number was seven! :D")
 else:
     print("OOPS, your number wasn't seven! :(")'''

keepLooping = True #start the code with true value
while keepLooping == True:
    user_number = int(input("Please enter a number: "))
    if(user_number == 7):
        print("Congrats, your number was seven! :D")
        keepLooping = False
    else:
        print("OOPS, wrong number! :(")



