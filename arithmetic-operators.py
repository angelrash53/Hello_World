#Given an exclusive price and VAT tax provided by the user,calculate the VAT amount then return the inclusive price.

exclusiveprice=55
VATtax=0.16 #16/100
VATAmount=0
InclusivePrice=0

VATAmount=exclusiveprice*VATtax
InclusivePrice=exclusiveprice+VATAmount

print(InclusivePrice)
