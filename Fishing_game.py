import random
#VARIAVEIS
s = 's'
f = 'f'
r = 'r'
pacus = 0
pirarucus = 0
while True:
    ran = random.randint(0,1)
    rad = random.randint(0,1)
    print(''' ___
_|_|_
 ( )
__|__
__|__\________________
_/_\__\___________
|     _\_        |
|________________|''')
    print('🐟 pacu =',pacus), print('🐟 pirarucu =',pirarucus)
    inp = input('Fishing Game! Insert s to start!')
    if inp == s:
        print(''' ___
_|_|_
 ( )
__|__
__|__\________________
_/_\__\___________
|     _\_        |
|________________|''')
        print('🐟 pacu =',pacus), print('🐟 pirarucu =',pirarucus)
        fish = input('Insert f to fish some fishes')       
    else:
        print('Insert a valid number')
        quit()
    if ran == 1:
        if fish == f:
            if rad == 1:
                print('you fished a pacu')
                print(''' ___
_|_|_
 ( )
__|__🐟
__|___________________
_/_\______________
|                |
|________________|''')
                pacus = pacus + 1
                print('🐟 pacu =',pacus), print('🐟 pirarucu =',pirarucus)
            elif rad == 0:
                print('no pacu fishie :(')
                print(''' ___
_|_|_
 ( ) <-- he is sad now
__|__
__|___________________
_/_\______________
|                |
|________________|''')
    elif ran == 0:
        if fish == f:
            if rad == 1:
                print('you fished a pirarucu')
                print(''' ___
_|_|_
 ( )
__|__🐟
__|___________________
_/_\______________
|                |
|________________|''')
                pirarucus = pirarucus + 1
                print('🐟 pacu =',pacus), print('🐟 pirarucu =',pirarucus)
            elif rad == 0:
                print('no pirarucuru fishie :(')
                print(''' ___
_|_|_
 ( ) <-- he is sad now
__|__
__|___________________
_/_\______________
|                |
|________________|''')
    op = input('wanna fish again? insert r')
    if op != r:
        break
    else:
        continue


