stundenlohn = input("Bitte gebe deinen Stundenlohn ein: ")
tag = 8*int(stundenlohn)
monat = tag * 20
year = monat *12

print("Dein Stundenlohn beträgt " + str(stundenlohn) + "$")
print('Du verdienst ' + str(tag) + '$ pro Tag')
print("Du verdienst pro Monat " + str(monat) + "$")
print("Du verdienst ein Jahresgehalt von " + str(year) + "$")
