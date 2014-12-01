To use lolPy, you must first create an instance of `RiotApiClient`, which requires an API key from [RiotGames](https://developer.riotgames.com/) and which region you'd like to begin work in. This region can change at any time by using `change_region`, which resets all region-specific data to their default values (e.g. summoner ids are region specific, so the summoner id stored is reset to -1).

Example:  
`1. list_of_summoner_names = ['Dyrus', 'hi im gosu']`  
`2. key = 'this-is-an-example'`  
`3. client = RiotApiClient(key, Region.na)  # Region.na evaluates to 'na'`  
`4. summoner = client.search(list_of_summoner_names)  # search returns the first summoner in the list of search results; these are stored in RiotApiClient.summoners`  
`5. print(summoner.name)`  
`6.    >> 'Dyrus'`  
`7. summoner = client.next()`  
`8. print(summoner.name)`  
`9.    >> 'hi im gosu'`  
`10. match_history = client.ranked_match_history()  # returns last 10 ranked games for hi im gosu in a list`  
`11. # what are the attributes stored in match_history[0]??`  
`12. print(match_history[0].get_data_members())`  
`13.    >> ['matchType', 'matchVersion', 'region', 'matchId', 'season', 'matchDuration', 'platformId', 'mapId', 'participants', 'matchCreation', 'queueType', 'participantIdentities', 'matchMode']`  
`14. client.next()  # client will loop back to the beginning of the list once the end has been hit`  
`15. print(client.current_summoner.name)`  
`16.   >> 'Dyrus'`  



For more on how to use lolPy, see the Wiki page for [`RiotApiClient`](https://github.com/p-ob/lolPy/wiki/RiotApiClient) and the other Wiki pages.

lolPy requires [restPy](https://github.com/p-ob/restPy/) to function in the new version. restPy requires [xmltodict](https://github.com/martinblech/xmltodict).


lolPy isn't endorsed by Riot Games and doesn't reflect the views or opinions of Riot Games or anyone officially involved
in producing or managing League of Legends. League of Legends and Riot Games are trademarks or registered trademarks of
Riot Games, Inc. League of Legends © Riot Games, Inc.
