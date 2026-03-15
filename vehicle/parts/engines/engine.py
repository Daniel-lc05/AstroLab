from ..base import Part
from tools import *


class Engine(Part):
    """
    Rocket engine physical model.

    This class only describes the engine and provides physical calculations.
    It does NOT perform simulation steps or drain propellant.

    Responsibilities:
    - describe engine geometry and mass
    - define propulsion characteristics
    - compute thrust, Isp and mass flow
    - define gimbal orientation
    - reference connected tanks
    """

    G0 = 9.80665
    P0 = 101325.0

    def __init__(
        self,
        name: str,
        mass_dry: float,
        r_cg_local,
        I_cg_local,
        length: float,
        radius: float,

        thrust_asl: float,
        thrust_vac: float,
        Isp_asl: float,
        Isp_vac: float,

        fuel_type: list[str] | tuple[str, str],
        OF: float,
        maxtime: float,

        fuel_tank=None,
        oxidizer_tank=None,

        min_throttle: float = 0.0,
        max_throttle: float = 1.0,
        gimbal_max: float = 0.0,

        stage: int = 0,
        parent=None,
        p_parent_child=None,
        R_parent_child=None,
    ):

        # geometry
        self.length = float(length)
        self.radius = float(radius)

        # propulsion
        self.thrust_asl = float(thrust_asl)
        self.thrust_vac = float(thrust_vac)

        self.Isp_asl = float(Isp_asl)
        self.Isp_vac = float(Isp_vac)

        self.fuel_type = list(fuel_type)
        self.OF = float(OF)
        self.maxtime = float(maxtime)

        # operating limits
        self.min_throttle = float(min_throttle)
        self.max_throttle = float(max_throttle)

        # gimbal
        self.gimbal_max = float(gimbal_max)

        # tank connections
        self.fuel_tank = fuel_tank
        self.oxidizer_tank = oxidizer_tank

        # simple cylindrical envelope
        struct_volume = float(np.pi * self.length * self.radius**2)

        # convert dry mass to equivalent density for Part
        material_rho = mass_dry / struct_volume

        super().__init__(
            name=name,
            material_rho=material_rho,
            volume=struct_volume,
            r_cg_local=np.asarray(r_cg_local, dtype=float),
            I_cg_local=np.asarray(I_cg_local, dtype=float),
            aero=False,
            stage=stage,
            parent=parent,
            p_parent_child=p_parent_child,
            R_parent_child=R_parent_child,
        )

        self.r_cg_local.setflags(write=False)

    # =========================================================
    # Atmosphere helpers
    # =========================================================

    @staticmethod
    def pressure_ratio(p_ambient: float) -> float:
        """
        Returns ambient pressure ratio relative to sea level.
        """
        return np.clip(p_ambient / Engine.P0, 0.0, 1.0)

    # =========================================================
    # Propulsion
    # =========================================================

    def get_isp(self, p_ambient: float) -> float:
        """
        Returns engine Isp at given ambient pressure.
        """
        pr = self.pressure_ratio(p_ambient)

        return self.Isp_vac - pr * (self.Isp_vac - self.Isp_asl)

    def get_max_thrust(self, p_ambient: float) -> float:
        """
        Maximum thrust available at given ambient pressure.
        """
        pr = self.pressure_ratio(p_ambient)

        return self.thrust_vac - pr * (self.thrust_vac - self.thrust_asl)

    def get_thrust(self, p_ambient: float, throttle: float) -> float:
        """
        Thrust produced for a given throttle level.
        """

        throttle = np.clip(throttle, 0.0, 1.0)

        if throttle > 0.0:
            throttle = max(throttle, self.min_throttle)

        throttle = min(throttle, self.max_throttle)

        return throttle * self.get_max_thrust(p_ambient)

    # =========================================================
    # Mass flow
    # =========================================================

    def get_mass_flow(self, p_ambient: float, throttle: float) -> float:
        """
        Total propellant mass flow [kg/s]
        """

        thrust = self.get_thrust(p_ambient, throttle)

        isp = self.get_isp(p_ambient)

        return thrust / (isp * self.G0)

    def get_propellant_flows(self, p_ambient: float, throttle: float):
        """
        Returns fuel and oxidizer mass flow.
        """

        mdot = self.get_mass_flow(p_ambient, throttle)

        mdot_fuel = mdot / (1 + self.OF)

        mdot_ox = mdot * self.OF / (1 + self.OF)

        return mdot_fuel, mdot_ox

    # =========================================================
    # Gimbal
    # =========================================================

    def get_gimbal_rotation(self, pitch: float, yaw: float):
        """
        Returns rotation matrix for gimbal angles.
        """

        pitch = np.clip(pitch, -self.gimbal_max, self.gimbal_max)
        yaw = np.clip(yaw, -self.gimbal_max, self.gimbal_max)

        cx = np.cos(pitch)
        sx = np.sin(pitch)

        cy = np.cos(yaw)
        sy = np.sin(yaw)

        Rx = np.array([
            [1, 0,  0],
            [0, cx, -sx],
            [0, sx, cx]
        ])

        Ry = np.array([
            [cy,     0,  sy],
            [0,      1,  0],
            [-sy,    0,  cy]
        ])

        return Ry @ Rx

    def get_thrust_vector_local(self, p_ambient: float, throttle: float, pitch=0.0, yaw=0.0):
        """
        Returns thrust vector in engine local frame.
        """

        thrust = self.get_thrust(p_ambient, throttle)

        Rg = self.get_gimbal_rotation(pitch, yaw)

        axis = np.array([0.0, 0.0, 1.0])

        return thrust * (Rg @ axis)

    # =========================================================
    # Mass
    # =========================================================

    def get_mass(self):

        return float(self.mass_dry)

    # =========================================================
    # Representation
    # =========================================================

    def __repr__(self):

        return (
            f"Engine(name={self.name}, "
            f"thrust_vac={self.thrust_vac}, "
            f"Isp_vac={self.Isp_vac}, "
            f"OF={self.OF})"
        )