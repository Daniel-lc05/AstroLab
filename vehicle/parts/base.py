from tools import *

class Part:
    """
    Rigid body element inside a hierarchical rocket structure.
    """
    def __init__(
        self,
        name: str,
        material_rho: float,
        volume: float,
        r_cg_local: np.ndarray,
        I_cg_local: np.ndarray,
        aero: bool = False,
        core: bool = False,
        main: bool = False,
        top: float = 0,
        bottom: float = 0,
        stage: int = 0,
        parent = None,
        p_parent_child: np.ndarray | None = None,
        R_parent_child: np.ndarray | None = None,
    ):
        self.name = name

        # Physical properties (defined in local frame)
        self.material_rho = float(material_rho)
        self.volume = float(volume)
        self.vehicle_internal_pos = np.zeros(3)
        self.mass_dry = float(material_rho*volume)
        self.r_cg_local = np.asarray(r_cg_local, dtype=float)
        self.I_cg_local = np.asarray(I_cg_local, dtype=float)

        # Flags / metadata
        self.aero = bool(aero)
        self.core = bool(core)
        self.main = bool(main)

        # Hierarchy
        self.stage = int(stage)
        self.parent = parent
        self.children: list["Part"] = []
        self.top: float(top)
        self.bottom: float(bottom)

        # Dirty flag (recompute derived stuff when True)
        self.dirty = True

        if parent is not None:
            parent.add_child(self)

        # Transform relative to parent
        self.p_parent_child = (
            np.zeros(3) if p_parent_child is None else np.asarray(p_parent_child, dtype=float)
        )
        self.R_parent_child = (
            np.eye(3) if R_parent_child is None else np.asarray(R_parent_child, dtype=float)
        )

    # --------------------------
    # Dirty management
    # --------------------------

    def mark_dirty(self) -> None:
        """Mark this node (and ancestors) as needing recomputation."""
        if self.dirty:
            return
        self.dirty = True
        if self.parent is not None:
            self.parent.mark_dirty()

    # --------------------------
    # Hierarchy management
    # --------------------------

    def add_child(self, child: "Part") -> None:
        self.children.append(child)
        child.parent = self
        self.mark_dirty()

    # --------------------------
    # Transformations
    # --------------------------

    def set_parent_transform(
        self,
        p_parent_child: np.ndarray | None = None,
        R_parent_child: np.ndarray | None = None,
    ) -> None:
        """Update transform relative to parent and mark dirty."""
        if p_parent_child is not None:
            self.p_parent_child = np.asarray(p_parent_child, dtype=float)
        if R_parent_child is not None:
            self.R_parent_child = np.asarray(R_parent_child, dtype=float)
        self.mark_dirty()

    def get_pose(self):
        """
        Returns (R_stage, p_stage)
        """
        if self.parent is None:
            return self.R_parent_child, self.p_parent_child

        R_parent, p_parent = self.parent.get_pose()
        R = R_parent @ self.R_parent_child
        p = p_parent + R_parent @ self.p_parent_child
        return R, p
    
    def set_local_frame_pos(self,pos):
        self.vehicle_internal_pos = (0,0,pos)


    # --------------------------
    # Mass
    # --------------------------

    def get_mass(self) -> float:
        if hasattr(self, "fuel_mass"):
            return self.mass_dry + self.fuel_mass
        return self.mass_dry
    
    

    # --------------------------
    # Center of Mass
    # --------------------------

    def get_cg(self):
        """
        Returns CG in coordinates.
        """
        R, p = self.get_pose()
        return p + R @ self.r_cg_local

    # --------------------------
    # Inertia in stage frame
    # --------------------------

    def get_inertia(self):
        """
        Returns inertia matrix in frame,
        expressed about the part's own CG.
        """
        R, _ = self.get_pose()
        return R @ self.I_cg_local @ R.T