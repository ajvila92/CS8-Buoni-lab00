# Angelo Vila
# May 27, 2018

def pay(hourlyWage, nHours):
	if hourlyWage <= 40:
		return hourlyWage*nHours
	else:
		return hourlyWage*40 + (nHours - 40)*hourlyWage*nHours

def monthlyPayment(P, r, n):
	numerator = ( P*(1 + r/12)**(12*n) )*(r/12) 
	denominator = ( (1 + r/12)**(12*n) ) - 1
	return numerator/denominator

def printBalance(P, r, n):
	denominator = ( (1 + r/12)**(12*n) ) - 1
	for i in range(n + 1):
		numerator =  P*( (1 + r/12)**(12*n) - (1 + r/12)**(12*i) )
		principal = numerator/denominator
		output = 'Year: {0:3} Balance: {1}'.format(i, principal)
		print(output)
