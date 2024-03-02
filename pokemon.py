import numpy as np
import time
from health_bar import HealthBar
import sys
import random
from move import Move

random.seed()

class Pokemon:
    def __init__(self, name:str, types:str, moves:str, EVs:dict, xp:int = 0):
        self.name = name
        self.types = types 
        self.moves = moves

        self.base_attack = EVs['ATTACK']
        self.base_defense = EVs['DEFENSE']
        self.base_health = EVs['HEALTH']

        self.lvl = 3*(1+np.mean([self.attack,self.defense]))
        self.xp = xp
        self.xp_req = (4*self.lvl**3)/5
        if self.lvl > 5:
            sim_lvl_up(self,1,self.lvl)
        else:
            self.attack = self.base_attack
            self.defense = self.base_defense
            self.health = self.base_health

    
    def fight(self, target):
        #Causes two pokemon to fight each other
        print('-----POKEMON BATTLE-----')
        print(f"\n{self.name}")
        print(f"TYPE/", self.types)
        print("ATTACK/",self.attack)
        print("DEFENSE/", self.defense)
        #TODO change to a scaled system later
        print("LVL",self.lvl)
        print(f"XP {self.xp}/{self.xp_req}")
        print("\nVS")

        print(f"\n{target.name}")
        print(f"TYPE/", target.types)
        print("ATTACK/",target.attack)
        print("DEFENSE/", target.defense)
        #TODO change to a scaled system later
        print("LVL",target.lvl)
        time.sleep(2)

        #type advantages
        version = ['Fire', 'Water', 'Grass']
        for i,k in enumerate(version):
            if self.types == k:
                #Both are the same type
                if target.types == k:
                    string_1_attack = 'It\'s not very effective...'
                    string_2_attack = 'It\'s not very effective...'
                
                #target is strong
                if target.types == version[(i+1)%3]:
                    target.attack *= 2
                    target.defense *= 2
                    self.attack /= 2 
                    self.defense /= 2
                    string_1_attack = 'It\'s not very effective...'
                    string_2_attack = 'It\'s super effective...'

                #Target is weak
                if target.types == version[(i+2)%3]:
                    self.attack *= 2
                    self.defense *= 2
                    target.attack /= 2
                    target.defense /= 2
        #Create health bar
        self.HealthBar.draw()
        target.HealthBar.draw()
        #The actual fight
        while(self.health > 0) and (target.health > 0):
            self.HealthBar.update()
            target.HealthBar.update()

            print(f"Go {self.name}!")
            for i, x in enumerate(self.moves):
                print(f"{i+1}.", x)
            index = int(input("Pick a move: "))
            delay_print(f"{self.name} used {moves[index-1]}!")

            #determine user damage
            self.damage = (((2*self.lvl)/5)+2)*(self.moves[index-1].power*self.attack/target.defense)*(random.randrange(217,255)/255)
            target.health -= self.damage

            time.sleep(1)

            if target.health <= 0:
                delay_print(f"{target.name} has fainted")
                self.xp += target.lvl/7
                break
            #determine target damage
            target.damage = ((((2*target.lvl)/5)+2)*(target.moves[index-1].power)*target.attack/self.defense)*(random.randrange(217,255)/255)
            self.health -= target.damage

            time.sleep(1)
        
        money = random.randrange(0,5000)
        

att_overflow:float = 0
def_overflow:float = 0
health_overflow:float = 0
def update_stats(self):
    #check for level up
    if (self.xp >= self.xp_req):
        total_xp += self.xp
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
        update_stats(self)
        curr_lvl -= 1