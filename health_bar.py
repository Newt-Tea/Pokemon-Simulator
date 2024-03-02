import os

os.system("")

class HealthBar:
    """
    A class to create the Graphical Health Bar

    ...

    Attributes
    ----------
    symbol-remaining : str
        A symbol to represent health remaining on the main health bar
    symbol-lost : str
        A symbol to represent a bar missing on the main health bar
    barrier : str
        A symbol to indicate the edge of the main health bar
    colors : dict
        Storage of color options for the class
    entity : Character
        A representation of the character
    length : int, optional
        Determines how many bars the main health bar has in it (default 40)
    is_colored : bool, optional
        Determines if the bar has color applied (default True)
    color
        Determines the bars color (default "")

    Methods
    -------
    draw(self)
        Prints the health bar to the console
    update(self)
        Updates stored health value based on entity's current health value
    """
    #List of symbols for Graphic Health Bar
    symbol_remaining: str = "█"
    symbol_lost: str = "_"
    barrier:str = "|"
    colors: dict = {"red": "\033[91m",
                    "green": "\033[92m",
                    "grey": "|33[37m",
                    "default": "\033[0m"
                    }

    def __init__(self, entity,length : int = 40,is_colored:bool = True,color:str = "") -> None:
        """
        Parameters
        ----------
        entity : Character
            A representation of the character
        length : int, optional
            Determines how many bars the main health bar has in it (default 40)
        is_colored : bool, optional
            Determines if the bar has color applied (default True)
        color : str, optional
            Determines the bars color (default "")
        """
        self.entity = entity
        self.length = length
        self.is_colored = is_colored
        self.color = self.colors.get(color) or self.colors["default"]
        self.max_value = entity.maxHealth
        self.current_value = entity.health

    def update(self) -> None:
        """
        Updates the health bar based on entities current health
        """
        self.current_value = self.entity.health
#Creates the Graphic Health Bar
    def draw(self) -> None:
        """
        Draws the health bar to the console
        """
        remaining_bars = round(self.current_value / self.max_value * self.length)
        lost_bars = self.length - remaining_bars
        print(f"{self.entity.name}'s Health: {self.entity.health}/{self.entity.maxHealth}")
        print(f"{self.barrier}"
              f"{self.color if self.is_colored else ''}"
              f"{remaining_bars * self.symbol_remaining}"
              f"{lost_bars * self.symbol_lost}"
              f"{self.colors['default'] if self.is_colored else ''}"
              f"{self.barrier}")
