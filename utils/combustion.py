import logging
log = logging.getLogger("cp_flue_gases.combustion")

from utils.fuel import Fuel
from math import log as loga
from math import exp
from utils.errors import *


class SingleTCombustion:
    def __init__(self, fuel: Fuel, n: float, T: float) -> None:
        """A class to handle single temperatures combustion.
        :param n: dilution factor
        :param T: temperature in K"""
        try:
            if not isinstance(fuel, Fuel):
                raise InvalidFuel("The provided fuel isn't a Fuel object.")
            self.fuel = fuel
            self.n = float(n)
            self.T = float(T)
        except:
            log.critical("An exception was raised.")
            raise
        else:
            log.debug("SingleTCombustion object succcessfully instanciated. Calculating mayor coefficients.")
        
    

    # Minor coefficients methods
    def b_m(self) -> float:
        """Returns the mass ratio of N2 to total flue gas."""
        m_N = 0.767 * self.fuel.min_air + self.fuel.kN
        m_tot_flue_gas = self.fuel.total_flue_gas(self.n)
        return m_N / m_tot_flue_gas
    
    def c_m(self) -> float:
        """Returns the mass ratio of H2O to total flue gas."""
        m_H = 8.938 * self.fuel.kH + self.fuel.kM
        m_tot_flue_gas = self.fuel.total_flue_gas(self.n)
        return m_H / m_tot_flue_gas
    
    def d_m(self) -> float:
        """Returns the mass ratio of SO2 to total flue gas."""
        m_S = 2 * self.fuel.kS
        m_tot_flue_gas = self.fuel.total_flue_gas(self.n)
        return m_S / m_tot_flue_gas
    
    def f_m(self) -> float:
        """Returns another coefficient correct the excess air amount."""
        m_air_steo = self.fuel.min_air
        m_flue_gas = self.fuel.total_flue_gas(self.n)
        return (m_air_steo * (self.n - 1)) / m_flue_gas
    

class Approximations:
    @classmethod
    def b_cp(cls, T: float) -> float:
        """Specific heat ratio of CO2 to N2 for the given temperature T.
        :param T: temperature in K"""
        return 0.9094 + 0.000169 * T - 11135 / ((T**2))
    
    @classmethod
    def c_cp(cls, T: float) -> float:
        """Specific heat ratio of CO2 to H2O for the given temperature T.
        :param T: temperature in K"""
        return 0.5657 - 0.00000668 * T - 10465 / ((T**2))
    
    @classmethod
    def d_Cp(cls, T: float) -> float:
        """Specific heat ratio of CO2 to SO2 for the given temperature T.
        :param T: temperature in K"""
        exp()
        return exp(2.679 - 151.16 / T - 0.289 * loga(T, exp(1)))
    
    @classmethod
    def C_pC(cls, T: float) -> float:
        """Specific heat of CO2.
        :param T: temperature in K"""
        return 0.1874 * 1.000061**T * T**0.2665

    @classmethod
    def C_pA(cls, T: float) -> float:
        """A constant to adjust the coefficient fA.
        :param T: temperature in K"""
        return 0.7124 * 1.00011**T * T**0.051