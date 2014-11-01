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
from riot import Player


class Participant(object):
    def __init__(self, json_data: dict, player: dict):
        self.champion_id = json_data["championId"]
        self.masteries = json_data.get("masteries", None)
        self.participant_id = json_data["participantId"]
        self.runes = json_data.get("runes", None)
        self.spell_id1 = json_data["spell1Id"]
        self.spell_id2 = json_data["spell2Id"]
        self.stats = json_data["stats"]
        self.team_id = json_data["teamId"]
        self.timeline = json_data.get("timeline", None)
        self.player = Player(player.get("player", player))

    def __repr__(self):
        try:
            return '{0} - {1}'.format(self.participant_id, self.player) if not list(self.player) == [
                "participantId"] else str(self.participant_id)
        except TypeError:
            return '{0} - {1}'.format(self.player.id, self.player.name)
