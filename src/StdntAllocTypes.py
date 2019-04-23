## @file StdntAllocTypes.py
#  @author Artemiy Kokhanov
#  @brief GenT, DeptT, and SInfoT types
#  @date 08/02/2018

from SeqADT import *
from enum import Enum
from typing import NamedTuple


## @brief A type for genders
class GenT(Enum):
    male = 1
    female = 2


## @brief A type for departments
class DeptT(Enum):
    civil = 1
    chemical = 2
    electrical = 3
    mechanical = 4
    software = 5
    materials = 6
    engphys = 7


## @brief A type for student info
class SInfoT(NamedTuple):
    fname: str
    lname: str
    gender: GenT
    gpa: float
    choices: SeqADT
    freechoice: bool
