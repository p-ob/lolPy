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
from riot.Player import Player


class Participant(object):
    def __init__(self, json_data: dict, player: dict):
        self.champion_id = json_data.get("championId", None)
        self.masteries = json_data.get("masteries", None)
        self.participant_id = json_data.get("participantId", None)
        self.runes = json_data.get("runes", None)
        self.spell_id1 = json_data.get("spell1Id", None)
        self.spell_id2 = json_data.get("spell2Id", None)
        self.stats = json_data.get("stats", None)
        self.team_id = json_data.get("teamId", None)
        self.timeline = json_data.get("timeline", None)
        self.player = Player(player.get("player", player))

    def __repr__(self):
        return self.player.name + ' - ' + str(vars(self))
