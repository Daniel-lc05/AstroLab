from .tank import Tank

FS_LOX = Tank(
    name="First Stage Oxidizer Tank",

    # Structural material density
    material_rho=2700,  # e.g. aluminium density

    # Rigid body properties
    r_cg_local=[0, 0, 0],
    I_cg_local=[[100, 0, 0], [0, 200, 0], [0, 0, 100]],

    # Tank configuration
    oxidizer=True,
    fuel_type="LOX",
    fuel_rho=1141,   #LOX density


    # Geometry
    thickness=5,
    length=1000,
    radius=200,

    # Mixture ratio reference
    OF=2.6,

    # Vehicle hierarchy
    stage=1,
    parent=None
)