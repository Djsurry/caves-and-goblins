# make some lists of the allowed races and classes
races = ['elf', 'dwarf', 'human', 'troll']
classes = ['wizard', 'cleric', 'warrior', 'thief']

# make a 'dictionary' where we can look up a race and get a list of which
# classes are not allowed
illegal = {
    'troll': ['wizard', 'cleric'],
    'dwarf': ['wizard', 'cleric'],
    'elf'  : ['thief']
}

print ('Welcome to Caves and Dragons! Please type your hero\'s name.')
UserHero = input()

print ("""Your were recruited by the Wizard of the West to eliminate the whole
goblin population in Morath, your home country. As a test, the wizard has placed
you in a cave full of traps and unknown dangers. But before you begin, we must
build your character.""")

print ("""Type your race. You can be a elf, a human,
a dwarf, or a troll. Each of these races has their limits to specific classes.
For example, if you are a troll or a dwarf, you can't be a wizard or a cleric as
a class.""")
while 1:                                    # keep asking until they give a good one
    UserRace = input().lower()              # make their answer lower case
    if UserRace not in races:
        print("Sorry, I don't understand '%s', please try again."%UserRace)
        continue
    else:
        break       # stop asking after a good answer

print ("""Now that you have picked your race,""",UserHero,""",you need to chose
a class. There are four classes you can chose from. Cleric,
wizard, warrior, and thief are those four clases. They each have their pros and
cons. I will go into depth on those later. There are also resitrictions. Dwarfs
and trolls can't be clerics or wizards, and a elf cant be a thief. Type your
class.""")
while 1:
    UserClass = input().lower()
    if UserClass not in classes:
        print("Sorry, I don't understand '%s', please try again."%UserClass)
        continue
    elif UserClass in illegal.get(UserRace, []):
        print("Sorry, a %s can't be a %s! Please select another class."
                %(UserRace, UserClass))
        continue
    else:
        break       # stop asking after a good answer        

if UserRace == 'elf':
    print ("""Congratulations! You are an elf""", UserClass,"""! Now I can tell you
your powers, which are decided by your class and race.""")

if UserRace in ['troll', 'human', 'dwarf']:
    print ("""Congratulations! You are a""",UserRace, UserClass,"""! Now I can tell
you your powers, which are decided by your class and race.""")

if UserRace == 'elf':
    print ("""Since you are an elf, you get certain boosts. If you are carrying a bow,
you have a better chance of hitting your opponent. You also have a better chance of
getting away or hiding from and enemy that is too powerful for you to beat.""")

if UserRace == 'troll' :
    print ("""Since you are a troll, you get certain boosts. If you are fighting a
monster where no ranged weapons are used, you have a better chance of winning since you
have a strengh bounus. You also have extra HP because of your toughness.""")

if UserRace == 'dwarf':
    print ("""Since you are a dwarf, when you are using an ax or a club you deal 2X as
much damage as if you were a different race. Also, you have the ability to mine in caves
in search for gold or diamond.""")

if UserRace == 'human':
    print ("""Since you chose human as your race, you have the ability to out-wit your
enemy. Also, you can presuade people and even monsters to do what you want them to (for
instance, you could convince a king to let you and your friends stay in his castle).""")

           



