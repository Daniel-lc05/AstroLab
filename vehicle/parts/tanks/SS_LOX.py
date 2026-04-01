from .tank import Tank

SS_LOX = Tank(
    name="Second Stage Oxidizer Tank",

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
    length=1000,
    radius=1990,

    # Mixture ratio reference
    OF=2.6,

    # Vehicle hierarchy
    stage=2,
    parent=None
)