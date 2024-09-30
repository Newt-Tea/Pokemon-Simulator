"""The Main game script"""
import sys
import time
from pokemon import Pokemon



def delay_print(s:str):
    """A method to print one char at a time simulating a gameboy"""
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

if __name__ == '__main__':
    char_dict = {
        "Charizard" : Pokemon('Charizard','Fire', ['Fire Blast', 'Earthquake', 'Slash', 'Body Slam'], {"ATTACK":84,"DEFENSE":78,"HEALTH":78},0),
        "Blastoise" : Pokemon('Blastoise', 'Water', ['Surf', 'Earthquake', 'Blizzard', 'Slash'],{'ATTACK':83,'DEFENSE':100,'HEALTH':79},0)
    }
    char_list:list = []
    IDX:int = 0
    AGAIN:bool = True
    MONEY:int = 0

    #game loop
    while AGAIN:
        VALID:bool = False
        delay_print("Choose your Pokemon\n-------------------\n")

        for key in char_dict:
            delay_print(f"{IDX+1}. {key}\n")
            char_list.append(key)
            IDX += 1
        user_mon = char_dict[char_list[int(input("Choose your Pokemon: "))-1]]
        target = char_dict[char_list[int(input("Choose your opponent: "))-1]]
        user_mon.fight(target)
        restart = input("Would you like to fight again: (y/n): ")

        while VALID is False:
            if restart in ('y','Y','yes','Yes'):
                AGAIN = True
                VALID = True
                #reset value for next attempt
                IDX = 0
                char_list = []
                MONEY += user_mon.money
                user_mon.health = user_mon.max_health
                target.health = target.max_health

            elif restart in ('n','N','y','Y'):
                AGAIN = False
                VALID = True
                print(f"You gained ${MONEY} over the course of your adventures")
            else:
                delay_print("Please enter a valid response")
                VALID = False
            