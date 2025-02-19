#This code ask for input from the user on how many items they would like to puchase
#then gives them a receipt with the information from their purchase
#Ask how many coffees and muffins they are purchasing
num_coffee = input('How many coffees would you like today?\n')
num_muffin = input('How many muffins would you like today?\n')
num_donut = input('How many donuts would you like today?\n')
num_bagel = input('How many bagels would you like today?\n')
num_coffee = int(num_coffee)
num_muffin = int(num_muffin)
num_donut = int(num_donut)
num_bagel = int(num_bagel)

#Calculate the subtotal
price_coffee = (num_coffee * 5)
price_muffin = (num_muffin * 4)
price_donut = (num_donut * 2)
price_bagel = (num_bagel * 3)
cost = price_coffee + price_muffin + price_donut + price_bagel
tax = cost * 0.06
total = cost + tax

#Create and format the receipt
print('***************************************\nMy Coffee and Muffin Shop')
print('Numbers of coffees bought?\n%s\nNumber of muffins bought?\n%d' % (num_coffee,num_muffin))
print('Numbers of donuts bought?\n%s\nNumber of bagels bought?\n%d' % (num_donut,num_bagel))
print('***************************************\n\n***************************************')
print('My coffee and Muffin Shop Receipt')
print('%s Coffees at $5 each: $ %d.00' % (num_coffee,price_coffee))
print('%s Muffins at $4 each: $ %d.00' % (num_muffin,price_muffin))
print('%s Donuts at $2 each: $ %d.00' % (num_donut,price_donut))
print('%s Bagels at $3 each: $ %d.00' % (num_bagel,price_bagel))
print('6%% tax: $ %.2f' % (tax))
print('---------\nTotal: $ %s\n***************************************' % (total))
print('Thank you for shopping with us.We hope to\nsee you again soon.Have a good day!')
