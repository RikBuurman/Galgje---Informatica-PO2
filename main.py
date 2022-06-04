import time
import random

print('\t\t\tGemaakt door Tygo de Wijn en Rik Buurman\n\n\n')
print('Welkom bij Galgje!')
print('  Veel Speelplezier!')

woordenlijst = ['informatiekunde','informatica','spelletje','aardigheidje','scholier','fotografie','waardebepaling','specialiteit','verzekering','universiteit','heesterperk']

time.sleep(1)
             
uitleg = input('\nWil je een uitleg over dit spel? JA / NEE\n') #wil je uitleg?
if uitleg == 'JA':
  print('\nOké, hierbij  de uileg:\n De bedoeling is dat je een woord moet raden met alle letters uit het alfabet, als de letter \n in het woord voor komt dan wordt de letter op de goede plek gezet en dan mag je opnieuw proberen \nen als de letter er niet in zit krijg je 5 kansen tot dat je dood bent ')

if uitleg == 'NEE':
  print('\n Fijn om te horen dat je goed bent voorbereid, laten we beginnen met het spel! \n')

gebruikersnaam = input('\n Vul hier je gebruikersnaam in:\n') #vul je gebruikersnaam in
print('\nGoed om je te zien,', gebruikersnaam) 

spel = input('Wil je een nieuw spel beginnen? JA / NEE\n')
if spel == 'JA':
  kiezen = random.choice(woordenlijst) # Kiezen is het random gekozen woord door de computer
  
  

if spel == 'NEE':
  print('\nTot de volgende keer!')
  quit()