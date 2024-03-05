from pokemon import Pokemon
import sys
import time


def delay_print(s:str):
    #prints one char at a time to simulate gameboy
    for c in s: 
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

if __name__ == '__main__':
    char_dict = {
        "Charizard" : Pokemon('Charizard','Fire', ['Fire Blast', 'Earthquake', 'Slash', 'Body Slam'], {"ATTACK":84,"DEFENSE":78,"HEALTH":78},0),
        "Blastoise" : Pokemon('Blastoise', 'Water', ['Surf', 'Earthquake', 'Blizzard', 'Slash'],{'ATTACK':83,'DEFENSE':100,'HEALTH':79},0)
    }
    char_list = []
    idx:int = 0
    again:bool = True
    money = 0

    #game loop
    while(again):
        valid = False
        delay_print("Choose your Pokemon\n-------------------\n")

        for key in char_dict:
            delay_print(f"{idx+1}. {key}\n")
            char_list.append(key)
            idx += 1
        user_mon = char_dict[char_list[int(input("Choose your Pokemon: "))-1]]
        target = char_dict[char_list[int(input("Choose your opponent: "))-1]]
        user_mon.fight(target)
        restart = input("Would you like to fight again: (y/n): ")

        while valid == False:
            if restart =='y' or 'Y' or 'yes' or 'Yes':
                again = True
                valid = True
                #reset value for next attempt
                idx = 0
                char_list = []
                money += user_mon.money
                user_mon.health = user_mon.max_health
                target.health = target.max_health

            elif restart == 'n' or 'N' or 'No' or 'no':
                again = False
                valid = True
                print(f"You gained ${money} over the course of your adventures")
            else:
                delay_print("Please enter a valid response")
                valid = False
            