
# Find the Factorial Number

i = int(input("enter the value :"))
factorial = 1
if i<0:
    print('negative value')
while i>0:
    factorial = factorial*i
    i=i-1
print("Factorial =", factorial)


# code
""" i=5
     check while condition i>0 
        fact = fact * i  
        
       =>  i = i - 1  
           i = 5 - 1 = 4 , i=4-1 = 3, i=3-1 = 2, i=2-1 = 1
              i=5,4,3,2,1
         so, i=5 and fact=1   
            first i = 5
            
            fact = 1 * 5
                 = 5
                 = 5 * 4
                 = 20
                 = 20 * 3
                 = 60
                 = 60 * 2
                 = 120
                 = 120 * 1
                 = 120
        final ans of factorial 5 = 120
"""


