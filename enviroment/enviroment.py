from tools import *

def get_atm_rho(H): # m
    rho_0=1.225 # kg/m^3
    Hs=8500 # m
    return rho_0 * np.exp(-H / Hs) # kg/m^3

def get_atm_p(H):  # m
    P0 = 101325.0  # Pa
    Hs = 8500.0    # m
    return P0 * np.exp(-H / Hs)  # Pa

def get_g(H): # m
    G=6.67*10**(-11) # m^3 / (kg * s^2)
    M = 5.972e24  # kg
    r=6.371e6 # m
    return(G*(M)/(r+H)**2) # N


def get_drag(rho,v,Cd,Area):
    return((1/2)*rho*Cd*Area*v**2)