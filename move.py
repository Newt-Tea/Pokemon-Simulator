class Move:
    def __init__(self,power:int,accuracy:int,PP:int) -> None:
        self.PP = PP
        self.power = power
        self.accuracy = accuracy
move_dict = {
    "Flamethrower":Move(15,100,95),
    "Fly":Move(),
    "Blast Burn":Move(),
    "Fire Punch":Move()
}