
# Check prime number

n=int(input("enter a value :"))
factor=0
i=1
while i<=n:
    if n%i==0:
        factor=factor+1
    i=i+1
if factor==2:
    print(n, "is prime number")
else:
    print(n, "is not prime number")


