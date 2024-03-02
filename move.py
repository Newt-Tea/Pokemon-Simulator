class Move:
    def __init__(self,power:int,accuracy:int,PP:int) -> None:
        self.PP = PP
        self.power = power
        self.accuracy = accuracy