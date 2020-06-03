Username = input("Username : ")
Password = int(input("Password : "))
if Username == "Mongkol" and Password == 39541 :
    print("-------------------------Hello Welcome Drugstore-------------------------")
    print("-------------------------Has the following druds-------------------------")
    print("                    1.Cough Syrup           : 100 THB                    ")
    print("                    2.Headache Medicine     : 140 THB                    ")
    print("                    3.Toothache Medication  : 120 THB                    ")
    print("                    4.Antibiotics           : 250 THB                    ")
    print("                    5.Runny Nose Medication : 175 THB                    ")
    print("   If you buy more than 2000 THB, there will be a 30 percent discount.   ")
    ProductPrice             = int(input("1.Cough Syrup                  (THB) : "))
    NumberOfProducts         = int(input("  Cough Syrup           (Collection) : "))
    SumOfCoughSyrup          = ProductPrice * NumberOfProducts
    print("  Sum Of CoughSyrup                  :",SumOfCoughSyrup ,"THB")
    ProductPrice             = int(input("2.Headache Medicine            (THB) : "))
    NumberOfProducts         = int(input("  Headache Medicine     (Collection) : "))
    SumOfHeadacheMedicine    = ProductPrice * NumberOfProducts
    print("  Sum Of Headache Medicine           :",SumOfHeadacheMedicine ,"THB")
    ProductPrice             = int(input("3.Toothache Medication         (THB) : "))
    NumberOfProducts         = int(input("  Toothache Medication  (Collection) : "))
    SumOfToothacheMedication = ProductPrice * NumberOfProducts
    print("  Sum Of Toothache Medication        :",SumOfToothacheMedication ,"THB")
    ProductPrice             = int(input("4.Antibiotics                  (THB) : "))
    NumberOfProducts         = int(input("  Antibiotics           (Collection) : "))
    SumOfAntibiotics         = ProductPrice * NumberOfProducts
    print("  Sum Of Antibiotics                 :",SumOfAntibiotics ,"THB")
    ProductPrice             = int(input("5.Runny Nose Medication        (THB) : "))
    NumberOfProducts         = int(input("  Runny Nose Medication (Collection) : "))
    SumOfRunnyNoseMedication = ProductPrice * NumberOfProducts
    print("  Sum Of Runny Nose Medication       :",SumOfRunnyNoseMedication ,"THB")
    Total = SumOfCoughSyrup + SumOfHeadacheMedicine + SumOfToothacheMedication + SumOfAntibiotics + SumOfRunnyNoseMedication
    if Total >= 2000 :
        TotalValue = Total - ((Total/100)*30)
        print("Total Value                          :",TotalValue ,"THB")
    elif Total < 2000 :
        TotalValue = Total - ((Total/100)*30)
        print("Total Value                          :",TotalValue ,"THB")
else :
    print("Try again")