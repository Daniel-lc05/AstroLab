from .tank import Tank

FS_LOX = Tank(
    name="First Stage Oxidizer Tank",

    # Structural material density
    material_rho= 2.7e-6 ,  # e.g. aluminium density

    # Rigid body properties
    r_cg_local=[0, 0, 0],
    I_cg_local=[[100, 0, 0], [0, 200, 0], [0, 0, 100]],

    # Tank configuration
    oxidizer=True,
    fuel_type="LOX",
    fuel_rho = 1.141*10**(-6),  # kg/mm^3


    # Geometry
    thickness=5,
    length=680,
    radius=150,

    # Mixture ratio reference
    OF=2.6,

    # Vehicle hierarchy
    stage=1,
    parent=None
)