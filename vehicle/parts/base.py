import numpy as np


class Part:
    """
    Rigid body element inside a hierarchical rocket structure.
    """
    def __init__(
        self,
        name: str,
        mass_dry: float,
        r_cg_local: np.ndarray,
        I_cg_local: np.ndarray,
        parent=None,
        p_parent_child: np.ndarray = None,
        R_parent_child: np.ndarray = None,
    ):
        self.name = name

        # Physical properties (defined in local frame)
        self.mass_dry = mass_dry
        self.r_cg_local = np.asarray(r_cg_local, dtype=float)
        self.I_cg_local = np.asarray(I_cg_local, dtype=float)

        # Hierarchy
        self.parent = parent
        self.children = []

        if parent is not None:
            parent.add_child(self)

        # Transform relative to parent
        self.p_parent_child = (
            np.zeros(3) if p_parent_child is None else np.asarray(p_parent_child)
        )
        self.R_parent_child = (
            np.eye(3) if R_parent_child is None else np.asarray(R_parent_child)
        )

    # --------------------------
    # Hierarchy management
    # --------------------------

    def add_child(self, child):
        self.children.append(child)
        child.parent = self

    # --------------------------
    # Transformations
    # --------------------------

    def get_global_pose(self):
        """
        Returns (R_global, p_global)
        """
        if self.parent is None:
            return self.R_parent_child, self.p_parent_child

        R_parent, p_parent = self.parent.get_global_pose()

        R = R_parent @ self.R_parent_child
        p = p_parent + R_parent @ self.p_parent_child

        return R, p

    # --------------------------
    # Center of Mass
    # --------------------------

    def get_global_cg(self):
        """
        Returns CG in global coordinates.
        """
        R, p = self.get_global_pose()
        return p + R @ self.r_cg_local

    # --------------------------
    # Inertia in global frame
    # --------------------------

    def get_global_inertia(self):
        """
        Returns inertia matrix in global frame,
        expressed about the part's own CG.
        """
        R, _ = self.get_global_pose()
        return R @ self.I_cg_local @ R.T