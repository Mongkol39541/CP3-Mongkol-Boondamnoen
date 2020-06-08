for x in range(1,13) :
    for y in  range(12) :
        print(x,"x",y+1,"=",x*(y+1))
    break

for val in "Hello" :
    if val == "l" :
        continue
    print(val)

print("The end")

number = int(input())
for x in range(number) :
    print("*"* (x+1))