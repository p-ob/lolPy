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
import copy

from riot.Participant import Participant


class Match(object):
    def __init__(self, match_id: int, json_data: dict):
        self.id = match_id
        self.map_id = json_data["mapId"]
        self.match_creation = json_data["matchCreation"]
        self.match_duration = json_data["matchDuration"]
        self.match_mode = json_data["matchMode"]
        self.match_type = json_data["matchType"]
        self.queue_type = json_data["queueType"]
        self.season = json_data["season"]

        self.teams = json_data["teams"]
        self.timeline = json_data.get("timeline", None)
        self.participant_ids = json_data["participantIdentities"]
        participants = copy.deepcopy(json_data["participants"])
        self.participants = [
            Participant(self.__find_participant(participant_id["participantId"], participants),
                        participant_id) for participant_id in self.participant_ids]

        self.match_details = json_data

    @staticmethod
    def __find_participant(participant_id: int, participants: list):
        for participant in participants:
            if participant["participantId"] == participant_id:
                participants.remove(participant)
                return participant
        return None

