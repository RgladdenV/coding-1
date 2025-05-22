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


# if the word is correct, end the loop

def wordGuessingGame():
    print('guess the word')
    print('circular object on a car, comes in 2 pairs')
    userGuess = input('What is your guess?')
    while userGuess != 'wheel':
        print('Try again')
        userGuess = input('What is your guess?')
    else:
        print("Correct!")

wordGuessingGame()


# For loops - are a type of loop that runs specific conditions on a list of data

# List - a collection data type for storing different types of data

bobby_Coding = ['Bobby, 16, True, 96.6']
david_Coding = ['Bobby, 15, False, 85.9']

blPoweSchool_Class = [bobby_Coding, david_Coding]

class BLHS:
    grade 9: [student]
    grade 10:[]
    grade 11:[]


class student:
    name:''
    grade:
    classes:



# A list is identified by square brackets

# studentQuiz() = round brackets means it is a function
# studentQuiz[] = square brackets means it is a list

studentQuiz = [90, 100, 70, 85, 65, 70, 82, 90]

# we can access values in a list using the list index system.

# when we access a list, the first piece of data in the list is always identified as being in position zero(0). List always start their count in zero, ex: 0, 1, 2, 3.

print(studentQuiz[2])


# Basic structure (syntax) for creating a for loop

for x in studentQuiz:
    print(x + 5)