from Image.RGB import RGB


class RGBCountable(RGB):
    count: int = 0

    def __init__(self, crgb:tuple[int, tuple[float]] | tuple[int, tuple[float, float]] | tuple[int, tuple[float, float, float]]):

        if len(crgb[1]) == 3:
            super().__init__(crgb[1][0], crgb[1][1], crgb[1][2])
            self.count = crgb[0]

        if len(crgb[1]) == 2:
            super().__init__(crgb[1][0], crgb[1][1], 0)
            self.count = crgb[0]

        if len(crgb[1]) == 1:
            super().__init__(crgb[1][0], 0, 0)
            self.count = crgb[0]

    def to_hex(self):
        return '#%02x%02x%02x' % (self.red, self.green, self.blue)