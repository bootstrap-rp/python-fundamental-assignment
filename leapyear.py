def leapyear(year):
    if ( year % 4 == 0 and year % 100 != 0 ) or ( year % 400 == 0 ):
        print("It is a leapyear")
    else:
        print("It's not a leapyear")

year=int(input("Enter the Year:"))
leapyear(year)            