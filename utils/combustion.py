from utils.fuel import Fuel
from math import log as loga
from math import exp


class SingleTCombustion:
    def __init__(self, fuel: Fuel, n: float, T: float) -> None:
        """A class to handle single temperatures combustion.
        :param n: dilution factor
        :param T: temperature in K"""
        pass
    

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

