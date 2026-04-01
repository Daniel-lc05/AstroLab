from vehicle.FDGS.control import *
from .state import State
from enviroment.enviroment import *


class Simulation1D:
    def __init__(self, rocket, dt, t_max):
        self.rocket = rocket
        self.dt = float(dt)
        self.t_max = float(t_max)
        self.history = []
        self.lists = []
        if self.dt <= 0.0:
            raise ValueError("dt must be > 0")

        if self.t_max <= 0.0:
            raise ValueError("t_max must be > 0")

    def step(self, state):
        h = state.h
        v = state.v
        

        rho = get_atm_rho(h)
        g = get_g(h)

        thrust = self.rocket.get_total_thrust_vector1D(h,throttle)
        self.rocket.burn_fuel(throttle,self.dt)
        m = self.rocket.get_total_mass()

        

        drag = -0.5 * rho * self.rocket.Cd * self.rocket.area * v * abs(v)
        weight = m * g

        F = thrust - drag - weight
        a = F / m

        self.lists.append((state.t,v,h,thrust,drag,weight))# for debug
        new_state = State(
            t=state.t + self.dt,
            h=state.h + state.v * self.dt + 0.5 * a * self.dt**2,
            v=state.v + a * self.dt,
        )

        return new_state

    def run(self, initial_state):
        state = initial_state.copy()
        self.history = [state.copy()]

        while state.t < self.t_max and state.h >= 0.0:
            state = self.step(state)
            self.history.append(state.copy())
        
    def get_data(self):
        #Data stored
        # - Time
        # - Vertical Speed
        # - Height
        # - Thrust
        # - Drag
        # - Weight
        header=["Time","Vetical Speed","Height","Thrust","Drag","Weight"]
        return([header]+self.lists)