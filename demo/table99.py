for num1 in range(1,10):
    for num2 in range(1,num1+1):
        print("%d * %d = %-2d"%(num2,num1,num1*num2),end=' ')
    print()
