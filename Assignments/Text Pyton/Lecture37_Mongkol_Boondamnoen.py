usernameInput = input("Username : ")
passwordInput = input("Password : ")
if usernameInput == "admin" and passwordInput == "1234" :
    print("Done !")
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    userSelected = int(input(">>"))
    if userSelected == 1:
        price = int(input("Price (THB) : "))
        vat = int(input("Vat (THB) : "))
        result = price + (price * vat / 100)
        print("Result (THB) :", result)
    elif userSelected == 2:
        price1 = int(input("Fist Product Price : "))
        price2 = int(input("Second Product Price : "))
        print(price1+price2)
else :
    print("Error !")