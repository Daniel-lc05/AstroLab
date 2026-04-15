from .tank import Tank
from .FS_LOX import FS_LOX


fuel_rho = 8.10*10**(-7) # kg/mm^3
OF=2.6

FS_RP1 = Tank(
    name="First Stage Fuel Tank",

    # Structural material density
    material_rho= 2.7e-6 ,  # same structure material as FS_LOX (adjust if needed)

    # Rigid body properties
    r_cg_local=[0, 0, 1.5],
    I_cg_local=[[100, 0, 0], [0, 200, 0], [0, 0, 100]],

    # Tank configuration
    oxidizer=False,
    fuel_type="RP1",
    fuel_rho = fuel_rho,  # kg/mm^3

    # Mixture ratio reference
    OF=OF,
    
    # Geometry
    thickness=5,
    length=FS_LOX.length * (FS_LOX.fuel_rho / (OF * fuel_rho)),
    radius=150,


    # Vehicle hierarchy
    stage=1,
    parent=None
)