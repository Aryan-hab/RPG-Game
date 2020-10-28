from Classes.rpgclass import Person, bcolors
from Classes.magic import Spell

# Black Magic:
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 10, 100, "black")
blizzard = Spell("Blizzard", 10, 100, "black")
meteor = Spell("Meteor", 20, 200, "black")
quake = Spell("Quake", 14, 140, "black")

# White Magic:
cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 18, 200, "white")

player = Person(460, 30, 200, 34, [fire, thunder, blizzard, meteor, cure, cura])
enemy = Person(500, 70, 85, 25, [])

run = True

print(bcolors.RED + bcolors.BOLD + 'Fight has started' + bcolors.END)


while run:



    print('===================')
    print("\n", "Attack or you Die", "\n")
    player.choose_action()
    choice = input("Choose action(1, 2 or 3?) :\n ")
    index = int(choice) - 1

    print('Performing', bcolors.BLUE, player.action_name(index), bcolors.END)


    if index == 0:
        dmg = player.generate_dmg()
        enemy_hp = enemy.take_dmg(dmg)
        print('You hit Enemy by', dmg, 'points', '\n')

    elif index == 1:
        player.choose_magic()
        magic_choice = int(input("Choose magic: ")) - 1

        spell = player.magic[magic_choice]
        magic_dmg = spell.generate_dmg()

        current_mp = player.get_mp()

        if spell.cost > current_mp:
            print(bcolors.RED + "Not enough MP" + bcolors.END)
            continue
        if spell.type == "white":
            player.heal(magic_dmg)
            print(bcolors.BLUE + "\n" + spell.name + " heals for " + str(magic_dmg) + " HP." + bcolors.END)
        elif spell.type == "black":
            enemy.take_dmg(magic_dmg)
            print(bcolors.BLUE + "\n" + spell.name + " Deals " + str(magic_dmg) + " Damage." + bcolors.END)

        player.reduce_mp(spell.cost)


    enemy_choice = 1

    enemy_dmg = enemy.generate_dmg()
    player.take_dmg(enemy_dmg)
    print("\n" + bcolors.RED + bcolors.BOLD + "You're under attack", bcolors.END, "\n",
          "Enemy hit you by", enemy_dmg, "points.\n")



    print("-----------------------------")
    print("Enemy Hp: ", bcolors.RED + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + bcolors.END)
    print("Your Hp: ", bcolors.GREEN + str(player.get_hp()) + "/" + str(player.get_max_hp()) + bcolors.END)
    print("Your Mp: ", bcolors.BLUE + str(player.get_mp()) + "/" + str(player.get_max_mp()) + bcolors.END)

    if player.get_hp() <= 0:
        print("You died!")
        break

    elif enemy.get_hp() <= 0:
        print("Enemy died!")
        break




        









