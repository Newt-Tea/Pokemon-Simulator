class Move:
    def __init__(self,power:int,accuracy:int,PP:int) -> None:
        self.PP = PP
        self.power = power
        self.accuracy = accuracy

move_dict = {
    'Fire Blast' : Move(120,85,5),
    'Earthquake' : Move(100,100,10),
    'Body Slam' : Move(85,100,15),
    'Slash' : Move(70,100,20),
    'Surf' : Move(95,100,15),
    'Blizzard' : Move(120,90,5)

}

