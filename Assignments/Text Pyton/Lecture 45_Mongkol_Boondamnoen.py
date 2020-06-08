InputRound = int(input("Please Enter Number : "))
Sum = 0
print(list(range(InputRound)))
for x in range(InputRound) :
    InputNumber = int(input("x"+str(x+1)+": "))
    Sum += InputNumber
print('Total :',Sum)