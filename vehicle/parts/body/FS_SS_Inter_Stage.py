from .body import Body

FS_SS_Inter_Stage = Body(
    name="First Stage Second Stage Interstage",
    material_rho=2.7e-6,  # Aluminum kg/mm³
    length=3000,             # m
    radius=2000,              # m
    thickness=5,         # m
    r_cg_local=[0.0, 0.0, 0.0],
    aero=True,
    core=True,
    stage=1,
    parent=None,
    p_parent_child=[0.0, 0.0, 0.0],
    R_parent_child=None,
)