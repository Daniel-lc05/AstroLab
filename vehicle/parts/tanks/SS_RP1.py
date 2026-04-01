from .tank import Tank
from .SS_LOX import SS_LOX

SS_RP1 = Tank(
    name="Second Stage Fuel Tank",

    # Structural material density
    material_rho= 2.7e-6 ,  # same structure material as FS_LOX (adjust if needed)

    # Rigid body properties
    r_cg_local=[0, 0, 1.5],
    I_cg_local=[[100, 0, 0], [0, 200, 0], [0, 0, 100]],

    # Tank configuration
    oxidizer=False,
    fuel_type="RP1",
    fuel_rho = 8.10*10**(-7),  # kg/mm^3

    # Geometry
    thickness=5,
    length=SS_LOX.length*2.6,
    radius=1990,

    # Mixture ratio reference
    OF=2.6,

    # Vehicle hierarchy
    stage=2,
    parent=None
)