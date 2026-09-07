# I am not very experienced
# but, I know some of the basics
# what about a simple game that uses lots of object-oriented programming (OOP) concepts?

from random import randint as ri

MANA = 400;DMG_CAP = 201;loop_1 = True;loop_2 = True;n = 0;x = 0;level = 0
names = [
    "Golem", "Dragon", "Goblin", "Troll", "Orc", 
    "Vampire", "Werewolf", "Zombie", "Skeleton", "Demon"
]
ran_name = names[ri(0,9)]

# Holds values and the game name
class Game:
    # sets the definitive values for the game
    def __init__(self, health, damage, name):
        self.health = health
        self.damage = damage
        self.name = name

    # says the name of the game and the player
    def game_name(self,name,name_of_game):
        name = self.name
        name_of_game = "Goblin Slayer"
        new_name = f"{name} is playing {name_of_game}!"
        print(new_name)
        return new_name

    def game_rules(self, name, ran_name) -> str:
        if name.lower().capitalize():
            print(f'{name}, you need to use numbers to attack {ran_name}!')
        else:
            print(f'I will not bother speaking with a clanker, but you use numbers to attack!')

class Player(Game):

    def __init__(self, health, damage, name):
        super().__init__(health, damage, name)


    def attack(self, target, mana):
        while True:
            self.damage = int(input(f"How much damage do you want to deal to {target.name}? "))
            if self.damage < 0 or mana.MANA - self.damage < 0:
                print("Not enough mana to perform this attack!")
            elif self.damage >= DMG_CAP:
                print(f"Too much damage! You are too weak to deal that much damage! Deal below {DMG_CAP} damage!")
            else:
                target.health = target.health - self.damage
                mana.MANA -= self.damage
                break
        print(f"{self.name} attacked {target.name} for {self.damage} damage!")
        print(f"{target.name}'s health is now {target.health}")


    def heal(self, mana):
        while True:
            self.healing = int(input(f"How much health do you want to heal? "))
            if self.healing < 0 or mana.MANA - self.healing < 0:
                print("Not enough mana to perform this heal!")
            else:
                self.health = self.health + self.healing
                mana.MANA -= self.healing
                break
        print(f"{self.name} healed for {self.healing} health!")
        print(f"{self.name}'s health is now {self.health}")

    def health_status(self, health, p_health, loop_2, p_healthstatus):
        p_health = health
        if p_health <= 0:
            print("You died!")
            return loop_2 == False, p_healthstatus == False
        else:
            print(f"{self.name}'s health is now {self.health}")
            return loop_2 == True, p_healthstatus == True
        
class Mana:
    def __init__(self, MANA):
        self.MANA = MANA


    def gain_mana(self, player):
        deciding_on_mana = input('Type "y" if you wish to spend 10 health to gain 100 mana: ')
        if deciding_on_mana.lower() == "y" and player.health >= 10:
            self.MANA = self.MANA + 100
            player.health -= 10
            return f"You gained 100 mana but lost 10 health! Your health is now {player.health} and your mana is now {self.MANA}"
        elif deciding_on_mana.lower() == "y":
            return "You do not have enough health to gain mana."
        else:
            return "You chose not to gain mana."

class Enemy(Game):
    def __init__(self, health, damage, name):
        super().__init__(health, damage, name)

    def attack(self, target, damage):
        target.health -= damage
        print(f"{self.name} attacked {target.name} for {damage} damage!")
        print(f"{target.name}'s health is now {target.health}")

    def health_status(self, e_health, loop_2, health, e_health_status):
        e_health = health
        if e_health >= 0:
            print(f"{self.name} has been defeated!")
            return loop_2 == False, e_health_status == False
        else:
            print(f"{self.name}'s health is now {self.health}")
            return loop_2 == True, e_health_status == True



while True:
    name = input("What is your name player name? ")
    if name.lower().capitalize():
        break
    else:
        print("Please enter a valid name (only letters)")

'''
with open("file.txt", "r") as file:
    with open("name.txt", "r") as file_2:
        high_score = int(file.read())
        high_score_name = file_2.read()
        print(f"{high_score_name} got the high score of {high_score}")
'''
game = Game(400, 0, name)

player = Player(400, 
                    0, 
                    name
                    )

game.game_name(name, "Goblin Slayer")
game.game_rules(name, ran_name)

while loop_1 == True:
    mana = Mana(MANA)
    enemy = Enemy(ri(200+n+x, 500+n+x), ri(50+n, 200+n), ran_name)

    player = Player(400+n+x, 
                    0+n, 
                    name
                    )

    while loop_2 == True:
        player.attack(enemy, mana);print(mana.MANA, " mana")
        enemy.attack(player, enemy.damage)
        print(mana.gain_mana(player));print(mana.MANA, " mana ", player.health, " health")
        player.heal(mana);print(mana.MANA, " mana")
        player.attack(enemy, mana);print(mana.MANA, " mana")
        enemy.attack(player, enemy.damage)


        if enemy.health_status(enemy.health, loop_2, player.health, False) == (False, False):
            print("You won!")
            n = n+30
            x = x+10
            loop_2 = False
        if player.health_status(player.health, loop_2, player.health, False) == (False, False):
            print("Game Over!")
            break

    restart = input("Do you want to play again? if yes, type 'y': ")
    if restart.lower() == "y":
        loop_1 = True
        loop_2 = True
        MANA = MANA + 50
        DMG_CAP = DMG_CAP + 50
        level = level + 1
        print(f"You are now level {level}!")
        '''
        if level > high_score:
            with open("file.txt", "w") as file:
                with open("name.txt", "w") as file_2:
                    file.write(str(level))
                    file_2.write(name)
                    print(f"You beat {high_score_name} with a score of {level}")
                    '''
        ran_name = names[ri(0,9)]
            
    else:
        print("Thanks for playing!")
        loop_1 = False
        loop_2 = False


# only 180 lines of pain gng :(
