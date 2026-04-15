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
    simulation = Simulation1D(AstroLab,0.1,290)
    simulation.run(initial_state)
    raw_data=simulation.get_data()
    ordered_data = order(raw_data)
    plotter(ordered_data)
    
def debug():
    for p in AstroLab.get_parts():
        print(p.name,p.length,"mm",p.get_mass(),"Kg")


AstroLab=VAB()
main()


initial_state = State(
    t=0.0,
    h=0.0,
    v=0.0,
)



simulate()