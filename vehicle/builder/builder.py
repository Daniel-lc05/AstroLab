################
# FIRST  STAGE #
################
from vehicle.parts.tanks.FS_RP1 import FS_RP1
from vehicle.parts.tanks.FS_LOX import FS_LOX
from vehicle.parts.body.FS_BODY import FS_BODY
from vehicle.parts.body.FS_SS_Inter_Stage import FS_SS_Inter_Stage
from vehicle.parts.engines.FS_engine import FS_engine

################
# SECOND STAGE #
################

from vehicle.parts.tanks.SS_RP1 import SS_RP1
from vehicle.parts.tanks.SS_LOX import SS_LOX
from vehicle.parts.body.SS_BODY import SS_BODY

################
# THIRD  STAGE #
################

from vehicle.parts.fairing.TS_FAIRING import TS_FAIRING
from vehicle.parts.body.TS_FAIRING_BASE import TS_FAIRING_BASE

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
        child = FS_SS_Inter_Stage,
        p_parent_child = [0,0,(FS_BODY.top)+abs((FS_SS_Inter_Stage.bottom))]
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
        child = SS_RP1,
        parent = SS_BODY,
        p_parent_child = [0,0,-1500]
    )

    attach(
        child = SS_LOX,
        parent = SS_BODY,
        p_parent_child = [0,0,1500]
    )

    ################
    # THIRD  STAGE #
    ################

    attach(
        child = TS_FAIRING_BASE,
        parent = TS_FAIRING,
        p_parent_child = [0,0,TS_FAIRING_BASE.bottom-(TS_FAIRING_BASE.length/2)]
    )

    ################
    #    STAGES    #
    ################

    AstroLab = Rocket("AstroLab")
    Stage1.add_part(FS_BODY)
    Stage2.add_part(SS_BODY)
    Stage3.add_part(TS_FAIRING)
    for child in FS_BODY.children:
        Stage1.add_part(child)
    for child in SS_BODY.children:
        Stage2.add_part(child)
    for child in TS_FAIRING.children:
        Stage3.add_part(child)
    

    AstroLab.add_stage(Stage1)
    AstroLab.add_stage(Stage3)
    AstroLab.add_stage(Stage2)

    return AstroLab