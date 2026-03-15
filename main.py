#from vehicle.parts.tanks.FS_LOX import FS_LOX
from vehicle.parts.tanks.FS_RP1 import FS_RP1
from vehicle.parts.tanks.FS_LOX import FS_LOX
from vehicle.stage import Stage
from vehicle.rocket import *
from vehicle.stages import *
from enviroment.body import *

from tools import *
from vehicle.parts.body.FS_body import FS_BODY

def assembly():
    attach(
        child = FS_RP1,
        parent = FS_BODY,
        p_parent_child = [0,0,-1.5]
    )

    attach(
        child = FS_LOX,
        parent = FS_BODY,
        p_parent_child = [0,0,1.5]
    )
    




def main():
    AstroLab = Rocket("AstroLab")
    Stage1.add_part(FS_BODY)
    for child in FS_BODY.children:
        Stage1.add_part(child)

    AstroLab.add_stage(Stage1)

    #print(Stage1.get_cg())    
    
    for p in (AstroLab.get_parts()):
        print (p.get_relative_pose())

assembly()
main()