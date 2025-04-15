# Szamologep v0.2

# Muveletek
def osszead(a, b):
    return a + b

def kivon(a, b):
    return a - b

def szor(a, b):
    return a * b

def oszt(a, b):
    if b != 0:  # 0-al valo osztas elleni vedelem
        return a / b
    else:
        print('Nullaval nem lehet osztani')

# A fo program
def szamologep():
    while True:
        try:
            a = int(input('Adj meg egy szamot: '))
            muvelet = input('Muvelet: ')
            b = int(input('Adj meg egy masik szamot: '))
        except ValueError:  # Hibakeyeles, csak szamot adhat meg a felhasznalo
            print('Csak szamot adhatsz meg')
            continue  # Hiba eseten visszateres a szam bekereshez
        
        # Muveletek elvegzese
        if muvelet == "+":
            eredmeny = osszead(a, b)
            print(f'Eredmeny: {eredmeny}')

        elif muvelet == '-':
            eredmeny = kivon(a, b)
            print(f'Eredmeny: {eredmeny}')

        elif muvelet == '*':
            eredmeny = szor(a, b)
            print(f'Eredmeny: {eredmeny}')
        
        elif muvelet == '/':
            eredmeny = oszt(a, b)
            print(f'Eredmeny: {eredmeny}')
        else:
            print('Ervenztelen muvelet')

szamologep()