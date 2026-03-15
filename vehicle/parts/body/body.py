from ..base import Part
from tools import *

class Body(Part):
    """
    Cylindrical fuselage / body tube.
    Assumptions:
    - Axis aligned with local z
    - Local origin at geometric center
    """

    def __init__(
        self,
        name: str,
        material_rho: float,
        length: float,
        radius: float,
        thickness: float,
        r_cg_local=None,
        I_cg_local=None,
        aero: bool = True,
        core: bool = True,
        stage: int = 0,
        parent=None,
        p_parent_child=None,
        R_parent_child=None,
    ):
        self.length = float(length)
        self.radius = float(radius)
        self.thickness = float(thickness)

        if self.thickness <= 0:
            raise ValueError("thickness must be > 0")
        if self.radius <= 0:
            raise ValueError("radius must be > 0")
        if self.length <= 0:
            raise ValueError("length must be > 0")
        if self.thickness >= self.radius:
            raise ValueError("thickness must be smaller than radius")

        # Geometría
        self.outer_volume = np.pi * self.radius**2 * self.length
        self.inner_radius = self.radius - self.thickness
        self.inner_volume = np.pi * self.inner_radius**2 * self.length

        # Volumen real de material
        material_volume = self.outer_volume - self.inner_volume

        # Centro de gravedad local por defecto
        if r_cg_local is None:
            r_cg_local = np.array([0.0, 0.0, 0.0])

        # Masa seca
        mass_dry = material_rho * material_volume

        # Inercia aproximada de cilindro hueco
        if I_cg_local is None:
            r_out = self.radius
            r_in = self.inner_radius
            m = mass_dry
            L = self.length

            Izz = 0.5 * m * (r_out**2 + r_in**2)
            Ixx = Iyy = (1/12) * m * (3 * (r_out**2 + r_in**2) + L**2)

            I_cg_local = np.array([
                [Ixx, 0.0, 0.0],
                [0.0, Iyy, 0.0],
                [0.0, 0.0, Izz],
            ])

        super().__init__(
            name=name,
            material_rho=material_rho,
            volume=material_volume,
            r_cg_local=np.asarray(r_cg_local, dtype=float),
            I_cg_local=np.asarray(I_cg_local, dtype=float),
            aero=aero,
            core=core,
            stage=stage,
            parent=parent,
            p_parent_child=p_parent_child,
            R_parent_child=R_parent_child,
        )

        self.surface_area = 2 * np.pi * self.radius * self.length

    # --------------------------
    # Geometry
    # --------------------------

    def get_volume(self) -> float:
        return self.volume  

    def get_outer_volume(self) -> float:
        return self.outer_volume

    def get_inner_volume(self) -> float:
        return self.inner_volume

    def get_surface_area(self) -> float:
        return self.surface_area