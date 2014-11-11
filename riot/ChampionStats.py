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
from lolPy.riot.AggregateStats import AggregateStats


class ChampionStats(object):
    def __init__(self, json_data: dict):
        self.id = json_data.get("id", None)
        self._name = None
        stats = json_data.get("stats", {})
        self.stats = AggregateStats(stats)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def __repr__(self):
        return str(self._name)