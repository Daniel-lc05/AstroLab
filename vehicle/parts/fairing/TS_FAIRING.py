from .fairing import Fairing
from tools import *

TS_FAIRING = Fairing(
    name="Main Fairing",
    material_rho = 2.7e-6 ,   # kg/m^3, por ejemplo aluminio
    thickness= 3,          # mm
    length=2500,           # mm
    base_radius=2000,      # mm
    main=True,
    stage=3,
    parent=None,
    p_parent_child=[0.0, 0.0, 0.0],
    R_parent_child=np.eye(3),
)