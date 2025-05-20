def keepYourHeadUp():
    print('Hello Im here to check up on you and see if youre doing well.')
    userAnswer = input('How are you feeling? Good or Bad?')
    if userAnswer == 'Good':
        print('Thats great!')
    if userAnswer == 'Bad':
            print('Im sorry to hear that, I can help you.')
    userResponse = input('Do you want some form of reassurance? Yes or No?')
    if userResponse == 'Yes':
            print('Youre special, everyone is special and everything happens for a reason so just keep your head up! Bye!')
    if userResponse == 'No':
            print('Well okay then, stay safe, see ya!')


keepYourHeadUp()