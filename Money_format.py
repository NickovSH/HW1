def Money_format():
    print('\nExercise 4')
    try:
        print('Enter the  number')
        number = float(input())
        print("{:,.2f}".format(number))
    except Exception:
        print('You entered an invalid number. Try again')
        exit()