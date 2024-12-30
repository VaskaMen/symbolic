class RGB:
    red: float | int
    green: float | int
    blue: float | int

    def __init__(self, r: float | int, g: float | int, b: float | int):
        self.red = r
        self.green = g
        self.blue = b

    def get_difference(self, color):
        difference = 0
        difference += abs(self.red - color.red)
        difference += abs(self.green - color.green)
        difference += abs(self.blue - color.blue)
        return difference