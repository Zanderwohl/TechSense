import math

G = 6.674 * (10 ** 11)

class Body:
    def __init__(self, mass, name):
        self.mass = mass
        self.name = name
        self.orbitRadius = 0
        self.system = 0
        self.period = 0
    
    def setSystem(self, system):
        self.system = system

    def calcMass(self):
        return self.mass

    def calcPeriod(self):
        radCubed = self.orbitRadius * self.orbitRadius * self.orbitRadius
        num = 4 * math.pi * math.pi * radCubed
        denom = G * self.system.center.mass
        self.period = math.sqrt(num / denom)

    def getAngle(self, time):
        if self.period == 0:
            return 0
        return 2 * math.pi * ((time % self.period) / self.period)

    #relative to its parent.
    def getPositionRelative(self, time):
        angle = self.getAngle(time)
        x = self.orbitRadius * math.cos(angle)
        y = self.orbitRadius * math.sin(angle)
        return (x, y)

    def getPosition(self, time):
        if(self.system == 0):  #if I have no parent, I must be the sun.
            return (0.0, 0.0)      #the sun is the center of the system.
        xSelf, ySelf = self.getPositionRelative(time)
        xSystem, ySystem = self.system.getPosition(time)
        return (xSelf + xSystem, ySelf + ySystem)

    #only between two children of the same system
    def getDistance(self, other, time):
        x1, y1 = getPosition(self, time)
        x2, y2 = getPosition(other, time)
        return math.sqrt((y1 - y2)**2 + (y1 - y2)**2)

class System(Body):
    def __init__(self, name, center):
        self.name = name
        self.center = center #can be a SYSTEM.
        center.setSystem(self)
        self.children = []
        self.mass = self.calcMass()
        Body.__init__(self, self.mass, name)

    def addBody(self, body, orbitRadius):
        self.children.append(body)
        body.setSystem(self)
        body.orbitRadius = orbitRadius
        body.calcPeriod()
        self.mass = self.calcMass()

    def calcMass(self):
        return self.massHelper(self.children, 0) + self.center.calcMass()

    def massHelper(self, bodies, total):
        #give me that tail end recursion
        if not bodies: #if list empty
            return total
        else:
            return self.massHelper(bodies[1:],total+bodies[0].calcMass())
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
        
    



def testSystem():
    print('hello')
    sol = Sun(10, 'Sol')
    solar = System('SomeSystem',sol)

    print(solar.mass)

    hermes = Planet(1, 'Hermes')
    solar.addBody(hermes, 40)

    print(solar.mass)

    earth = Planet(4, 'Terra')
    moon = Planet(1, 'Moon')

    earthmoon = System('Earth-Moon',earth)
    earthmoon.addBody(moon, 3)

    solar.addBody(earthmoon, 70)

    print(solar.mass)

    time = 0
    for x in range(0, 4):
        time = x * math.pi * .00001
        print("At t=" + str(time))
        print(sol.getPosition(time))
        print(hermes.getPosition(time))
        print(earth.getPosition(time))
        print(moon.getPosition(time))

    return solar

testSystem()
