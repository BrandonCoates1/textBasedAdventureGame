import random
import math
import time
from pprint import pprint
import os
import sys
import textwrap

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def typewriter(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        if char == "\n":
            time.sleep(1)
        elif char == "." or char == "?" or char == "!":
            time.sleep(0.3)
        else:
            time.sleep(0.01)

class player:
    def __init__(self, phealth, pstrength, pdefence, pmagic_attack, pranged_attack, ppower_of_words, pname):
        self.health = phealth
        self.strength = pstrength
        self.defence = pdefence
        self.magic_attack = pmagic_attack
        self.ranged_attack = pranged_attack
        self.power_of_words = ppower_of_words
        self.name = pname

    def current_health(self):
        return self.health
    def current_strength(self):
        return self.strength
    def current_defence(self):
        return self.defence
    def current_magic_attack(self):
        return self.magic_attack
    def current_ranged_attack(self):
        return self.ranged_attack
    def current_power_of_words(self):
        return self.power_of_words
    def current_name(self):
        return self.name

    def new_health(self, new_health):
        self.health = new_health
    def new_strength(self, new_strength):
        self.strength = new_strength
    def new_defence(self, new_defence):
        self.defence = new_defence
    def new_magic_attack(self, new_magic_attack):
        self.magic_attack = new_magic_attack
    def new_ranged_attack(self, new_ranged_attack):
        self.ranged_attack = new_ranged_attack
    def new_power_of_words(self, new_power_of_words):
        self.power_of_words = new_power_of_words
    def new_name(self, new_name):
        self.name = new_name

def create_class():
    typewriter("""Do you like close combat (1)
or ranged combat (2)
or do you think you're funny (3)?""")
    a = input("\n")
    while a != "1" and a != "2" and a != "3":
        clear()
        typewriter("Invalid selection!\n")
        typewriter("""Do you like close combat (1)
or ranged combat (2)
or do you think you're funny (3)?""")
        a = input("\n")
    clear()
    if a == "1":
        typewriter("""Do you prefer magic (1)
or melee (2)?""")
        b = input("\n")
        while b != "1" and b != "2":
            clear()
            typewriter("Invalid selection!\n")
            typewriter("""Do you prefer magic (1)
or melee (2)?""")
            b = input("\n")
        clear()
        if b == "1":
            player_health = 150
            player_strength = 15
            player_defence = 10
            player_magic_attack = 15
            player_ranged_attack = 0
            player_power_of_words = 1
        elif b == "2":
            player_health = 150
            player_strength = 25
            player_defence = 8
            player_magic_attack = 0
            player_ranged_attack = 10
            player_power_of_words = 1
    elif a == "2":
        typewriter("""Do you prefer ranged magic (1)
or archer (2)?""")
        b = input("\n")
        while b != "1" and b != "2":
            clear()
            typewriter("Invalid selection!\n")
            typewriter("""Do you prefer ranged magic (1)
or archer (2)?""")
            b = input("\n")
        clear()
        if b == "1":
            player_health = 100
            player_strength = 1
            player_defence = 5
            player_magic_attack = 25
            player_ranged_attack = 0
            player_power_of_words = 2
        elif b == "2":
            player_health = 100
            player_strength = 3
            player_defence = 4
            player_magic_attack = 0
            player_ranged_attack = 25
            player_power_of_words = 1
    else:
        player_health = 75
        player_strength = 1
        player_defence = 15
        player_magic_attack = 0
        player_ranged_attack = 0
        player_power_of_words = 50
    typewriter("What is your name player?")
    player_name = input("\n")
    clear()
    typewriter(f"Welcome {player_name}, We hope you enjoy our game!\n")
    time.sleep(0.3)
    clear()
    return (player_health, player_strength, player_defence, player_magic_attack, player_ranged_attack, player_power_of_words, player_name)

class enemy:
    def __init__(self, ehealth, eattack, especial, echance, ename):
        self.health = ehealth
        self.attack = eattack
        self.special = especial
        self.chance = echance
        self.name = ename

    def current_health(self):
        return self.health
    def current_attack(self):
        return self.attack
    def current_special(self):
        return self.special
    def current_chance(self):
        return self.chance
    def current_name(self):
        return self.name
    
    def new_health(self, new_health):
        self.health = new_health
    def new_attack(self, new_attack):
        self.attack = new_attack
    def new_special(self, new_special):
        self.special = new_special
    def new_chance(self, new_chance):
        self.chance = new_chance
    def new_name(self, new_name):
        self.name = new_name

def enemy_gen():
    file = open("adjective.txt", "r")
    lines = file.readlines()
    adjective = lines[random.randint(0,len(lines)-1)][:-1]
    file.close
    if choice == "1a":
        health = random.randint(100, 250)
        attack = random.randint(20, 40)
        special = random.randint(40, 70)
        chance = random.randint(6, 15)
        return enemy(health, attack, special, chance, adjective + " Witch")
    elif choice == "2a":
        health = random.randint(50, 500)
        attack = random.randint(25, 55)
        special = random.randint(25, 100)
        chance = random.randint(7, 15)
        return enemy(health, attack, special, chance, adjective + " Knights")
    elif choice == "1b":
        health = random.randint(100, 250)
        attack = random.randint(20, 35)
        special = random.randint(30, 60)
        chance = random.randint(3, 15)
        return enemy(health, attack, special, chance, adjective + " Guard")
    elif choice == "2b":
        health = random.randint(150, 400)
        attack = random.randint(25, 55)
        special = random.randint(30, 100)
        chance = random.randint(3, 15)
        return enemy(health, attack, special, chance, adjective + " Troll")

def do_health(background_colour, background_colour_end):
    global max_health, health_dashes
    dash_convert = int(max_health / health_dashes)
    current_dashes = int(character.current_health() / dash_convert)
    remaining_health = health_dashes - current_dashes
    health_display = "-" * current_dashes
    remaining_display = " " * remaining_health

    return "|" + background_colour + health_display + background_colour_end + remaining_display + "|"

def enemy_do_health(background_colour, background_colour_end):
    global enemy_max_health, health_dashes
    dash_convert = int(enemy_max_health / health_dashes)
    current_dashes = int(boss.current_health() / dash_convert)
    remaining_health = health_dashes - current_dashes
    health_display = "-" * current_dashes
    remaining_display = " " * remaining_health

    return "|" + background_colour + health_display + background_colour_end + remaining_display + "|"

def health_bar():
    print(red + "     __  __           ____  __  \n    / / / /__  ____ _/ / /_/ /_ \n", "  / /_/ / _ \/ __ `/ / __/ __ \   " + rend, f"{do_health(bred, brend)}\n", red + " / __  /  __/ /_/ / / /_/ / / /", f"             {character.current_health()}\n", "/_/ /_/\___/\__,_/_/\__/_/ /_/ " + rend)
    print("")

def poison_health_bar():
    print(green + "     __  __           ____  __  \n    / / / /__  ____ _/ / /_/ /_ \n", "  / /_/ / _ \/ __ `/ / __/ __ \   " + gend, f"{do_health(bgreen, bgend)}\n", green + " / __  /  __/ /_/ / / /_/ / / /", f"             {character.current_health()}\n", "/_/ /_/\___/\__,_/_/\__/_/ /_/ " + gend)
    print("")

def enemy_health_bar():
    print(red + "     __  __           ____  __  \n    / / / /__  ____ _/ / /_/ /_ \n", "  / /_/ / _ \/ __ `/ / __/ __ \   " + rend, f"{enemy_do_health(bred, brend)}\n", red + " / __  /  __/ /_/ / / /_/ / / /", f"             {boss.current_health()}\n", "/_/ /_/\___/\__,_/_/\__/_/ /_/ " + rend)
    print("")

def projectile():
    global purple, pend
    clear()
    print(purple, """
            ________
        _____ ##### ____
    ____ ############# ______
    ___ ###### ______
        __________
    """, pend)
    time.sleep(0.3)
    clear()
    print(purple, """
                                    ________
                                _____ ##### ____
                            ____ ############## ______
                            ___ ###### ______
                                __________
    """, pend)
    time.sleep(0.2)
    clear()
    print(purple, """
                                                                                ________
                                                                            _____ ##### ____
                                                                        ____ ############## ______
                                                                        ___ ###### ______
                                                                            __________
    """, pend)
    time.sleep(0.2)
    clear()
    print(purple, """
                                                                                                                                    ________
                                                                                                                                _____ ##### ____
                                                                                                                            ____ ############## ______
                                                                                                                            ___ ###### ______
                                                                                                                                __________
    """, pend)
    time.sleep(0.2)
    clear()

def arrow():
    clear()
    print("""
             _______
        _____ ##### ____
________ ############# ______
        _____ ##### ____
             _______
    """)
    time.sleep(0.3)
    clear()
    print("""
                                     _______
                                _____ ##### ____
________________________________ ############## ______
                                _____ ##### ____
                                     _______
    """)
    time.sleep(0.2)
    clear()
    print("""
                                                                               _______
                  |\|\|\|\                                                _____ ##### ____
                 (        >________________________________________________ ############## ______
                  |/|/|/|/                                                _____ ##### ____
                                                                               _______
    """)
    time.sleep(0.2)
    clear()
    print("""
                                                                                                                                                 _______
                                                                                    |\|\|\|\                                                _____ ##### ____
                                                                                   (        >________________________________________________ ############## ______
                                                                                    |/|/|/|/                                                _____ ##### ____
                                                                                                                                                 _______
    """)
    time.sleep(0.2)
    clear()

def word_attack():
    clear()
    print("""
            
wasdadhfrsth                    
                            
""")
    time.sleep(0.2)
    clear()
    print("""
            sdfwesfsegfjytd                
wasdadhfrsth                         
                                
""")
    time.sleep(0.2)
    clear()
    print("""
            sdfwesfsegfjytdxzzaw                      
wasdadhfrsth                    fvcb                    
                                    cvdsdesplo
""")
    time.sleep(0.2)
    clear()
    print("""
            sdfwesfsegfjytdxzzaw                                                                     
wasdadhfrsth                    fvcb                    saddsadadfgwadesrbniopaewrg             
                                    cvdsdesplofjivmnawef                           sdvbnaolwef
""")
    time.sleep(0.2)
    clear()
    print("""
            sdfwesfsegfjytdxzzaw                                                                    swkadlfbplsadknvowieuvna
wasdadhfrsth                    fvcb                    saddsadadfgwadesrbniopaewrg           dsfava                        aspobmzcaerdgsdgfbsrt
                                    cvdsdesplofjivmnawef                           sdvbnaolwef
""")
    time.sleep(0.2)
    clear()

def health_potion():
    clear()
    typewriter("""A potion has been dropped.
You decide to consume the potion.
You start to feel rejuvenated.""")
    clear()
    typewriter("Your health is increasing by 5 for 5 seconds...\n")
    health_bar()
    time.sleep(1)
    clear()
    for i in range(1, 6):
        print("Your health is increasing by 5 for 5 seconds...")
        character.new_health(character.current_health() + 5)
        health_bar()
        time.sleep(1)
        clear()

def poison():
    clear()
    typewriter("""You have been poisoned!
You start to feel sick.""")
    clear()
    typewriter("Your health is descreasing by 5 for 3 seconds...\n")
    poison_health_bar()
    time.sleep(1)
    clear()
    for i in range(1, 4):
        print("Your health is descreasing by 5 for 3 seconds...")
        character.new_health(character.current_health() - 5)
        poison_health_bar()
        time.sleep(1)
        clear()

def enemy_attack(hit_chance, attack_value, special_attack, name, defence):
    typewriter(f"{boss.current_name()} is winding up for an attack...\n")
    hit = random.randint(0, 15)
    which_attack = random.randint(0, 10)
    if which_attack > 3:
        if hit_chance >= hit:
            typewriter("You get hit!\n")
            loss = attack_value - defence
            typewriter(f"You lose {loss} health!\n")
            time.sleep(1)
            clear()
            return math.ceil(loss)
        else:
            typewriter(f"{boss.current_name()} has missed!\n")
            return 0
    else:
        if hit_chance >= hit:
            typewriter("You get hit with a special attack!\n")
            loss = special_attack - defence
            typewriter(f"You lose {loss} health!\n")
            clear()
            poison_chance = random.randint(0, 10)
            if character.current_health() > 0:
                if poison_chance >= 5:
                    poison()
            return math.ceil(loss)
        else:
            typewriter(f"{boss.current_name()} has missed its special attack!\n")
            return 0
        
def choices(x):
    global choice
    choice = x

def is_dead(health):
    if health < 1:
        return True
    else:
        return False

def game_over(enemy_dead):
    if enemy_dead == True:
        return 
    else:
        print(red + "  ,--,     .--.           ,---.    .---..-.   .-.,---.  ,---.   .-.  \n.' .'     / /\ \ |\    /| | .-'   / .-. )\ \ / / | .-'  | .-.\  |  ) \n|  |  __ / /__\ \|(\  / | | `-.   | | |(_)\ V /  | `-.  | `-'/  | /  \n\  \ ( _)|  __  |(_)\/  | | .-'   | | | |  ) /   | .-'  |   (   |/   \n \  `-) )| |  |)|| \  / | |  `--. \ `-' / (_)    |  `--.| |\ \  (    \n )\____/ |_|  (_)| |\/| | /( __.'  )---'         /( __.'|_| \)\(_)   \n(__)             '-'  '-'(__)     (_)           (__)        (__)   " + rend)
        time.sleep(3)
        clear()
        typewriter("Thank you for playing our game!\n\n")
        print("""   ______                ____               __  
  / ____/___  ____  ____/ / /_  __  _____  / /   
 / / __/ __ \/ __ \/ __  / __ \/ / / / _ \/ /    
/ /_/ / /_/ / /_/ / /_/ / /_/ / /_/ /  __/_/     
\____/\____/\____/\__,_/_.___/\__, /\___(_)      
                             /____/              """)
        exit()

def battle(gen_enemy, gen_player):
    typewriter(f"""You have chosen to battle the {gen_enemy.name}!
Here are its stats:
""")
    pprint(vars(gen_enemy))
    battle = True
    time.sleep(3)
    clear()
    while battle == True:
        typewriter(f"{gen_player.current_name()} attacks...\n")
        typewriter(f"""Attack, close combat? (1) {gen_player.current_strength()}
Attack, ranged combat? (2) {gen_player.current_ranged_attack()}
Attack, magic? (3) {gen_player.current_magic_attack()}
attack... with words (4) {gen_player.current_power_of_words()}
""")
        action = input()
        while action != "1" and action != "2" and action != "3" and action != "4":
            clear()
            typewriter("Invalid selection!\n")
            typewriter(f"""Attack, close combat? (1) {gen_player.current_strength()}
Attack, ranged combat? (2) {gen_player.current_ranged_attack()}
Attack, magic? (3) {gen_player.current_magic_attack()}
attack... with words (4) {gen_player.current_power_of_words()}
""")
            action = input()
        clear()
        crit = random.randint(0, 10)
        if action == "1":
            damage = gen_player.current_strength()
        elif action == "2":
            damage = gen_player.current_ranged_attack()
        elif action == "3":
            damage = gen_player.current_magic_attack()
        else:
            damage = gen_player.current_power_of_words()
        typewriter("You wind up for the attack!...\n")
        hit = random.randint(0, 10)
        stun_boolean = False
        stun = random.randint(0, 10)
        crit = random.randint(0, 10)
        if hit > 3:
            if crit > 3:
                if damage == gen_player.current_ranged_attack():
                    arrow()
                elif damage == gen_player.current_magic_attack():
                    projectile()
                elif damage == gen_player.current_power_of_words():
                    word_attack()
                typewriter(f"You've damaged the {gen_enemy.current_name()} for {damage}!\n")
                gen_enemy.new_health(gen_enemy.current_health() - damage)
            else:
                if damage == gen_player.current_ranged_attack():
                    arrow()
                elif damage == gen_player.current_magic_attack():
                    projectile()
                elif damage == gen_player.current_power_of_words():
                    word_attack()
                typewriter(f"You've crit the {gen_enemy.current_name()} for {int(damage * 1.5)}!\n")
                gen_enemy.new_health(gen_enemy.current_health() - int(damage * 1.5))
            if stun < 4:
                typewriter(f"You've stunned the {gen_enemy.current_name()} for 1 turn!\n")
                stun_boolean = True
            else:
                stun_boolean = False
            if gen_enemy.current_health() > 0:
                typewriter(f"The {gen_enemy.current_name()} health is {gen_enemy.current_health()}!\n")
                enemy_health_bar()
                time.sleep(2)
                clear()
            else:
                typewriter(f"The {gen_enemy.current_name()} health is 0!\n")
                clear()
        else:
            typewriter(f"You've missed the {gen_enemy.current_name()}!\n")
            time.sleep(1)
            clear()
        enemy_dead = is_dead(gen_enemy.current_health())
        if enemy_dead == False and stun_boolean == False:
            gen_player.new_health(gen_player.current_health() - enemy_attack(gen_enemy.current_chance(), gen_enemy.current_attack(), gen_enemy.current_special(), gen_enemy.current_name(), gen_player.current_defence()))
            player_dead = is_dead(gen_player.current_health())
            if player_dead == True:
                battle = False
                return False
            else:
                typewriter(f"Your remaining health is {gen_player.current_health()}!\n")
                health_bar()
                time.sleep(1)
                clear()
        elif enemy_dead == True:        
            battle = False
            typewriter(f"You have defeated the {gen_enemy.current_name()}!\n")
            health_potion()
            time.sleep(1)
            clear()
            return True
        elif stun_boolean == True:
            typewriter(f"{gen_player.current_name()} attacks again!\n")
            clear()

def check_battle_state():
    global enemy_max_health, boss
    boss = enemy_gen()
    enemy_max_health = boss.current_health()
    who_died = battle(boss, character)
    game_over(who_died)

def route_choice():
    typewriter("You awake from a deep sleep to the sound of birds and tree branches blowing in the wind, this is odd as you live in an apartment in the city.\nAlso to your confusion, you are laying on a bail of hay in an old rickety barn... And to make things worse you have hayfever.\nAfter all the confusion just seems to never disappear, You plan your next move.\nFrom what you can see you have only three options...\n") 
    time.sleep(1)
    a = input("\nYou could head towards the castle (1)\nA little village on the river (2)\nGo back to sleep in the barn you woke up in (3)\n")
    while a != "1" and a != "2" and a != "3":
        typewriter("Invalid selection!\n")
        a = input("\nYou could head towards the castle (1)\nA little village on the river (2)\nGo back to sleep in the barn you woke up in (3)\n")
    if a == "1":
        castle()
    elif a == "2":
        clear()
        tavern_stables()
    elif a == "3":
        clear()
        typewriter("\nYou must be sleepy!\nOff to the hay we go.\nYou wake up in your bed in the city, that was a quick dream!\nYou get up and head to Codenation.")
        time.sleep(3)
        clear()
        typewriter("Thank you for playing our game!\n\n")
        print("""   ______                ____               __  
  / ____/___  ____  ____/ / /_  __  _____  / /   
 / / __/ __ \/ __ \/ __  / __ \/ / / / _ \/ /    
/ /_/ / /_/ / /_/ / /_/ / /_/ / /_/ /  __/_/     
\____/\____/\____/\__,_/_.___/\__, /\___(_)      
                             /____/              """)
        exit()

def castle():
    clear()
    typewriter("""Whilst heading towards the majestic castle you see miraculous events taking place like it's natural.
You speak to a few people, asking questions about where you are? How these people are flying around?
...
You learn about magic and all sorts of magical creatures like witches, ogers, and trolls.
You also find out that this age is completely different to the one you know.
...
You start to bombard you mind with questions about everything but...
out of the corner of your eye, you spot a Lady. A very weird looking Lady.
She has long black hair and a scoul on her face, with tattered clothes and a broken carrige behind her.

""")
    time.sleep(1.5)
    typewriter("""Do you approach her? (1)
Do you stay away from that freak! (2)
""")
    a = input()
    while a != "1" and a != "2":
        typewriter("Invalid selection!\n")
        typewriter("""Do you approach her? (1)
Do you stay away from that freak! (2)
""")
        a = input()
    if a == "1":
        approach()
    else:
        not_approach()

def approach():
    clear()
    typewriter(f"""You gather all your courage and approach the eerie lady.
'He-hello.'
'Oh, hello there {character.current_name()}.'
'Wa-wait... how do you kn-know my name?'
'Ohhhh little one, I know many things. Including how you're here.'
'Wa-wait wh-...'
'Now, now. I have things that can help you survive in this place.' The Lady rumages through a bag pulled of the broken carrige.
'Here, take this apple... It will help on your journey, trust me.'

""")
    time.sleep(1.5)
    typewriter("""Do you take the apple? (1)
Do you say hell no? (2)
""")
    a = input()
    while a != "1" and a != "2":
        clear()
        typewriter("Invalid selection!\n")
        typewriter("""Do you take the apple? (1)
Do you say hell no? (2)
""")
        a = input()
    if a == "1":
        speak_yes()
    else:
        speak_no()

def not_approach():
    clear()
    typewriter("""You decide to avoid the weird looking Lady.
You walk by and the Lady gives you an ominous look
...
You ignore the Lady and walk off towards the castle,
but suddenly you feel an object smash into the back of your head.

""")
    time.sleep(1.5)
    typewriter("""Do you turn around and attack the Lady? (1)
Do you ignore the Lady and walk away? (2)
""")
    a = input()
    while a != "1" and a != "2":
        clear()
        typewriter("Invalid selection!\n")    
        typewriter("""Do you turn around and attack the Lady? (1)
Do you ignore the Lady and walk away? (2)
""")
        a = input()
    if a == "1":
        choices("1a")
        check_battle_state()
        witch_dead()
    else:
        draw_bridge()

def speak_yes():
    clear()
    typewriter("""'Th-thanks, I was getting a little hungry.' You accept the apple with utmost gratitude.
'hehe' The lady crackled.

You eat the apple whilst walking off and start to feel a bit dazed...
Then all of a sudden, you feel sharp pain shooting through your body...
*Crash*...
You awaken to heavy breathing, and a slight bit of pain.
You realize it was all a dream.
You relax for a little while, then head to Codenation
to have another horrible day of coding again...""")
    time.sleep(1.5)
    clear()
    typewriter("Thank you for playing our game!\n\n")
    print("""   ______                ____               __  
  / ____/___  ____  ____/ / /_  __  _____  / /   
 / / __/ __ \/ __ \/ __  / __ \/ / / / _ \/ /    
/ /_/ / /_/ / /_/ / /_/ / /_/ / /_/ /  __/_/     
\____/\____/\____/\__,_/_.___/\__, /\___(_)      
                             /____/              """)

def speak_no():
    global chioce
    clear()
    typewriter("""'E-ewwww no...
Who would ever accept anything from a stranger like you?
Sorry but goodbye.'
...
You start to walk off towards the castle,
but suddenly you feel an object smash into the back of your head.

""")
    time.sleep(1.5)
    typewriter("""Do you turn around and attack the Lady? (1)
Do you ignore the Lady and walk away? (2)
""")
    a = input()
    while a != "1" and a != "2":
        clear()
        typewriter("Invalid selection!\n")    
        typewriter("""Do you turn around and attack the Lady? (1)
Do you ignore the Lady and walk away? (2)
""")
        a = input()
    if a == "1":
        choices("1a")
        check_battle_state()
        witch_dead()
    else:
        draw_bridge()

def witch_dead():
    clear()
    typewriter("""You walked out of sight and felt so exhausted but relieved that was over.
...
Shortly after, you suddenly notice how big the castle has gotten.
It was enormous!
You see the drawbridge at the end of your path.
When you arrive, there is a guard standing there...
he looks asleep, you shout him and he jolts awake.
'Oh sorry, it seems I nodded off.'
'What is it you want?'
'I would like to enter the castle?'
'Well then, I'm going to have to ask a few questions.'
'Did you see a suspicious Lady on your travels?'

""")
    time.sleep(1.5)
    typewriter("""Yes? (1)
No? (2)
""")
    a = input()
    while a != "1" and a != "2":
        clear()
        typewriter("Invalid selection!\n")
        typewriter("""Yes? (1)
No? (2)
""")
        a = input()
    if a == "1":
        drawbridge_answer()
    else:
        drawbridge_answer()

def draw_bridge():
    clear()
    typewriter("""You decided to walk away and be the better person.
The Witch hailed insult left and right, trying to provoke you.
You walked out of sight and felt so exhausted but relieved that was over.
...
Shortly after, you suddenly notice how big the castle has gotten.
It was enormous!
You see the drawbridge at the end of your path.
When you arrive, there is a guard standing there...
he looks asleep, you shout him and he jolts awake.
'Oh sorry, it seems I nodded off.'
'What is it you want?'
'I would like to enter the castle?'
'Well then, I'm going to have to ask a few questions.'
'Did you see a suspicious Lady on your travels?'

""")
    time.sleep(1.5)
    typewriter("""Yes? (1)
No? (2)
""")
    a = input()
    while a != "1" and a != "2":
        clear()
        typewriter("Invalid selection!\n")
        typewriter("""Yes? (1)
No? (2)
""")
        a = input()
    if a == "1":
        drawbridge_answer()
    else:
        enter_castle()

def drawbridge_answer():
    clear()
    typewriter("""Did you up the Ladys' offer?
""")
    time.sleep(1)
    typewriter("""Yes? (1)
No? (2)
""")
    a = input()
    while a != "1" and a != "2":
        clear()
        typewriter("Invalid selection!\n")
        typewriter("""Yes? (1)
No? (2)
""")
        a = input()
    if a == "1":
        drawbridge_yes()
    else:
        enter_castle()

def drawbridge_yes():
    clear()
    typewriter("""'No, You're lying to me.'
'I know you are because you would be dead.'
'This kingdom doesn't accept people who are liars...'
'Begone!'

""")
    time.sleep(1.5)
    typewriter("""Do you attack the guard? (1)
do you persuade guard? (2)
""")
    a = input()
    while a != "1" and a != "2":
        clear()
        typewriter("Invalid selection!\n")    
        typewriter("""Do you attack the guard? (1)
do you persuade guard? (2)
""")
        a = input()
    if a == "1":
        choices("1b")
        check_battle_state()
        enter_castle()
    else:
        persuade()

def persuade():
    clear()
    typewriter(f"""'No no, sorry, I'm not from around here.'
'I'm actually new to all this and I sincerely appologise...'
...
'Ok... Fine, I'll believe you this time.'
'Just make sure it doesn't happen agian!'
'Head inside and register you name.'
'I hope you throughly enjoy your stay here...'
'{character.current_name()}.'""")
    time.sleep(1.5)
    enter_castle()

def enter_castle():
    clear()
    typewriter("""Well... you are now in the castle.
You aimlessly walk around, not sure what to do.
...
Eventually you land upon a tavern.
It's brimming with people and just... a welcoming environment.
You sit down and enjoy ale, of which you have never tasted before but loved at first sip.
People come and go, loads of drunk conversations with strangers,
Game are won and lost.
All leading into the next morning, were you suddenly collapse...
*crash*
You wake to your alarm screeching, wait, was that a dream you thought?
'Well, it was amazing!'
You suddenly get a message from Codenation...
'Don't worry you don't have to come in today.'""")
    time.sleep(1.5)
    clear()
    typewriter("Thank you for playing our game!\n\n")
    print("""   ______                ____               __  
  / ____/___  ____  ____/ / /_  __  _____  / /   
 / / __/ __ \/ __ \/ __  / __ \/ / / / _ \/ /    
/ /_/ / /_/ / /_/ / /_/ / /_/ / /_/ /  __/_/     
\____/\____/\____/\__,_/_.___/\__, /\___(_)      
                             /____/              """)
                
def tavern_stables():
    clear() 
    typewriter("\nWhile walking towards the tavern you quickly realise you are in the 11th Century.\nConfused and perplexed you do your best to blend in without causing too much suspicion, afterall you are very aware of how brutal these times can be.\nAs you are approaching the tavern you see a stables hidden behind a row of trees, the two options are both promising as you are ready to embrace an adventure in this strange land.\nWill you:\nChoose to go inside for a look around (1) or go and take alook inside the stables? (2)")
    time.sleep(1)
    a = input()
    while a != "1" and a != "2":
        typewriter("Invalid selection!\n")
        a = input()
    if a == "1":
        tavern()
    elif a == "2":
        clear()
        typewriter("\nAs a horse enthusiast you instinctively head straight for the stables, you could possibly be able to fulfill your childhood dream!\nRiding in a Jousting tournament has been a fantasy for years, the thought is exhilarating.\nAs you approach you don’t hear the sound of horses you are so used to, instead you hear someone talking to themselves about going on an adventure to a mountain?\nTurning the corner into the stable you are not greeted by horses or humans but a glorious talking Unicorn called Charlie, he tells you he wants to take you to Candy Mountain.\nYou ride him all the way to Candy Mountain.\nThen all of a sudden... you wake up in your bed.\n'What a strange dream that was'\nYou then head to Codenation and begin your horrible day of coding.")
        time.sleep(1.5)
        clear()
        typewriter("Thank you for playing our game!\n\n")
        print("""   ______                ____               __  
  / ____/___  ____  ____/ / /_  __  _____  / /   
 / / __/ __ \/ __ \/ __  / __ \/ / / / _ \/ /    
/ /_/ / /_/ / /_/ / /_/ / /_/ / /_/ /  __/_/     
\____/\____/\____/\__,_/_.___/\__, /\___(_)      
                             /____/              """)
def tavern():
    clear()
    typewriter("\nWalking toward the weathered tavern you can tell it's a popular place for locals and travelers alike.\nAs you approach the noise from inside becomes louder, it’s clearly a popular place.\nYou notice some knights horses hitched up outside, they must be on their way back to the Castle.\nPlacing your hand on the old oak door you push it open, thankfully nobody turns around and stares at you.\nYou must be blending in with the locals, thanking your past self for choosing the correct outfit.\nYou walk over to the bar to ask for a beer.\nSitting next to the bar is the group of knights whose horses are hitched up outside.\nThey ask you for a game of cards, you eagerly accept.\nDo you cheat them (1) or do you play with honour? (2)\n")
    time.sleep(1.5)
    a = input()
    while a != "1" and a != "2":
        typewriter("Invalid selection!\n")
        a = input()
    if a == "1":
        cheat_knights()
    elif a == "2":
        honor_knights()

def cheat_knights():
    clear()
    typewriter("""The Knights know you cheated!
They draw their swords, demanding for the coin to be given back.
You grab your weapon ready to defend yourself.
Running as fast as you can you barge through the oak door taking it off its hinges.
You try to put as much distance between you and the group of knights as you can. 
Managing to lose them in the trees you head towards the village.
It was a good idea to stay off the main path as they are now on horseback looking for you. 
Reaching the end of the tree line your safety of cover is now gone,
you see a chance to run into the village and hide between the buildings.
Just as you enter the main gates of the village you are cut off and surrounded by the group. 
The battle for your life is about to begin...
""")
    choices("2a")
    time.sleep(1.5)
    check_battle_state()
    knight_dead()

def knight_dead():
    clear()
    typewriter("""You have defeated the knights.
The village is disgusted with your actions.
You get chased out of the village by every living soul inside...
Eventually, you get caught.
The village has a long discussion and decides to behead you for your crimes.
...
*Chop*
...
Sreaming, you wake up from what seems to be a dream.
You ignore what happened and plan to continue with your day.
You go to Codenation.
With a headache...
""")
    time.sleep(1.5)
    clear()
    typewriter("Thank you for playing our game!\n\n")
    print("""   ______                ____               __  
  / ____/___  ____  ____/ / /_  __  _____  / /   
 / / __/ __ \/ __ \/ __  / __ \/ / / / _ \/ /    
/ /_/ / /_/ / /_/ / /_/ / /_/ / /_/ /  __/_/     
\____/\____/\____/\__,_/_.___/\__, /\___(_)      
                             /____/              """)

def honor_knights():
    clear()
    typewriter("\nYou play the game of cards with honour and grace however you suck at cards and loose, but the knights respect you for this.\nThey buy you numerous rounds of beer and have a great night in the local, they offer you to join them on the journey to the village.\nOn the journey they warn you there are trolls in the area and to be very careful.\nUnfortunately at the next bridge the noise of your new drunken friends wake a sleeping troll.\nYou all dismount so you are ready to flee into the trees or battle.\nDo you decide to battle the troll with the knights? (1) or do you flee from the troll? (2)\n")
    time.sleep(1)
    a = input()
    while a != "1" and a != "2":
        typewriter("Invalid selection!\n")
        a = input()
    if a == "1":
        choices("2b")
        check_battle_state()
        troll_dead()
    elif a == "2":
        clear()
        typewriter("\nRunning into the trees to hide from the troll, you notice the knights have stayed to battle the troll.\nYou watch through the thick bushes as one by one the knights get beaten and crushed by the troll, one knight shouts before he is crushed 'run to the village for safety'.\nYou wait until the troll goes back under the bridge, leaving your hiding place you tiptoe across the same bridge to avoid waking the troll again.\nYou made it! But then before you can begin to run the troll picks you up and eats you alive.\nYou wake up in your bed in the city!\nIt was all a dream!\nYou move on with your day and head to Codenation.\nTime for another horrible day of coding!")

def troll_dead():
    clear()
    typewriter("""You have defeated the troll.
The village and a few remaining knights all look worn out.
Inclucding you.
A few moments afterwards, all the knights run to you...
They pick you up screaming 'He's our hero, the villages hero'!
All night long celebrations raged throughout the Village.
All leading into the next morning, were you suddenly collapse...
*crash*
You wake to your alarm screeching, wait, was the a dream you thought?
'Well, it was amazing!'
You suddenly get a message from Codenation...
Don't worry you don't have to come in today.h""")
    time.sleep(1.5)
    clear()
    typewriter("Thank you for playing our game!\n\n")
    print("""   ______                ____               __  
  / ____/___  ____  ____/ / /_  __  _____  / /   
 / / __/ __ \/ __ \/ __  / __ \/ / / / _ \/ /    
/ /_/ / /_/ / /_/ / /_/ / /_/ / /_/ /  __/_/     
\____/\____/\____/\__,_/_.___/\__, /\___(_)      
                             /____/              """)

typewriter("Welcome to our game!")
print("""
 ____  ____  ____   __   _  _  _  _    ____   __   ____   __   ____  __  ____  ____  ___  
(    \(  _ \(  __) / _\ ( \/ )( \/ )  (  _ \ / _\ (  _ \ / _\ (    \(  )/ ___)(  __)(__ \ 
 ) D ( )   / ) _) /    \/ \/ \ )  /    ) __//    \ )   //    \ ) D ( )( \___ \ ) _)  (__/ 
(____/(__\_)(____)\_/\_/\_)(_/(__/    (__)  \_/\_/(__\_)\_/\_/(____/(__)(____/(____) (_)  """)

time.sleep(2)
clear()
class_data = create_class()
character = player(class_data[0], class_data[1], class_data[2], class_data[3], class_data[4], class_data[5], class_data[6])
max_health = character.current_health()
choice = "1a"
enemy_max_health = 0
boss = ""
health_dashes = 20
red = "\33[91m"
bred = "\33[41m" + "\033[91m"
rend = "\33[0m"
brend = "\33[0m" + "\033[0m"
green = "\33[92m"
bgreen = "\33[102m" + "\33[92m"
gend = "\33[0m"
bgend = "\33[0m" + "\33[0m"
purple = "\33[35m"
pend = "\33[0m"

typewriter("""Here are your stats:
""")
pprint(vars(character))
typewriter("""Would you like to continue to the game? y/n
""")
answer = input()
while answer != "y" and answer != "n":
    typewriter("""Invalid selection!\n
""")
    typewriter("""Would you like to continue to the game? y/n
""")
    answer = input()
if answer == "y":
    clear()
    route_choice()
else:
    exit()