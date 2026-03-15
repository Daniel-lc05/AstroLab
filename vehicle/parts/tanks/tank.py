from ..base import Part
from tools import *

class Tank(Part):
    """
    Cylindrical tank
    Assumptions for cgz():
    - Local origin at tank geometrical centre (0,0,0)
    - z axis along tank length (vertical)
    - Liquid settles towards -z (towards the bottom)
    """

    def __init__(
        self,
        name: str,
        material_rho: float,
        r_cg_local,
        I_cg_local,
        oxidizer: bool,
        thickness: float,
        length: float,
        radius: float,
        fuel_type: str,
        fuel_rho: float,
        OF: float,
        stage: int,
        parent=None,
        p_parent_child=None,
        R_parent_child=None,
    ):
        self.oxidizer = bool(oxidizer)
        self.thickness = float(thickness)

        self.length = float(length)
        self.radius = float(radius)

        self.fuel_type = str(fuel_type)
        self.fuel_rho = float(fuel_rho)
        self.OF = float(OF)

        # ----- volumes (minimal, consistent) -----
        r_i = self.radius - self.thickness
        if r_i <= 0.0 or self.length <= 0.0:
            raise ValueError("Invalid geometry: radius - thickness and length must be > 0")

        # Structural material volume (hollow cylinder)
        struct_volume = float(np.pi * self.length * (self.radius**2 - r_i**2))

        # Fuel volume (inner cylinder)
        self.fuel_volume = float(np.pi * self.length * (r_i**2))

        # Fuel mass (assume full initially)
        self.fuel_mass = float(self.fuel_rho * self.fuel_volume)
        self.fuel_mass0 = float(self.fuel_mass)

        super().__init__(
            name=name,
            material_rho=float(material_rho),
            volume=struct_volume,
            r_cg_local=np.asarray(r_cg_local, dtype=float).copy(),
            I_cg_local=np.asarray(I_cg_local, dtype=float),
            aero=False,
            stage=stage,
            parent=parent,
            p_parent_child=p_parent_child,
            R_parent_child=R_parent_child,
        )

        # Initialize CG according to current fill
        self.update_cg_local()

        # Make CG read-only from outside (prevents in-place edits)
        self.r_cg_local.setflags(write=False)

    def get_mass(self) -> float:
        return float(self.mass_dry + self.fuel_mass)

    def drain(self, output: float) -> None:
        if not isinstance(output, (int, float)):
            raise TypeError("Output value must be numerical")

        new_mass = max(0.0, self.fuel_mass - float(output))
        if new_mass != self.fuel_mass:
            self.fuel_mass = new_mass
            self.update_cg_local()
            self.mark_dirty()

    def volume(self) -> float:
        return float(np.pi * (self.radius ** 2) * self.length)

    def cgz(self) -> float:
        """
        Returns z position of the combined CG (dry tank at z=0 + liquid),
        relative to the tank geometrical centre.
        """
        mf = self.fuel_mass
        m0 = self.fuel_mass0
        mt = self.mass_dry + mf

        if m0 <= 0.0 or mt <= 0.0 or self.length <= 0.0:
            return 0.0

        H = 0.5 * self.length  # half-height, centre -> end
        # liquid CG relative to centre: 0 at full, -H at empty
        cgz = (((mf / m0) - 1.0) * H * mf) / mt
        return float(cgz)

    def update_cg_local(self) -> None:
        """
        Updates self.r_cg_local to reflect current propellant level.
        Keeps x,y as-is and overwrites z.
        """
        z = self.cgz()

        # Temporarily allow writing, update, then lock again
        self.r_cg_local.setflags(write=True)
        self.r_cg_local[2] = z
        self.r_cg_local.setflags(write=False)