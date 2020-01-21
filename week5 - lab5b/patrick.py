check = 1
j=0

n = int(input("Enter the number of times"))
sum = 0
sum1 = 0
i=1

while i<=n:
    x = (i**n)
    sum = x+sum
    print(sum)
    i += 1



while j<(n):
    x1 = check*(n-j)
    sum1 = x1+sum1
    check+=2
    j+=1
    print(sum1)


