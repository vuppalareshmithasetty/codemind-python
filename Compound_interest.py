def compound_interest(principal, rate, time):
	Amount = principal * (pow((1 + rate / 100), time))
	CI = Amount
	print('%.2f' % CI)
#	print( round(CI, 2))
principal,rate,time = map(int,input().split())
compound_interest(principal,rate,time)