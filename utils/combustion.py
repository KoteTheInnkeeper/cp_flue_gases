import logging
log = logging.getLogger("cp_flue_gases.combustion")

from utils.fuel import Fuel
from math import log as loga
from math import exp
from utils.errors import *
from typing import Tuple, List


class SingleTCombustion:
    def __init__(self, fuel: Fuel, n: float, T: float) -> None:
        """A class to handle single temperatures combustion.
        :param n: dilution factor
        :param T: temperature in K"""
        log.debug("A SingleTCombustion is being instanciated.")
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
            log.debug("SingleTCombustion object succcessfully instanciated.")

    def get_cp(self) -> float:
        return self.cp_for_T(self.T)

    def cp_for_T(self, T: float) -> float:
        """Gets the specific mean heat for the given temperature within this method."""
        C_pC = Approximations.C_pC(T)
        a_C = self.a_C(T)
        b_N = self.b_N(T)
        c_H = self.c_H(T)
        d_S = self.d_S(T)
        m_tot_steo = self.fuel.min_gas_total
        m_tot_flue_gas = self.fuel.total_flue_gas(self.n)
        f_A = self.f_m() * Approximations.C_pA(T)
        cp = C_pC / (a_C + b_N + c_H + d_S) * m_tot_steo / m_tot_flue_gas + f_A
        return round(cp, 4)
    
    # Mayor coefficients
    def b_N(self, T: float) -> float:
        b_m = self.b_m()
        b_cp = Approximations.b_cp(T)
        return b_m / b_cp

    def c_H(self, T: float) -> float:
        c_m = self.c_m()
        c_cp = Approximations.c_cp(T)
        return c_m / c_cp

    def d_S(self, T: float) -> float:
        d_m = self.d_m()
        d_cp = Approximations.d_Cp(T)
        return d_m / d_cp

    def a_C(self, T: float) -> float:
        return self.a_m()

    # Minor coefficients methods
    def a_m(self) -> float:
        m_C = 3.667 * self.fuel.kC
        m_tot_steo = self.fuel.min_gas_total
        return m_C / m_tot_steo
        

    def b_m(self) -> float:
        """Returns the mass ratio of N2 to total flue gas."""
        m_N = 0.767 * self.fuel.min_air + self.fuel.kN
        m_tot_steo = self.fuel.min_gas_total
        return m_N / m_tot_steo
    
    def c_m(self) -> float:
        """Returns the mass ratio of H2O to total flue gas."""
        m_H = 8.938 * self.fuel.kH + self.fuel.kM
        m_tot_steo = self.fuel.min_gas_total
        return m_H / m_tot_steo
    
    def d_m(self) -> float:
        """Returns the mass ratio of SO2 to total flue gas."""
        m_S = 2 * self.fuel.kS
        m_tot_steo = self.fuel.min_gas_total
        return m_S / m_tot_steo
    
    def f_m(self) -> float:
        """Returns another coefficient correct the excess air amount."""
        m_air_steo = self.fuel.min_air
        m_flue_gas = self.fuel.total_flue_gas(self.n)
        return (m_air_steo * (self.n - 1)) / m_flue_gas
    

class MultipleTCombustion(SingleTCombustion):
    def __init__(self, fuel: Fuel, n: float, T_init: float, T_end: float, step: float):
        try:
            log.debug("A MultipleTCombustion is being instanciated.")
            self.n = float(abs(n))
            if abs(T_init) == abs(T_end):
                raise InvalidTemperatures("Both temperatures are the same.")
            elif abs(T_init) > abs(T_end):
                self.T_init = float(abs(T_end))
                self.T_end = float(abs(T_init) + step)
            else:
                self.T_init = float(abs(T_init))
                self.T_end = float(abs(T_end) + step)
            self.step = float(abs(step))
            if not isinstance(fuel, Fuel):
                raise InvalidFuel("The provided fuel isn't a Fuel object.")
            self.fuel = fuel
        except ValueError:
            log.critical("An invalid number was entered.")
            raise InvalidNumbers("Calculations can't be performed if the temperatures, dilution factor and step aren't numbers.")
        else:
            log.debug("The MultipleTCombustion object has been instanciated successfully.")

    def get_cp(self) -> List[Tuple[float]]:
        T_range = range(int(self.T_init), int(self.T_end))
        cp_list = []
        for T in T_range:
            cp_list.append((T, self.cp_for_T(T)))
        return cp_list




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