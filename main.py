from pokemon import Pokemon

if __name__ == '__main__':
    Charizard = Pokemon('Charizard','Fire', ['Fire Blast', 'Earthquake', 'Slash', 'Body Slam'], {"ATTACK":84,"DEFENSE":78,"HEALTH":78},0)
    Blastoise = Pokemon('Blastoise', 'Water', ['Surf', 'Earthquake', 'Blizzard', 'Slash'],{'ATTACK':83,'DEFENSE':100,'HEALTH':79},0)
    Charizard.fight(Blastoise)