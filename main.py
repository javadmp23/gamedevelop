from classes.game import Person, bcolors
from classes.magic import Spell

#jadohaye-siyah
fire = Spell ("Fire",10,100,"black")
thunder = Spell ("thunder",10,100,"black")
blizzard = Spell ("blizzard",10,100,"black")
meteor = Spell ("meteor",20,200,"black")
quake = Spell ("quake",14,140,"black")

#jadohaye-sefid
cure = Spell ("cure",12,120,"white")
cura = Spell ("cura",18,200,"white")

#afrade-bazi
player = Person(460, 65, 60, 34, [fire , thunder,meteor,cure,cura])
enemy = Person(1200, 65, 45, 25,[])

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "enemy attacks" + bcolors.ENDC)

while running:
    print("====================")
    player.choose_action()
    choice = input("choose action:")
    index = int(choice) - 1

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for", dmg, "points of damage.")
    elif index == 1:
        player.choose_magic()
        magic_choice = int(input("choose magic:")) - 1


        spell = player.magic[magic_choice]
        magic_dmg = spell.generate_damage()


        current_mp = player.get_max_mp()

        if spell.cost > current_mp:
            print(bcolors.FAIL + "\n not enough mp \n" + bcolors.ENDC)
            continue

        player.reduce_mp(spell.cost)
        enemy.take_damage(magic_dmg)
        print(bcolors.OKBLUE + "\n" + spell.name + "deals", str(magic_dmg), "points of damage" + bcolors.ENDC)

    enemy_choice = 1

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacks for", enemy_dmg)

    print("---------------------")
    print("enemy hp", bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + bcolors.ENDC + "\n")
    print("your hp:", bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_max_hp()) + bcolors.ENDC)
    print("your mp:", bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_max_mp()) + bcolors.ENDC + "\n")

    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "you win" + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + "your enemy has defeated you!" + bcolors.ENDC)
        running = False
