import random

#Player stats
player_health = 100
player_attack_range = 2, 11

#Monster stats
monster_health = 90
monster_attack_range = 6, 10

#health
heal_potion = 1, 9

while True:
    option = input("Would you like to Attack or Heal? ")
#Player Attacks
    if option.lower().strip() == "attack":
        print("----You have chosen to attack----")
        monster_health = monster_health - random.randint(player_attack_range[0], player_attack_range[1])
        print("Monster's Health = ", monster_health, "/", 90)
#Monster Attacks
        print("----The Monster has attacked----")
        player_health = player_health - random.randint(monster_attack_range[0], monster_attack_range[1])
        print("Player Health = ",player_health, "/", 100)
#Who wins or loses
        if player_health <= 0:
            print("You lost")
            break
        elif monster_health <= 0:
            print("You Won")
            break
#Player Heals
    elif option.lower().strip()  == "heal":
        print("----You have chosen to heal----")
        player_health = player_health + random.randint(heal_potion[0], heal_potion[1])
        if player_health > 100:
            player_health = 100
            print("Unable to heal more than 100")
        print(player_health, "/", 100)
#Monster attacks on heal
        print("----The Monster has attacked----")
        player_health = player_health - random.randint(monster_attack_range[0], monster_attack_range[1])
        print("Player Health = ",player_health, "/", 100)
#Who wins or loses
        if player_health <= 0:
            print("You lost")
            break
        elif monster_health <= 0:
            print("You Won")
            break
    else:
        print("You have inputted a invalid option")



