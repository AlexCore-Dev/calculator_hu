# while, try
while True:
    try:
        eredmeny = None
# User input
        num1 = float(input('Adj meg egy szamot: '))
        muvelet = input('Muvelet (+, -, *, /): ')
        num2 = float(input('Adj meg egy masik szamot: '))
# muveletek
        if muvelet == '+':
            eredmeny = num1 + num2
        elif muvelet == '-':
            eredmeny = num1 - num2
        elif muvelet == '*':
            eredmeny = num1 * num2
        elif muvelet == '/':
            if num2 != 0:
                eredmeny = num1 / num2
            else:
                print('Nullaval nem lehet osztani!')
        else:
            print('Ervenytelen muvelet!')
# eredmeny
        if eredmeny is not None:
            print(f'Vegeredmeny: {eredmeny}')
# hibakezeles
    except ValueError:
        print('Nem szamot adtal meg!')
# uj szamitas
    ujra = input('\nSzeretnel uj szamitast vegezni? (i/n): ')
    if ujra != 'i':
        print('Viszlat!')