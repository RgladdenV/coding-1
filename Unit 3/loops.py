endOfSchool = 'April 2nd'

# while endofSchool !='May 31st'
#   print('school is in session.')

dismissalHour = 3 
while dismissalHour != 3:
    print('school is in session')

# 1 Kosher
# 2 Vegitarian
# 3 Allergies
# 4 Lactose Intolerant
# 5 Nothing

foodOrder = 1

while foodOrder == 1:
    print('you will get the kosher option')



# While loop: so long as a condition is true, the loop will continue to run

# Create a function with a while loop that will print out a message, so long as we enter the correct number code

def codeToSeeMsg():
    code = input('Please enter code to see message: ')
    while code != '123':
        print('correct message is: have a good day')
    else:
        print('locked out')

    
codeToSeeMsg()


