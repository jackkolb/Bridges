import Force
import math


class Joint:
    name = ""

    position_x = 0
    position_y = 0
    position_z = 0

    forces = []

    # joint constructor
    def __init__(self, x, y, z, name=""):
        self.position_x = x
        self.position_y = y
        self.position_z = z
        self.forces = []
        self.name = name
        return

    # adds a force to the external loads
    def add_force(self, magnitude, x, y, z):
        force = Force.Force("external", float(magnitude), x, y, z)
        self.forces.append(force)
        return

    # add a connection to the loads (calculate multipliers, placeholder magnitudes)
    def add_connection(self, joint):
        dx = joint.position_x - self.position_x
        dy = joint.position_y - self.position_y
        dz = joint.position_z - self.position_z

        # calculate angles, if angles are negative keep them positive for consistency
        theta_xy = math.atan(dy / dx) if dx != 0 else 0
        if theta_xy < 0:
            theta_xy *= -1

        theta_xz = math.atan(dz / dx) if dx != 0 else 0
        if theta_xz < 0:
            theta_xz *= -1

        multiplier_x = dx / (math.sqrt(dx**2 + dy**2 + dz**2))
        multiplier_y = dy / (math.sqrt(dx**2 + dy**2 + dz**2))
        multiplier_z = dz / (math.sqrt(dx**2 + dy**2 + dz**2))

        # invert negative values for consistency (default in tension, negative in compression)
        if dx < 0: multiplier_x *= -1
        if dy < 0: multiplier_y *= -1
        if dz < 0: multiplier_z *= -1

        force_title = [self.name, joint.name]
        force_title.sort()
        force_title = force_title[0] + force_title[1]

        force = Force.Force("beam", 0, multiplier_x, multiplier_y, multiplier_z, name=force_title)
        self.forces.append(force)
        return

    # generates the sum of forces equations (x, y, z) in a dictionary form of name and modifier
    def force_balance_equations(self):
        equation_x = dict()
        equation_y = dict()
        equation_z = dict()

        equation_x["external"] = 0
        equation_y["external"] = 0
        equation_z["external"] = 0

        for force in self.forces:
            if force.force_type == "beam":
                equation_x[force.name] = force.multiplier_x
                equation_y[force.name] = force.multiplier_y
                equation_z[force.name] = force.multiplier_z

            if force.force_type == "external":
                equation_x["external"] += force.multiplier_x * force.magnitude
                equation_y["external"] += force.multiplier_y * force.magnitude
                equation_z["external"] += force.multiplier_z * force.magnitude

        return equation_x, equation_y, equation_z
