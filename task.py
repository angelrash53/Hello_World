
#Given an inclusive price and VAT tax provided by the user,
#calculate the VAT amount then return the exclusive price.

inclusiveprice=60
vattax=0.16
vatamount=0
exclusiveprice=0

vatamount=inclusiveprice*vattax
exclusiveprice=inclusiveprice-vatamount
print(exclusiveprice)


def calculatevat():
    exclusiveprice=53
    vattax=0.16
    vatamount=0
    inclusiveprice=0

    vatamount=exclusiveprice*vattax
    inclusiveprice=exclusiveprice+vatamount

    return inclusiveprice

print(calculatevat())

def calculatevat(exclusiveprice,vattax):
    vatamount=exclusiveprice*vattax
    inclusiveprice=exclusiveprice+vatamount
    return inclusiveprice
print (calculatevat(53,0.16))


def userInputs():
    exclusiveprice=float(input("Enter the exclusive amount"))
    vattax=float(input("Enter vattax"))
    inclusiveprice=calculatevat(exclusiveprice,vattax)

    print(inclusiveprice)

userInputs()

    