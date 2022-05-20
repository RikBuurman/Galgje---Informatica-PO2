
print('\t\t\tGemaakt door Tygo de Wijn en Rik Buurman\n\n\n')
print('Welkom bij Galgje!')
print('  Veel Speelplezier!')

Woordenlijst = ['informatiekunde','informatica','spelletje','aardigheidje','scholier','fotografie','waardebepaling','specialiteit','verzekering','universiteit','heesterperk']
 
               
uitleg = input('\nWil je uitleg van het spel Galgje? JA / NEE\n')
if uitleg == 'JA':
  print('\nOké laten we beginnen! \n De bedoleing is dat je een woord moet raden met alle letters uit het alfabet, als de letter \n in het woord voor komt en als de letter op de goede plek staat dan mag je opnieuw proberen \nen als de letter er niet in zit krijg je 5 kansen tot dat je dood bent ')

if uitleg == 'NEE':
  print('\n Fijn om te horen dat je goed bent voorbereidt, laten we beginnen met het spel! \n')

gebruikersnaam = input('\n Vul hier je gebruikersnaam in:\n')
print('\nGoed om je te zien,', gebruikersnaam)

spel = input('Wil je een nieuw spel beginnen? JA / NEE\n')
if spel == 'JA':
##start spel
  print('*start spel*')

if spel == 'NEE':
  print('\nTot de volgende keer!')
  quit()


