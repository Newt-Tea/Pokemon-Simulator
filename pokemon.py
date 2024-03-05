import numpy as np
import time
from health_bar import HealthBar
import sys
import random
from move import move_dict
import os


random.seed()

class Pokemon:
    def __init__(self, name:str, types:str, moves:str, EVs:dict, xp:int = 0,lvl:int = None):
        self.name = name
        self.types = types 
        self.moves = moves

        self.base_attack = EVs['ATTACK']
        self.base_defense = EVs['DEFENSE']
        self.base_health = EVs['HEALTH']

        if lvl == None:
            self.lvl = 5
        else:
            self.lvl = lvl

        self.xp = xp
        self.total_xp = 0
        self.xp_req = (4*self.lvl**3)/5

        # if self.lvl > 1:
        #     sim_lvl_up(self,1,self.lvl)
        # else:
        self.attack = self.base_attack
        self.defense = self.base_defense
        self.health = self.base_health
        self.max_health = EVs['HEALTH']

        self.health_bar = HealthBar(self, color = "green")

        self.type_adv:str = None

    
    def fight(self, target):
        #Causes two pokemon to fight each other
        

        #type advantages
        version = ['Fire', 'Water', 'Grass']
        for i,k in enumerate(version):
            if self.types == k:
                #Both are the same type
                if target.types == k:
                    self.type_adv = None
                    target.type_adv = None
                    string_1_attack = None
                    string_2_attack = None
                
                #target is strong
                if target.types == version[(i+1)%3]:
                    target.type_adv = 'STRONG'
                    self.type_adv = 'WEAK'
                    string_1_attack = 'It\'s not very effective...'
                    string_2_attack = 'It\'s super effective...'

                #Target is weak
                if target.types == version[(i+2)%3]:
                    self.type_adv = 'STRONG'
                    target.type_adv = 'WEAK'
                    string_1_attack = 'It\'s super effective'
                    string_2_attack = 'It\'s not very effective'
        #Create health bar
        target.health_bar = HealthBar(target, color = "red")
        #The actual fight
        while(self.health > 0) and (target.health > 0):
            os.system('cls')
            print('-----POKEMON BATTLE-----')
            print(f"\n{self.name}")
            print(f"TYPE/", self.types)
            print("ATTACK/",self.attack)
            print("DEFENSE/", self.defense)
            #TODO change to a scaled system later
            print("LVL",self.lvl)
            print(f"XP {self.xp}/{self.xp_req}")
            self.health_bar.draw()
            print("\nVS")

            print(f"\n{target.name}")
            print(f"TYPE/", target.types)
            print("ATTACK/",target.attack)
            print("DEFENSE/", target.defense)
            #TODO change to a scaled system later
            print("LVL",target.lvl)
            target.health_bar.draw()
            time.sleep(1)
            

            

            delay_print(f"Go {self.name}!\n")
            for i, x in enumerate(self.moves):
                delay_print(f"{i+1}. {x}\n")
            index = int(input("Pick a move: "))
            delay_print(f"{self.name} used {self.moves[index-1]}!\n")

            #Rolls for accuracy
            acc_roll = random.randrange(0,100)
            #if roll is less then the accuracy of the move selected it hits
            if acc_roll < move_dict[self.moves[index-1]].accuracy:
                #determine user damage
                self.damage = round(((((2*self.lvl)/5)+2)*(move_dict[self.moves[index-1]].power*self.attack/target.defense)/50+2)*(random.randrange(217,255)/255))

                if self.type_adv == 'STRONG' :
                    self.damage *= 2
                elif self.type_adv == 'WEAK':
                    self.damage /= 2
                    self.damage = int(self.damage)

                target.health -= min(self.damage,target.health)
                target.health_bar.update()

                delay_print(f"{self.moves[index-1]} does {self.damage} damage to {target.name}\n")
                if(string_1_attack != None):
                    delay_print(f"{string_1_attack}\n")
            else:
                delay_print(f"{self.moves[index-1]} missed.\n")

            

            time.sleep(1)

            if target.health <= 0:
                delay_print(f"{target.name} has fainted")
                self.xp += target.lvl/7
                self.money = random.randrange(0,5000)
                break

            #Rolls for accuracy
            acc_roll = random.randrange(0,100)
            #if roll is less then the accuracy of the move selected it hits
            if acc_roll < move_dict[self.moves[index-1]].accuracy:
                #determine target damage
                target.damage = round((((((2*target.lvl)/5)+2)*(move_dict[target.moves[index-1]].power)*target.attack/self.defense)/50+2)*(random.randrange(217,255)/255))

                if target.type_adv == 'STRONG' :
                    target.damage *= 2
                elif target.type_adv == 'WEAK':
                    target.damage /= 2
                    target.damage = int(target.damage)

                self.health -= target.damage
                self.health_bar.update()

                delay_print(f"{target.name} uses {target.moves[index-1]} and it does {target.damage} damage to {self.name}\n")
                if (string_2_attack != None):
                    delay_print(f"{string_2_attack}\n")
            else:
                delay_print(f"{target.name} attempts to use {target.moves[index-1]} but it missed.\n")

            if self.health <= 0:
                delay_print(f"Your {self.name} has fainted")
                self.money = 0
                break

            time.sleep(1)
        

        

att_overflow:float = 0
def_overflow:float = 0
health_overflow:float = 0



def update_stats(self):
    #check for level up
    if (self.xp >= self.xp_req):
        self.total_xp += self.xp
        self.xp -= self.xp_req
        self.health += self.base_health/50
        self.attack += self.base_attack/50
        self.defense += self.base_defense/50
    
        #make sure stats stay as a whole number
        if (round(self.attack) > self.attack) :
            self.attack = round(self.attack)
        else:
            att_overflow = self.attack - round(self.attack)
            self.attack = round(self.attack)
        if(round(self.defense) > self.defense):
            self.defense = round(self.defense)
        else:
            def_overflow = self.defense - round(self.defense)
            self.defense = round(self.defense)
        if (round(self.health) > self.health):
            self.health = round(self.health)
        else: 
            health_overflow = self.health - round(self.health)
            self.health = round(self.health)


def delay_print(s:str):
    #prints one char at a time to simulate gameboy
    for c in s: 
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

def sim_lvl_up(self,curr_lvl,desired_lvl):
    #upgrades stats when a pokemon is initilized to ensure consitancy
    while curr_lvl < desired_lvl:
        self.xp = self.xp_req
        update_stats(self)
        curr_lvl += 1