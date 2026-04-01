################
#    LOGICAL   #
################
from vehicle.builder.builder import VAB
from vehicle.stage import Stage
from vehicle.rocket import *
from vehicle.stages import *
from tools import *
from solver.state import *
from solver.simulation_1d import *
from Analysis.plotter import *


def main():
    #print(get_pos_parts(FS_LOX,FS_BODY))
    #rocketo = AstroLab.get_sorted_parts()

    for p in AstroLab.get_parts():
        pos = get_pos_parts(p,AstroLab)
        p.set_local_frame_pos(pos)    

def simulate():
    simulation = Simulation1D(AstroLab,0.5,1000)
    simulation.run(initial_state)
    raw_data=simulation.get_data()
    ordered_data = order(raw_data)
    plotter(ordered_data)
    

AstroLab=VAB()
main()


initial_state = State(
    t=0.0,
    h=0.0,
    v=0.0,
)



#simulate()

print(AstroLab.get_total_mass()*9.81/1000)





"""
for p in AstroLab.get_parts():
    print(p.name,p.get_mass())
"""