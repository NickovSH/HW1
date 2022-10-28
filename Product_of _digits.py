#The program finds the product of all digits of a number except zero

def Product():
    print('\nExercise 6 - Product')
    print('Enter the number = ')
    digit = input()
    product_digit = 1

    for i in digit:
        if int(i) != 0:
            product_digit = product_digit*int(i)
        else:
            product_digit

    print(f'The product of the digits of the number {digit} is {product_digit}'.format(digit=digit, product_digit=product_digit))


Product()