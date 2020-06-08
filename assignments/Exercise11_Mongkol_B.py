number = int(input())
for x in range(number) :
    text2 = ""
    for y in range(x) :
        text2 = "*" + text2
    for z in range(x+1) :
        text2 = "*" + text2
    print(" "*(number-x),text2)