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


class AggregateStats(object):
    def __init__(self, json_data: dict):
        self.average_assists = json_data.get("averageAssists", None)
        self.average_champions_killed = json_data.get("averageChampionsKilled", None)
        self.average_combat_playerScore = json_data.get("averageCombatPlayerScore", None)
        self.average_node_capture = json_data.get("averageNodeCapture", None)
        self.average_node_capture_assist = json_data.get("averageNodeCaptureAssist", None)
        self.average_node_neutralize = json_data.get("averageNodeNeutralize", None)
        self.average_node_neutralize_assist = json_data.get("averageNodeNeutralizeAssist", None)
        self.average_num_deaths = json_data.get("averageNumDeaths", None)
        self.average_objective_player_score = json_data.get("averageObjectivePlayerScore", None)
        self.average_team_objective = json_data.get("averageTeamObjective", None)
        self.average_total_player_score = json_data.get("averageTotalPlayerScore", None)
        self.bot_games_played = json_data.get("botGamesPlayed", None)
        self.killing_spree = json_data.get("killingSpree", None)
        self.max_assists = json_data.get("maxAssists", None)
        self.max_champions_killed = json_data.get("maxChampionsKilled", None)
        self.max_combat_player_score = json_data.get("maxCombatPlayerScore", None)
        self.max_largest_critical_strike = json_data.get("maxLargestCriticalStrike", None)
        self.max_largest_killing_spree = json_data.get("maxLargestKillingSpree", None)
        self.max_node_capture = json_data.get("maxNodeCapture", None)
        self.max_node_capture_assist = json_data.get("maxNodeCaptureAssist", None)
        self.max_node_neutralize = json_data.get("maxNodeNeutralize", None)
        self.max_node_neutralize_assist = json_data.get("maxNodeNeutralizeAssist", None)
        self.max_num_deaths = json_data.get("maxNumDeaths", None)
        self.max_objective_player_score = json_data.get("maxObjectivePlayerScore", None)
        self.max_team_objective = json_data.get("maxTeamObjective", None)
        self.max_time_played = json_data.get("maxTimePlayed", None)
        self.max_time_spent_living = json_data.get("maxTimeSpentLiving", None)
        self.max_total_player_score = json_data.get("maxTotalPlayerScore", None)
        self.most_champion_kills_per_session = json_data.get("mostChampionKillsPerSession", None)
        self.most_spells_cast = json_data.get("mostSpellsCast", None)
        self.normal_games_played = json_data.get("normalGamesPlayed", None)
        self.ranked_premade_games_played = json_data.get("rankedPremadeGamesPlayed", None)
        self.ranked_solo_games_played = json_data.get("rankedSoloGamesPlayed", None)
        self.total_assists = json_data.get("totalAssists", None)
        self.total_champion_kills = json_data.get("totalChampionKills", None)
        self.total_damage_dealt = json_data.get("totalDamageDealt", None)
        self.total_damage_taken = json_data.get("totalDamageTaken", None)
        self.total_deaths_per_session = json_data.get("totalDeathsPerSession", None)
        self.total_double_kills = json_data.get("totalDoubleKills", None)
        self.total_first_blood = json_data.get("totalFirstBlood", None)
        self.total_gold_earned = json_data.get("totalGoldEarned", None)
        self.total_heal = json_data.get("totalHeal", None)
        self.total_magic_damage_dealt = json_data.get("totalMagicDamageDealt", None)
        self.total_mininion_kills = json_data.get("totalMininionKills", None)
        self.total_neutral_minions_killed = json_data.get("totalNeutralMinionsKilled", None)
        self.total_node_capture = json_data.get("totalNodeCapture", None)
        self.total_node_neutralize = json_data.get("totalNodeNeutralize", None)
        self.total_penta_kills = json_data.get("totalPentaKills", None)
        self.total_physical_damage_dealt = json_data.get("totalPhysicalDamageDealt", None)
        self.total_quadra_kills = json_data.get("totalQuadraKills", None)
        self.total_sessions_lost = json_data.get("totalSessionsLost", None)
        self.total_sessions_played = json_data.get("totalSessionsPlayed", None)
        self.total_sessions_won = json_data.get("totalSessionsWon", None)
        self.total_triple_kills = json_data.get("totalTripleKills", None)
        self.total_turrets_killed = json_data.get("totalTurretsKilled", None)
        self.total_unreal_kills = json_data.get("totalUnrealKills", None)