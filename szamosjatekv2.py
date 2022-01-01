import random

# szám kitalálos játék második verzió

print('Kérem válasszon lehetőséget!\n1. A gép találki 1 és 10 között\n2. Ön adja meg a minimum és maximim értéket!')
valasz = int(input('Válasza: '))

if valasz == 1:
    print('Ön az 1. lehetőséget választotta!\nEgy pillanat kezdheti a tippeket!')
    gszam = random.randint(1, 10)
    tipp = 0
    tippek = 0
    while tipp != gszam:
        if tipp < gszam:
            print('A szám nagyobb kérem próbálja újra!')
            tipp = int(input('\nKérem az új tippet! Tipp: '))
            tippek += 1
        else:
            print('A szám kisebb kérem próbálja újra!')
            tipp = int(input('\nKérem az új tippet! Tipp: '))
            tippek += 1
    print(f'A szám helyes! A megoldás: {gszam}! A tippek száma: {tippek}')


else:
    print('Ön a 2. lehetőséget választotta! Kérem adja a minimum és a maximum értéket!')
    minimum = int(input('Minimum: '))
    maximum = int(input('Maximum: '))
    if (
            minimum == maximum or maximum == minimum + 1 or maximum == minimum + 2
            or maximum == minimum + 3 or maximum == minimum + 4):
        print('Nem csalhat! Kérem adjon meg új számokat! Legalább öttel kell nagyobbnak lenni a maximumnak!')
        minimum = int(input('Minimum: '))
        maximum = int(input('Maximum: '))
        if (
                minimum != maximum or maximum != minimum + 1 or maximum != minimum + 2 or maximum != minimum + 3
                or maximum != minimum + 4):
            print('Rendben a számok most már helyesek! Indul a generálás!')
            gszam1 = random.randint(minimum, maximum)
            tipp1 = 0
            tippek2 = 0
            while gszam1 != tipp1:
                if tipp1 < gszam1:
                    print('A szám nagyobb kérem próbálja újra!')
                    tipp1 = int(input('\nKérem az új tippet! Tipp: '))
                    tippek2 += 1
                else:
                    print('A szám kisebb kérem próbálja újra!')
                    tipp1 = int(input('\nKérem az új tippet! Tipp: '))
                    tippek2 += 1
            print(f'A szám helyes! A megoldás: {gszam1}! A tippek száma: {tippek2}')

    else:
        minimum = minimum
        maximum = maximum
        gszam1 = random.randint(minimum, maximum)
        tipp1 = 0
        tippek2 = 0
        while gszam1 != tipp1:
            if tipp1 < gszam1:
                print('A szám nagyobb kérem próbálja újra!')
                tipp1 = int(input('\nKérem az új tippet! Tipp: '))
                tippek2 += 1
            else:
                print('A szám kisebb kérem próbálja újra!')
                tipp1 = int(input('\nKérem az új tippet! Tipp: '))
                tippek2 += 1
        print(f'A szám helyes! A megoldás: {gszam1}! A tippek száma: {tippek2}')
