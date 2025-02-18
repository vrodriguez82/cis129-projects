#This code ask for input from the user on how many items they would like to puchase
#then gives them a receipt with the information from their purchase
#Ask how many coffees and muffins they are purchasing
num_coffee = input('How many coffees would you like today?\n')
num_muffin = input('How many muffins would you like today?\n')
num_coffee = int(num_coffee)
num_muffin = int(num_muffin)
#Calculate the subtotal
price_coffee = (num_coffee * 5)
price_muffin = (num_muffin * 4)
cost = price_coffee + price_muffin
tax = cost * 0.06
total = cost + tax
#Create and format the receipt
print('***************************************\nMy Coffee and Muffin Shop')
print('Numbers of coffees bought?\n%s\nNumber of muffins bought?\n%d' % (num_coffee,num_muffin))
print('***************************************\n\n***************************************')
print('My coffee and Muffin Shop Receipt')
print('%s Coffee at $5 each: $ %d.00' % (num_coffee,price_coffee))
print('%s Muffin at $4 each: $ %d.00' % (num_muffin,price_muffin))
print('6%% tax: $ %.2f' % (tax))
print('---------\nTotal: $ %s\n***************************************' % (total))