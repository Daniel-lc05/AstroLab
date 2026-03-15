from .tank import Tank
from .FS_LOX import FS_LOX

FS_RP1 = Tank(
    name="First Stage Fuel Tank",

    # Structural material density
    material_rho=2700,  # same structure material as FS_LOX (adjust if needed)

    # Rigid body properties
    r_cg_local=[0, 0, 1.5],
    I_cg_local=[[100, 0, 0], [0, 200, 0], [0, 0, 100]],

    # Tank configuration
    oxidizer=False,
    fuel_type="RP1",
    fuel_rho=810,  # RP-1 density (adjust if needed)

    # Geometry
    thickness=5,
    length=FS_LOX.length*2.6,
    radius=200,

    # Mixture ratio reference
    OF=2.6,

    # Vehicle hierarchy
    stage=1,
    parent=None
)