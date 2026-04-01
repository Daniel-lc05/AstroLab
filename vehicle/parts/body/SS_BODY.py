from .body import Body

SS_BODY = Body(
    name="Second Stage Fuselage",
    material_rho=2.7e-6,  # Aluminum kg/mm³
    length=8000,             # mm
    radius=2000,              # mm
    thickness=5,         # mm
    r_cg_local=[0.0, 0.0, 0.0],
    aero=True,
    core=True,
    stage=2,
    parent=None,
    p_parent_child=[0.0, 0.0, 0.0],
    R_parent_child=None,
)