print ('Welcome to Caves and Dragons! Please type your hero\'s name.')
UserHero = input()

print ("""Your were recruited by the Wizard of the West to eliminate the whole
goblin population in Morath, your home country. As a test, the wizard has placed
you in a cave full of traps and unknown dangers. But before you begin, we must
build your character.""")

print ("""Type your race. Use all lowercase letters. You can be a elf, a human,
a dwarf, or a troll. Each of these races has their limits to specific classes.
For example, if you are atroll or a dwarf, you can't be a wizard or a cleric as
a class.""")
UserRace = input()

print (""" Now that you have picked your race,""",UserHero,
""",you need to chose a class. There are four classes you can chose from. Cleric,
wizard, warrior, and theif are those four clases. They each have their pros and
cons. I will go into dephth on those later. There are also resitrictions. Dwarfs
and trolls can't be clerics or wizards, and a elf cant be a theif. Type your
class, please use only lowercase letters.""")
UserClass = input()

if UserRace == 'troll' and UserClass == 'wizard':
    print ('A troll can\'t be a wizard! Please select another class.')
    UserClass = input()

if UserRace == 'troll' and UserClass == 'cleric':
    print ('A troll can\'t be a cleric! Please select another class.')
    UserClass = input()

if UserRace == 'dwarf' and UserClass == 'wizard':
    print ('A dwarf cant\'t be a wizard! Please select another class.')
    UserClass = input()

if UserRace == 'dwarf' and UserClass == 'cleric':
    print ('A dwarf cant\'t be a cleric! Please select another class.')
    UserClass = input()

if UserRace == 'elf' and UserClass == 'theif':
    print ('An elf can\'t be a theif! Please select another class.')
    UserClass = input()

if UserRace == 'elf':
    print ('Congradulations! You are an elf', UserClass,'! Now I can tell you your powers, which are decided by your class and race.')

if UserRace == 'troll' or 'human' or 'dwarf':
    print ('Congradulations! You are a',UserRace, UserClass,'! Now I can tell you your powers, which are decided by your class and race.')




