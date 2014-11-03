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

''' This file is simply for testing/development purposes only, as well as
    to provide an example on how to use Client.
'''
import Client


with open("key.txt") as f:
    key = f.read()

client = Client.Client("drunk7irishman", "na", key)

stats = client.recent_match_history()

for stat in stats:
    print(vars(stat))

me = 25886496
