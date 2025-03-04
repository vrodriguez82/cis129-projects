#Module 5 Lab-5
#Victor Rodriguez
#3/4/25
#code asks user how many bottles they collected each day
#then it adds up the total amount of bottles for the week and calculates the payout
#it then asks user if they would like to enter data for another week

#declare local variables
total_bottles = 0
counter = 1
today_bottles = 0 
keep_going = ('y')
total_payout = 0


#loop to run program again
while keep_going == 'y':
    #loop to divide program into weekly segments
    while counter <= 7 :
        today_bottles = int(input('Enter number of bottles for day #%d:' % (counter)))
        total_bottles += today_bottles
        total_payout = total_bottles * 0.1
        counter += 1
    #print end of week info
    print('\nThe total number of bottles collected is %d' % (total_bottles))
    print('The total paid out is $%.1f\n' % (total_payout))
    #oppotunity to enter a new week or terminate the program
    keep_going = input("Do you want to enter another week's worth of data?\n(Enter y or n):")
    #reset counters to not stack info across weeks
    total_bottles = 0
    total_payout = 0
    counter = 1
    
   

