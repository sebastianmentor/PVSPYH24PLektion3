lista_med_namn = ['Sebastian', 'Kalle', 'Erik', 'Ida', 'Malin']

namn = input('Hej! Vänligen skriv in ditt namn: ')
cap_namn = namn.capitalize()
# Sebastian == sebastian -> False

if cap_namn in lista_med_namn:
    print('Hej', namn ,'du är min klasskamrat!')

    position = lista_med_namn.index(cap_namn) + 1

    print('Du är plats', position,'i kö!')
    if namn == cap_namn:
        print('Du skrev in ditt namn korrekt!')
    else:
        print('Du skrev ditt namn på ett katastrofalt sett!!!!')
else:
    print('Hej främling!!! Du är inte min klasskamrat')