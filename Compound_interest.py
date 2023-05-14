def compound_interest(principal, rate, time):
    Amount = principal * (pow((1 + rate / 100), time))
    CI = Amount
    print("%.2f"%(CI))
  
  
principal,rate,time=map(int,input().split())
compound_interest(principal,rate,time)
  