from tools import *

class Body:

    def __init__(self, radius, rho):
        self.radius = radius
        self.rho = rho

    @property
    def volume(self):
        return (4/3) * np.pi * self.radius**3

    @property
    def mass(self):
        return self.volume * self.rho
    

