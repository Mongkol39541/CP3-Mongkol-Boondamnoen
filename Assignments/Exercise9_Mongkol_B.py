UserNameInput = input("Username : ")
PassWordInput = input("Password : ")
if UserNameInput == "Admin" and PassWordInput == "1234" :
    print("True ! ")
while UserNameInput != "Admin" or PassWordInput != "1234" :
    print("False ! ")
    UserNameInput = input("Username : ")
    PassWordInput = input("Password : ")
    if UserNameInput == "Admin" and PassWordInput == "1234":
        print("True ! ")