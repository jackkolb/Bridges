class Force:
    name = "untitled force"
    force_type = "unspecified type"

    magnitude = 0

    multiplier_x = 0
    multiplier_y = 0
    multiplier_z = 0

    def __init__(self, force_type, magnitude, x, y, z, name="untitled force"):
        self.force_type = force_type
        self.magnitude = magnitude
        self.multiplier_x = x
        self.multiplier_y = y
        self.multiplier_z = z

        self.name = name
