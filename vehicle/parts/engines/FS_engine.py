"""from .engine import Engine
from ..tanks.FS_LOX import FS_LOX
from ..tanks.FS_RP1 import FS_RP1

FS_engine = Engine(
    name="AQUILA-5",
    mass_dry=300.0,        # kg
    length=34.0,           # mm
    radius=3.0,            # mm
    OF= 5,
    fuel_type=("LOX","RP1"),

    thrust_asl=4.80e5,     # N
    thrust_vac=5.20e5,     # N
    Isp_asl=296.0,         # s
    Isp_vac=330.0,         # s

    fuel_tank=FS_RP1,
    oxidizer_tank=FS_LOX,
    maxtime=165.0,         # s
    max_throttle=1.0,      # adimensional
    min_throttle=0.7,      # adimensional
    gimbal_max=6.0,        # deg
    stage=1,
    parent=None,
)

"""

from .engine import Engine
from ..tanks.FS_LOX import FS_LOX
from ..tanks.FS_RP1 import FS_RP1
FS_engine = Engine(
    name="AQUILA-T",
    mass_dry=550.0,         # kg aprox, no 85
    length=2600.0,          # mm
    radius=450.0,           # mm

    OF=2.6,
    fuel_type=("LOX", "RP1"),

    thrust_asl=1.35e6,      # N
    thrust_vac=1.50e6,      # N
    Isp_asl=290.0,          # s
    Isp_vac=320.0,          # s

    fuel_tank=FS_RP1,
    oxidizer_tank=FS_LOX,

    maxtime=110.0,          # s
    max_throttle=1.0,
    min_throttle=0.70,
    gimbal_max=5.0,         # deg

    stage=1,
    parent=None,
)