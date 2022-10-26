def Rug_designer():

    print('\nExercise 5')
    try:
        print('Enter height')
        height = int(input())
        width = height*3
    except Exception:
        print('You entered an invalid number. Try again')
        exit()

    for i in range(1, height, 1):
        print(('$'*i).center(width,'*'))

    print('Like'.center(width,'o'))

    for i in range(height-1, 0, -1):
        print(('$'*i).center(width, '*'))