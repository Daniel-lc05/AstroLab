from ..base import Part
from tools import *


class Fairing(Part):
    """
    Hollow paraboloid fairing.

    Convention:
    - Local origin is placed at the paraboloid centroid (CG).
    - +z points toward the tip.
    - Therefore:
        bottom = -L/3
        top    = +2L/3

    Geometry model:
    - Structural volume is approximated as:
        outer paraboloid - inner paraboloid
      using the same height and a reduced inner base radius.
    """

    def __init__(
        self,
        name: str,
        material_rho: float,
        thickness: float,
        length: float,
        base_radius: float,
        r_cg_local: np.ndarray | None = None,
        I_cg_local: np.ndarray | None = None,
        aero: bool = True,
        core: bool = False,
        main: bool = False,
        stage: int = 0,
        parent=None,
        p_parent_child: np.ndarray | None = None,
        R_parent_child: np.ndarray | None = None,
    ):
        self.length = float(length)
        self.base_radius = float(base_radius)
        self.thickness = float(thickness)

        if self.length <= 0.0:
            raise ValueError("length must be > 0")
        if self.base_radius <= 0.0:
            raise ValueError("base_radius must be > 0")
        if self.thickness <= 0.0:
            raise ValueError("thickness must be > 0")
        if self.thickness >= self.base_radius:
            raise ValueError("thickness must be smaller than base_radius")

        # Paraboloid logic with origin at centroid
        self.bottom = -self.length / 3.0
        self.top = 2.0 * self.length / 3.0

        r_i = self.base_radius - self.thickness

        # Structural volume: outer paraboloid - inner paraboloid
        outer_volume = 0.5 * np.pi * self.base_radius**2 * self.length
        inner_volume = 0.5 * np.pi * r_i**2 * self.length
        struct_volume = float(outer_volume - inner_volume)

        # Local CG at origin by convention
        if r_cg_local is None:
            r_cg_local = np.array([0.0, 0.0, 0.0], dtype=float)
        else:
            r_cg_local = np.asarray(r_cg_local, dtype=float)
            if r_cg_local.shape != (3,):
                raise ValueError("r_cg_local must be a 3-component vector")

        # Rough inertia approximation if not provided
        if I_cg_local is None:
            mass = float(material_rho) * struct_volume
            R = self.base_radius
            L = self.length

            Ixx = mass * (3.0 * R**2 + 4.0 * L**2) / 20.0
            Iyy = Ixx
            Izz = 3.0 * mass * R**2 / 10.0

            I_cg_local = np.array(
                [
                    [Ixx, 0.0, 0.0],
                    [0.0, Iyy, 0.0],
                    [0.0, 0.0, Izz],
                ],
                dtype=float,
            )
        else:
            I_cg_local = np.asarray(I_cg_local, dtype=float)
            if I_cg_local.shape != (3, 3):
                raise ValueError("I_cg_local must be a 3x3 matrix")

        super().__init__(
            name=name,
            material_rho=float(material_rho),
            volume=struct_volume,
            r_cg_local=r_cg_local,
            I_cg_local=I_cg_local,
            aero=aero,
            core=core,
            main=main,
            top=self.top,
            bottom=self.bottom,
            stage=stage,
            parent=parent,
            p_parent_child=p_parent_child,
            R_parent_child=R_parent_child,
        )