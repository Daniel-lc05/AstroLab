################
# FIRST  STAGE #
################
from vehicle.parts.tanks.FS_RP1 import FS_RP1
from vehicle.parts.tanks.FS_LOX import FS_LOX
from vehicle.parts.body.FS_BODY import FS_BODY
from vehicle.parts.engines.FS_engine import FS_engine

################
# SECOND STAGE #
################


from vehicle.parts.fairing.SS_FAIRING import SS_FAIRING
from vehicle.parts.body.SS_FAIRING_BASE import SS_FAIRING_BASE

################
#    LOGICAL   #
################

from vehicle.stage import Stage
from vehicle.rocket import *
from vehicle.stages import *
from tools import *


def VAB():
    ################
    # FIRST  STAGE #
    ################
    attach(
        child = FS_RP1,
        parent = FS_BODY,
        p_parent_child = [0,0,-1500]
    )

    attach(
        child = FS_LOX,
        parent = FS_BODY,
        p_parent_child = [0,0,1500]
    )
    attach(
        parent = FS_BODY,
        child = FS_engine,
        p_parent_child = [0,0,(FS_BODY.bottom-(FS_engine.length/2))]
    )


    ################
    # SECOND STAGE #
    ################

    attach(
        child = SS_FAIRING_BASE,
        parent = SS_FAIRING,
        p_parent_child = [0,0,SS_FAIRING_BASE.bottom-(SS_FAIRING_BASE.length/2)]
    )

    ################
    #    STAGES    #
    ################

    AstroLab = Rocket("AstroLab")
    Stage1.add_part(FS_BODY)
    for child in FS_BODY.children:
        Stage1.add_part(child)
    Stage2.add_part(SS_FAIRING)
    for child in SS_FAIRING.children:
        Stage2.add_part(child)
    

    AstroLab.add_stage(Stage1)
    AstroLab.add_stage(Stage2)

    return AstroLab