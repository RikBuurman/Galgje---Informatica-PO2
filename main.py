import time #Importeren van tijd, voor het tijdelijk 'op de wacht zetten' van code
import random #Importeren van random, zodat de code random een woord uit de lijst kan selecteren
import string

print('\t\t\tGemaakt door Tygo de Wijn en Rik Buurman\n\n\n')
print('Welkom bij Galgje!') #Spelintroductie
print('  Veel Speelplezier!') 

woordenlijst = ['informatiekunde','informatica','spelletje','aardigheidje','scholier','fotografie','waardebepaling','specialiteit','verzekering','universiteit','heesterperk'] #Lijst met woordjes waaruit de computer later random kiest

time.sleep(1) #Wacht 1 seconde
             
uitleg = input('\nWil je een uitleg over dit spel? JA / NEE\n') #wil je uitleg?
if uitleg == 'JA':
  time.sleep(0.5)
  print('\nOké, hierbij de uileg:\n De bedoeling van dit spel is dat je een woord raadt, een woord dat de computer kiest. \n Je hebt alle letters uit het alfabet tot je beschikking, elke poging kan je 1 letter \n proberen te raden.\n Wanneer de letter die je gokt aanwezig is in het woord, ga je verder totdat je het woord \n volledig hebt geraden. \n Je hebt 5 pogingen, elke letter die niet aanwezig is in het woord, zorgt voor -1 poging. \n Al zijn al je pogingen op, ben je af en kan je helemaal opnieuw beginnen.')
  print('\n Hopelijk is alles duidelijk nu, laten we verdergaan met het kiezen van je gebruikersnaam!')
 #Uitleg over galgje

if uitleg == 'NEE':
  time.sleep(0.5)
  print('\n Fijn om te horen dat je goed bent voorbereid, laten we beginnen met je gebruikersnaam! \n')

time.sleep(0.5)
gebruikersnaam = input('\n Vul hier je gebruikersnaam in:\n') #vul je gebruikersnaam in
print('\nGoed om je te zien,', gebruikersnaam) 

def galg_print(poging): #Functie voor de plaatjes van galgje 
  galgjes = ['________\n|      |\n|      \n|     \n|      \n|     \n|______\n', #Plaatje bij 1 poging
             '________\n|      |\n|      o\n|     \n|      \n|     \n|______\n', #Plaatje bij 2 pogingen
             '________\n|      |\n|      o\n|     \ /\n|      \n|     \n|______\n', #Plaatje bij 3 pogingen
             '________\n|      |\n|      o\n|     \ /\n|      |\n|     \n|______\n', #Plaatje bij 4 pogingen
             '________\n|      |\n|      o\n|     \ /\n|      |\n|     / \\\n|______\n'] #Plaatje bij 5 pogingen
  
  if poging == 1:
    return galgjes[0]  
    
  if poging == 2:
    return galgjes[1]

  if poging == 3:
    return galgjes[2]

  if poging == 4:
    return galgjes[3]

  if poging == 5:
    return galgjes[4] 

def galgje(): #Functie voor het spel zelf
  pogingen = 0 #Hoe vaak je geprobeerd hebt
  foute_letters = []
  
  kiezen = random.choice(woordenlijst) #Kiezen is het random gekozen woord door de computer
  woord = len(kiezen) * '-' #Zet het aantal streepjes (_) neer t.o.v. het aantal letters van het woord
  print(f'\n\n{woord}')
  while pogingen < 5: #Controle of je niet te veel pogingen hebt (max 5)
    if kiezen == woord: # Is wat je hebt geraden gelijk aan het woord?
      time.sleep(1)
      print('\nGefeliciteerd, je hebt het woord geraden!')     
      print('--------------------------------------------------------------')
      break 

    raden = input('Type een letter\n').lower()
    alfabet = string.ascii_lowercase
    if raden in alfabet and len(raden) == 1:
      if raden in kiezen: #Is de letter poging aanwezig in het woord?
        for i in range(len(kiezen)):
          if kiezen[i] == raden:
            letterlijst = list(woord)
            letterlijst[i] = raden 
            woord = ''.join(letterlijst)  
      else:
        foute_letters.append(raden)
        foute_letters.sort()
        pogingen += 1 #Als de letter niet aanwezig is, gaat er 1 poging bij     
    else:
      time.sleep(1)
      print('\nInvoer is niet correct (Gebruik alleen letters uit het alfabet; Maximaal 1 letter)\n')
      pogingen += 1

    
    print(woord) 
    time.sleep(0.5) #Code wacht een halve seconde
    print(f'\nGeprobeeerde foute Letters: {foute_letters}\n')

    if pogingen == 1: 
      time.sleep(0.5) #Code wacht een halve seconde
      print(galg_print(pogingen)) #Print het plaatje als er 1 foute poging gedaan is
      
    if pogingen == 2:
      time.sleep(0.5) #Code wacht een halve seconde
      print(galg_print(pogingen)) #Print het bijbehorende plaatje als er 2 foute pogingen gedaan zijn
      
    if pogingen == 3:
      time.sleep(0.5) #Code wacht een halve seconde
      print(galg_print(pogingen)) #Print het bijbehorende plaatje als er 3 foute pogingen gedaan zijn
      
    if pogingen == 4:
      time.sleep(0.5) #Code wacht een halve seconde
      print(galg_print(pogingen)) #Print het bijbehorende plaatje als er 4 foute pogingen gedaan zijn 
      
    if pogingen == 5:
      time.sleep(1) #Code wacht 1 seconde
      print(galg_print(pogingen)) #Print het eindeplaatje als er 5 foute pogingen gedaan zijn
      print(f'\nHelaas, je beurten zijn op\n Het woord was: {kiezen}') #Verloren-bericht, aangeven van het woord

def spelen(): #Functie voor herhalen van het spel
  while True:
    spel = input('\nWil je een nieuw spel starten? JA / NEE\n')
    if spel.upper() == 'JA':
      galgje() #De functie galgje wordt afgespeeld wanneer deze if statement True is
    else:
      print('\nTot de volgende keer!') 
      quit() #De console stopt wanneer de if statemnt False is 
spelen() 
        