from .body import Body

FS_BODY = Body(
    name="First Stage Fuselage",
    material_rho=2.7e-6,  # Aluminum kg/mm³
    length=2500.0,             # mm
    radius=150,              # mm
    thickness=5,         # mm
    r_cg_local=[0.0, 0.0, 0.0],
    aero=True,
    core=True,
    stage=1,
    parent=None,
    p_parent_child=[0.0, 0.0, 0.0],
    R_parent_child=None,
)