import math

G = 6.674 * (10 ** 11)


class Body:
    def __init__(self, mass, name):
        self.mass = mass
        self.name = name
        self.orbitRadius = 0
        self.parent_system = 0
        self.period = 0

    def set_parent_system(self, parent):
        self.parent_system = parent

    def calculate_total_mass(self):
        return self.mass

    def calculate_orbital_period(self):
        radius_cubed = self.orbitRadius * self.orbitRadius * self.orbitRadius
        num = 4 * math.pi * math.pi * radius_cubed
        denominator = G * self.parent_system.center.mass
        self.period = math.sqrt(num / denominator)

    def get_orbit_angle(self, time):
        if self.period == 0:
            return 0
        return 2 * math.pi * ((time % self.period) / self.period)

    # relative to its parent.
    def get_position_relative(self, time):
        angle = self.get_orbit_angle(time)
        x = self.orbitRadius * math.cos(angle)
        y = self.orbitRadius * math.sin(angle)
        return x, y

    def get_position_absolute(self, time):
        if self.parent_system == 0:  # if I have no parent, I must be the sun.
            return 0.0, 0.0      # the sun is the center of the system.
        x_self, y_self = self.get_position_relative(time)
        x_parent_system, y_parent_system = self.parent_system.get_position_absolute(time)
        return x_self + x_parent_system, y_self + y_parent_system

    # only between two children of the same system
    def get_distance_to(self, other, time):
        x1, y1 = self.get_position_absolute(time)
        x2, y2 = other.get_position_absolute(time)
        return math.sqrt((y1 - y2)**2 + (y1 - y2)**2)


class System(Body):
    def __init__(self, name, center):
        self.name = name
        self.center = center # can be a SYSTEM.
        center.set_parent_system(self)
        self.children = []
        self.mass = self.calculate_total_mass()
        Body.__init__(self, self.mass, name)

    def add_child_body(self, body, orbit_radius):
        self.children.append(body)
        body.set_parent_system(self)
        body.orbitRadius = orbit_radius
        body.calculate_orbital_period()
        self.mass = self.calculate_total_mass()

    def calculate_total_mass(self):
        return self.mass_helper(self.children, 0) + self.center.calculate_total_mass()

    def mass_helper(self, bodies, total):
        # give me that tail end recursion
        if not bodies:  # if list empty
            return total
        else:
            return self.mass_helper(bodies[1:], total + bodies[0].calculate_total_mass())
        return 


class Sun(Body):
    def __init__(self, mass, name):
        Body.__init__(self, mass, name)
        self.mass = mass
        self.name = name
        self.period = 0


class Planet(Body):
    def __init__(self, mass, name):
        Body.__init__(self, mass, name)
        

def test_system():
    print('Building Test System')
    sol = Sun(10, 'Sol')
    solar = System('SomeSystem', sol)

    print(solar.mass)

    hermes = Planet(1, 'Hermes')
    solar.add_child_body(hermes, 40)

    print(solar.mass)

    earth = Planet(4, 'Orthe')
    moon = Planet(1, 'Moon')

    earth_moon = System('Earth-Moon',earth)
    earth_moon.add_child_body(moon, 3)

    solar.add_child_body(earth_moon, 70)

    print(solar.mass)

    time = 0
    for x in range(0, 4):
        time = x * math.pi * .00001
        print("At t=" + str(time))
        print(sol.get_position_absolute(time))
        print(hermes.get_position_absolute(time))
        print(earth.get_position_absolute(time))
        print(moon.get_position_absolute(time))

    return solar


test_system()
