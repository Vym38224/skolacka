number= input("Zadej číslo dne:")
number = int(number)
month=()

if number >= 1 and number <= 365:
    if number in range(1,365,7): 
        day = 1
    if number in range(2,365,7): 
        day = 2
    if number in range(3,365,7): 
        day = 3
    if number in range(4,365,7): 
        day = 4
    if number in range(5,365,7): 
        day = 5
    if number in range(6,365,7): 
        day = 6
    if number in range(7,365,7): 
        day = 7
    if number == 365: 
        day = 1

    if number >= 1 and number <= 31:
        month = 1
    if number >= 32 and number <= 59:
        month = 2
    if number >= 60 and number <= 80:
        month = 3
    if number >= 81 and number <= 110:
        month = 4
    if number >= 111 and number <= 141:
        month = 5
    if number >= 142 and number <= 171:
        month = 6
    if number >= 172 and number <= 202:
        month = 7
    if number >= 203 and number <= 233:
        month = 8
    if number >= 234 and number <= 263:
        month = 9
    if number >= 264 and number <= 294:
        month = 10
    if number >= 295 and number <= 324:
        month = 11
    if number >= 325 and number <= 365:
        month = 12
else:
    day = 0

match day:
    case 1: print("Den v týdnu:neděle")
    case 2: print("Den v týdnu:pondělí")
    case 3: print("Den v týdnu:úterý")
    case 4: print("Den v týdnu:středa")
    case 5: print("Den v týdnu:čtvrtek")
    case 6: print("Den v týdnu:pátek")
    case 7: print("Den v týdnu:sobota")
    case _: print("Chyba:Zadáno špatné číslo, vybírejte z intervalu <1,365>")

match month:
    case 1: print("Měsíc:leden")
    case 2: print("Měsíc:únor")
    case 3: print("Měsíc:březen")
    case 4: print("Měsíc:duben")
    case 5: print("Měsíc:květen")
    case 6: print("Měsíc:červen")
    case 7: print("Měsíc:červenec")
    case 8: print("Měsíc:srpen")
    case 9: print("Měsíc:září")
    case 10: print("Měsíc:říjen")
    case 11: print("Měsíc:listopad")
    case 12: print("Měsíc:prosinec")
    
    
    

