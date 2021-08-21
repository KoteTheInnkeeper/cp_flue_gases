import logging
log = logging.getLogger("cp_flue_gases.fuel")

from typing import Dict
from data.db_manager import Database
from utils.errors import *


class Fuel:
    def __init__(self, name: str, db: Database)-> None:
        """Initializes the object.
        :param name: the fuel's name.
        :param db: a Database object from where to extract the information."""
        log.debug(f"Initializing a Fuel object. Searching for an entry like {name.title()} in the database.")
        try:
            self.name = name.lower()
            from_db = db.get_fuel_composition(name.lower())
            self.kC, self.kH, self.kO, self.kN, self.kS, self.kM, self.kAsh = from_db
            if not self.has_integrity():
                raise FuelIntegrityError("The given fuel's composition doesn't add up to a 100%.")
        except Exception:
            log.critical("An exception was raised")
            raise
        else:
            log.debug("Fuel object correctly initialized. Calculating their minimum air and gas.")
            # Calculating the minimum amount of air per kg of fuel.
            self.min_air = round((2.9978 * self.kH + 0.3747 * (self.kS - self.kO) + self.kC) * 11.445, 4)
            # Calculating the minimum total gas after burning this fuel.
            self.min_gas_total = round((2.9978 * self.kH + 0.3747 * (self.kS - self.kO) + self.kC) * 11.445, 4) + (1 - self.kAsh)

    def has_integrity(self) -> bool:
        """Checks if the given composition adds up to a 100% (1)."""
        total_comp = self.kC + self.kH + self.kO + self.kN + self.kS + self.kM + self.kAsh
        if total_comp != 1:
            log.critical(f"This {self.name.title()} fuel has a composition that doesn't add up to 100%.")
            return False
        log.debug(f"This {self.name.title()} fuel has integrity")
        return True
    
    def __repr__(self) -> str:
        return f"""<<FUEL OBJECT NAMED {self.name.upper()}>>"""
    
    def required_air(self, n: float) -> float:
        """Returns the required air given a dilution factor n.
        :param n: dilution factor, a float that expresses 'how many times the minimum air' is being used."""
        return self.min_air * n
    
    def total_flue_gas(self, n: float) -> float:
        """Return the total flue gas for this fuel given a dilution factor n.
        :param n: dilution factor, a float that expresses 'how many times the minimum air' is being used."""
        return self.required_air(n) + (1 - self.kAsh)    



        
        
        


