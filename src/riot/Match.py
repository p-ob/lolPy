from src.riot.Participant import Participant

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
        try:
            self.timeline = json_data["timeline"]
        except KeyError:
            self.timeline = None
        self.participant_ids = json_data["participantIdentities"]
        self.participants = [
            Participant(self.__match_participant_id(participant_id["participantId"], json_data["participants"]),
                        participant_id) for participant_id in self.participant_ids]

        self.match_details = json_data

    @staticmethod
    def __match_participant_id(participant_id, participants):
        for participant in participants:
            if participant["participantId"] == participant_id:
                return participant
        return None

