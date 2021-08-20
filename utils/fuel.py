from typing import Dict


class Fuel:
    def __init__(
        self,
        name: str,
        kC: float,
        kH: float,
        kO: float,
        kN: float,
        kS: float,
        kM: float,
        kAsh: float
    ) -> None:
        self.name = name.lower()
        self.kC, self.kH, self.kO, self.kN, self.kS, self.kM, self.kAsh = kC, kH, kO, kN, kS, kM, kAsh
