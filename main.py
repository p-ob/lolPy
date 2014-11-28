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
from RiotApiClient import RiotApiClient
from Region import Region


def main():
    with open('key.txt') as f:
        key = f.read()
    c = RiotApiClient(key, Region.na)
    p = c.search(False, 'Dyrus', 'DoubleLift', 'hi im gosu')
    p = c.search(False, 'drunk7irishman')
    m = c.league_data()
    return m


if __name__ == '__main__':
    main()