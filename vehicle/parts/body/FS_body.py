from .body import Body

FS_BODY = Body(
    name="First Stage Fuselage",
    material_rho=2700.0,     # Aluminum
    length=12.0,             # m
    radius=1.2,              # m
    thickness=0.005,         # m
    r_cg_local=[0.0, 0.0, 0.0],
    aero=True,
    core=True,
    stage=1,
    parent=None,
    p_parent_child=[0.0, 0.0, 0.0],
    R_parent_child=None,
)