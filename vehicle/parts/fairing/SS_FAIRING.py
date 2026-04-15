from .fairing import Fairing
from tools import *

SS_FAIRING = Fairing(
    name="Main Fairing",
    material_rho = 2.7e-6 ,   # kg/m^3, por ejemplo aluminio
    thickness= 3,          # mm
    length=850,           # mm
    base_radius=150,      # mm
    main=True,
    stage=2,
    parent=None,
    p_parent_child=[0.0, 0.0, 0.0],
    R_parent_child=np.eye(3),
)