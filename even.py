i = int(input("Enter number of even number: "))
t = i*2

for e in range(1,t+2,1):
    if (e%2) == 0:
        print(e)