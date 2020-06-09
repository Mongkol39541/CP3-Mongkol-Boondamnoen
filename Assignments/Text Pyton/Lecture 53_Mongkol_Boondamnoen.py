def VatCalculate(TotalPrice):
    Result = TotalPrice + (TotalPrice*7/100)
    return Result
print(VatCalculate(int(input())))