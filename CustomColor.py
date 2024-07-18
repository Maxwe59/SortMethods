#color class to define color type

class Color:
    def __init__(self, red: int, green: int, blue: int) -> None:
        self.red: int = red
        self.green: int = green
        self.blue: int = blue

        for color, color_str in [(self.red, "red"), (self.green, "green"), (self.blue, "blue")]:
            if not (0 <= color <= 255):
                raise Exception(f"Invalid color code for {color_str}")

    def getColor(self) -> tuple[int,int,int]:
        return self.red, self.green, self.blue





