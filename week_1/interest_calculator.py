while True:
    name = input('What is your name ')
    calculation = input(f'''
    Welcome to the Interest Calculator {name}, what would you like to calculate?
    For Simple Interest, type SI
    For Compound Interest, type CI
    For Annuity Plan, type AP
    '''
    ).upper()


    if calculation == 'SI' or calculation == 'SIMPLE INTEREST':
        principal = int(input('What is your principal? '))
        rate = int(input('What is your interest rate in %? Please enter only a number else my program will crash '))
        time = int(input('How long was it lent for? '))
        Amount = principal * (1 + ((rate/100)*time))
        print (f'The Amount for the Simple Interest is {Amount}')
        break

    elif calculation == 'CI' or calculation == 'COMPOUND INTEREST':
        principal = int(input('What is your principal? '))
        rate = int(input('What is your interest rate in %? Please enter only a number else my program will crash '))
        number = int(input('What is the number of times interest would be taken '))
        time = int(input('How long was it lent for? '))
        Amount = principal * (1 + (rate/number)) **(number*time)
        print (f'The Amount for the Compound Interest is {Amount}')
        break

    elif calculation == 'AP' or calculation == 'ANNUITY PLAN':
        pmt = int(input('What is the periodic payment amount '))
        rate = int(input('What is your interest rate in %? Please enter only a number else my program will crash '))
        number = int(input('What is the number of times interest would be taken '))
        time = int(input('How long was it lent for? '))
        Amount = pmt * (((1 + (rate/number)) **(number*time) - 1) / (rate/number))
        print (f'The Amount for the Annuity Plan is {Amount}')
        break

    else:
        print('You have entered an invalid input, kindly input a correct value')