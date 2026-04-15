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
    name="AQUILA-S",
    mass_dry=12.0,          # kg
    length=650.0,           # mm
    radius=80.0,            # mm

    OF=2.6,
    fuel_type=("LOX", "RP1"),

    thrust_asl=5000.0,      # N
    thrust_vac=8200.0,     # N
    Isp_asl=255.0,          # s
    Isp_vac=285.0,          # s

    fuel_tank=FS_RP1,
    oxidizer_tank=FS_LOX,

    maxtime=20.0,           # s
    max_throttle=1.0,
    min_throttle=0.70,
    gimbal_max=3.0,         # deg

    stage=1,
    parent=None,
)