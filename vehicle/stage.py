from tools import *

class Stage:
    """
    Logical container grouping parts that belong to the same rocket stage.
    """

    def __init__(self, id: int):
        self.id = int(id)
        self.parts: list["Part"] = []

    # --------------------------
    # Add parts
    # --------------------------

    def add_part(self, part):
        if part.stage != self.id:
            raise ValueError(f"{part.name} stage mismatch")

        self.parts.append(part)

    # --------------------------
    # Get parts
    # --------------------------


    def get_parts(self):
        return self.parts


    # --------------------------
    # Mass
    # --------------------------

    
    def get_fuel_mass(self):
        mass_0=0
        for t in self.parts:
            if isinstance(part, Tank):
                mass_0 += p.fuel_mass0
        return mass_0
    

    def get_initial_fuel_mass(self):
        mass=0
        for t in self.parts:
            if isinstance(part, Tank):
                mass += p.fuel_mass
        return mass
    
    def get_mass(self):
        mass = 0.0

        for p in self.parts:
            mass += p.mass_dry
            if hasattr(p, "fuel_mass"):
                mass += p.fuel_mass

        return mass

    # --------------------------
    # Center of mass
    # --------------------------

    def get_cg(self):

        M = 0
        r = np.zeros(3)

        for p in self.parts:

            m = p.mass_dry
            if hasattr(p, "fuel_mass"):
                m += p.fuel_mass

            cg = p.get_cg()

            M += m
            r += m * cg

        if M == 0:
            return np.zeros(3)

        return r / M

    # --------------------------
    # Inertia (about stage CG)
    # --------------------------

    def get_inertia(self):

        cg_stage = self.get_cg()
        I_total = np.zeros((3,3))

        for p in self.parts:

            m = p.mass_dry
            if hasattr(p, "fuel_mass"):
                m += p.fuel_mass

            I = p.get_inertia()

            r = p.get_cg() - cg_stage

            I_shift = m * (
                np.dot(r,r)*np.eye(3) - np.outer(r,r)
            )

            I_total += I + I_shift

        return I_total