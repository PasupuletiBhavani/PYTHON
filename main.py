def CheckLeap(Year):
if ((Year % 4 == 0)):
    print("the year is leap year");
else:
    print("not a leap year");
    Year = int(input("Enter the number: "))
    CheckLeap(Year)
