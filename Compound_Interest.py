def compound_interest(principal, rate, time):
	Amount = principal * (pow((1 + rate / 100), time))
	CI = Amount - principal
	print("%.2f"%( CI))
a=int(input())
b=int(input())
c=int(input())
compound_interest(a,b,c)
