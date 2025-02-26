#Module 4 Lab-4
#Victor Rodriguez
#2/25/25
#program gets user input entering store sales information and calculates store bonus, 
#employee bonus and a congratulations message if both max bonuses were acheived 

#declare local variables
monthlySales = 0 #monthly sales amount
storeAmount = 0 #store amount bonus
empAmount = 0 #employee bonus amount
salesIncrease = 0 #percent of sales increase
prompt = """. . ."""

#This code gets the monthly sales
monthlySales = float(input('Enter Monthly Sales $'))

#This code determines the store bonus
if monthlySales >= 110000:
    storeAmount = 6000
elif monthlySales >= 100000:
    storeAmount = 5000
elif monthlySales >= 90000:
    storeAmount = 4000
elif monthlySales >= 80000:
    storeAmount = 3000
else: 
    storeAmount= 0

#This code gets the percent of increase in sales
salesIncrease = float(input('Enter percent of sales increase:'))
salesIncrease = salesIncrease / 100

#This code determines the employee bonus
if salesIncrease >= .05:
    empAmount = 75
elif salesIncrease >= .04:
    empAmount = 50
elif salesIncrease >= .03:
    empAmount = 40
else:
    empAmount = 0

#This code prints the bonus information
print('The store bonus amount is $%.0f'%storeAmount)
print('The employee bonus amount is $%.0f'%empAmount)
if (storeAmount == 6000) and (empAmount == 75):
    print('Congrats! You have reached the highest bonus amounts possible!')