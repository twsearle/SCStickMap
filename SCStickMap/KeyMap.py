from bs4 import BeautifulSoup
from dataclasses import dataclass
from enum import Enum

class OperatorMode(Enum):
    """Operator mode """
    SCM = "SCM"
    NAV = "Navigation"
    MINING = "Mining"
    SALVAGE = "Salvage"
    TURRET = "Turret"
    DRIVING = "Driving"
    VEHICLE_MINING = "Vehicle Mining"


@dataclass
class KeyMap:
    """Mapping for a star citizen key bind"""
    name: str
    controller: str
    binding: str
    mode: OperatorMode = OperatorMode.SCM


def parseKeyMap(key_map_file):
    with open(key_map_file, 'r') as f:
        data = f.read()

    bs_data = BeautifulSoup(data, "xml")


