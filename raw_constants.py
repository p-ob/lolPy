__author__ = 'Patrick O\'Brien'
''' COPYRIGHT 2014
    This file is part of lolPy.

    lolPy is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    lolPy is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with lolPy.  If not, see <http://www.gnu.org/licenses/>.
'''
from enum import Enum


class SummonersRiftBounds(Enum):
    min_x = -650
    min_y = -83
    max_x = 14076
    max_y = 14522


class MapNames(Enum):
    SummonersRift = 1
    SummonersRiftAutumn = 2
    ProvingGrounds = 3
    TwistedTreelineOld = 4
    CrystalScar = 8
    TwistedTreeline = 10
    HowlingAbyss = 12


class Mastery(Enum):
    Invalid = 0


class Rune(Enum):
    Invalid = 0


class Item(Enum):
    Invalid = 0


class Champion(Enum):
    Invalid = 0
