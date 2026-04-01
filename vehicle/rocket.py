from enviroment.enviroment import *
from tools import *
from vehicle.stage import Stage
from vehicle.stages import *

class Rocket:

    def __init__(self, name: str):
        self.name = name
        self.stages = []
        self.Cd = 1.64
        self.area = 3

    def add_stage(self, stage):
        self.stages.append(stage)

    def get_stages(self):   
        return sorted(self.stages, key=lambda s: s.id, reverse=False)

    def get_total_mass(self):
        return sum(p.get_mass() for p in self.stages)
    
    
    def get_parts(self):
        parts= []
        for s in self.stages:
            stage_parts = s.parts
            for p in stage_parts:
                parts.append(p)
        return parts

    def get_main_part(self):
        mp=None
        parts = self.get_parts()
        for part in parts:
            if part.main:
                mp=part
        return mp


    def get_active_engines(self):
        active = []
        for part in self.get_parts():
            if hasattr(part,"thrust_asl") and part.status:
                active.append(part)
        return active
    
    
    def burn_fuel(self,throtle,dt):
        for e in self.get_active_engines():
            e.burn(throtle,dt)


    def get_total_thrust_vector1D(self,h,throttle): 
        active=self.get_active_engines()
        thrust=0
        for engine in active:
            thrust+=engine.get_thrust(get_atm_p(h),throttle)
        
        if thrust> 0:
            return thrust
        else:
            return 0




    """def cg(self):
        m_total = self.total_mass()
        if m_total == 0:
            return np.zeros(3)

        cg = np.zeros(3)

        for s in self.stages:
            for p in (s.get_cg()):

                
            
        return cg / m_total"""