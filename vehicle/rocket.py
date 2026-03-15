from tools import *

class Rocket:

    def __init__(self, name: str):
        self.name = name
        self.stages = []

    def add_stage(self, stage):
        self.stages.append(stage)

    def get_stages(self):
        return self.stages

    def total_mass(self):
        return sum(p.get_mass() for p in self.stages)
    
    def get_parts(self):
        parts= []
        for s in self.stages:
            stage_parts = s.parts
            for p in stage_parts:
                parts.append(p)
        return parts


    """def cg(self):
        m_total = self.total_mass()
        if m_total == 0:
            return np.zeros(3)

        cg = np.zeros(3)

        for s in self.stages:
            for p in (s.get_cg()):

                
            
        return cg / m_total"""