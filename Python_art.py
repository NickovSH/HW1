#Letter H output function
def CharacterH(c, thickness):
    #TopBar
    for i in range(thickness):
        print((c*thickness) + (c*thickness).center(thickness*5))

    #MiddleBar
    for i in range((thickness+1)//2):
        print(c*thickness*4)

    #BottomBar
    for i in range(thickness):
        print((c * thickness) + (c * thickness).center(thickness * 5))

#Letter T output function
def CharacterT(c, thickness):
    #HorizontalBar
    for i in range((thickness+1)//2):
        print(c*thickness*4)

    #VerticalBar
    for i in range(thickness):
        print((c*thickness).center(thickness*4))


#Letter U output function
def CharacterU(c, thickness):
    #VerticalBar
    for i in range(thickness):
        print((c*thickness)+(c*thickness).center(thickness*5))

    #HorizontolBar
    for i in range((thickness+1)//2):
        print(c*thickness*4)

def main():
    print('\nExercise 2')
    try:
        print('Enter character: \'U\', \'T\', \'H\' ')
        c = str(input())
        print('Enter thickness')
        thickness = int(input())
    except Exception:
        print('You entered an invalid letter or number. Try again')
        exit()

    if c=='H':
        CharacterH(c, thickness)
    elif c=='U':
        CharacterU(c, thickness)
    elif c=='T':
        CharacterT(c, thickness)
    else:
        print('You entered an invalid letter. Try again')
        exit()
