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


class Player(object):
    def __init__(self, json_data: dict):
        if not isinstance(json_data, dict):
            raise TypeError("Input must be a dictionary")
        self.name = json_data.get("name", json_data.get("summonerName", None))
        self.id = json_data.get("id", json_data.get("summonerId", None))

    def __repr__(self):
        return 'Name: {0}; Id: {1}'.format(self.name, self.id)
