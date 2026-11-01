"""
Digital Line Coding Schemes: NRZ-L, NRZ-I, Manchester, Differential Manchester, Bipolar AMI.
"""
from typing import List, Tuple

def nrz_l(bits: List[int]) -> List[int]:
    """NRZ-Level: bit 1 = +1V, bit 0 = -1V."""
    return [1 if b == 1 else -1 for b in bits]

def nrz_i(bits: List[int]) -> List[int]:
    """NRZ-Invert: bit 1 causes signal inversion, bit 0 maintains level."""
    signal = []
    curr = 1
    for b in bits:
        if b == 1:
            curr = -curr
        signal.append(curr)
    return signal

def manchester(bits: List[int]) -> List[Tuple[int, int]]:
    """Manchester: bit 0 = high-to-low (+1, -1), bit 1 = low-to-high (-1, +1)."""
    return [(-1, 1) if b == 1 else (1, -1) for b in bits]

def bipolar_ami(bits: List[int]) -> List[int]:
    """Bipolar AMI: bit 0 = 0V, bit 1 alternates between +1V and -1V."""
    signal = []
    last_one = -1
    for b in bits:
        if b == 0:
            signal.append(0)
        else:
            last_one = -last_one
            signal.append(last_one)
    return signal
