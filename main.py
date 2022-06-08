import time
import random

print('\t\t\tGemaakt door Tygo de Wijn en Rik Buurman\n\n\n')
print('Welkom bij Galgje!')
print('  Veel Speelplezier!')

woordenlijst = ['informatiekunde','informatica','spelletje','aardigheidje','scholier','fotografie','waardebepaling','specialiteit','verzekering','universiteit','heesterperk'] #Lijst met woordjes waaruit de computer later random kiest


time.sleep(1) #Wacht 1 seconde
             
uitleg = input('\nWil je een uitleg over dit spel? JA / NEE\n') #wil je uitleg?
if uitleg == 'JA':
  print('\nOké, hierbij  de uileg:\n De bedoeling is dat je een woord moet raden met alle letters uit het alfabet, als de letter \n in het woord voor komt dan wordt de letter op de goede plek gezet en dan mag je opnieuw proberen \nen als de letter er niet in zit krijg je 5 kansen tot dat je dood bent ')

if uitleg == 'NEE': 
  print('\n Fijn om te horen dat je goed bent voorbereid, laten we beginnen met het spel! \n')

gebruikersnaam = input('\n Vul hier je gebruikersnaam in:\n') #vul je gebruikersnaam in
print('\nGoed om je te zien,', gebruikersnaam) 

def galgje(): #Functie voor het spel zelf
  pogingen = 0 #Hoe vaak je geprobeerd hebt
  
  kiezen = random.choice(woordenlijst) #Kiezen is het random gekozen woord door de computer
  woord = len(kiezen) * '-' #Zet het aantal streepjes (_) neer t.o.v. het aantal letters van het woord
  print(f'\n\n{woord}')
  while pogingen < 5: #Controle of je niet te veel pogingen hebt (max 5)
    if kiezen == woord: # Is wat je hebt geraden gelijk aan het woord?
      print('\nGefeliciteerd, je hebt het woord geraden!')   
      print('--------------------------------------------------------------')
      break 

    raden = input('Type een letter\n')[0]
    if raden in kiezen: #Is de letter poging aanwezig in het woord?
       for i in range(len(kiezen)):
         if kiezen[i] == raden:
          letterlijst = list(woord)
          letterlijst[i] = raden 
          woord = ''.join(letterlijst)        
    else:
      pogingen += 1 #Als de letter niet aanwezig is, gaat er 1 poging bij
    print(woord) 

    if pogingen >= 5:
      print(f'\nHelaas, je beurten zijn op\n Het woord was: {kiezen}')

    if pogingen == 1:
      print('\n\nGalgje 1\n\n') #Print het eerste plaatje, wanneer je 1 foute poging hebt

    if pogingen == 2:
      print('\n\nGalgje 2\n\n') #Print het eerste plaatje, wanneer je 2 foute poging hebt

    if pogingen == 3:
      print('\n\nGalgje 3\n\n') #Print het eerste plaatje, wanneer je 3 foute poging hebt

    if pogingen == 4:
      print('\n\nGalgje 4\n\n') #Print het eerste plaatje, wanneer je 4 foute poging hebt

    if pogingen == 5:
      print('\n\nGalgje 5\n\n') #Print het eerste plaatje, wanneer je 5 foute poging hebt
 
def spelen(): #Functie voor herhalen van het spel
  while True:
    spel = input('\nWil je een nieuw spel starten? JA / NEE\n')
    if spel.upper() == 'JA':
      galgje() #De functie galgje wordt afgespeeld wanneer deze if statement True is
    else:
      print('\nTot de volgende keer!') 
      quit() #De console stopt wanneer de if statemnt False is 
spelen() 
        