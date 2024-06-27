
# Check leap year

year = int(input("Enter Year:"))

if (year%4==0 and year%100!=0) or (year%400 == 0):
    print(year, "This is leap year")
else:
    print(year, "This is not leap year")


