**lolPy was originally made to be more OOP friendly. I treated it like my C# equivalent, and that was both fun and a learning experience. However, that was not very Pythonic, and I've since created a new API client for my own personal project. I've decided to branch the old version (v1.0) which had the dependency on restPy and update this project with the new, more general purpose client.**

To use lolPy, you must first create an instance of `riot_client.Client`, which requires an API key from [RiotGames](https://developer.riotgames.com/). 

lolPy 2.0 is written with Python 3.5 and requires [requests](http://docs.python-requests.org/en/latest/). I've commented out some of the code that is used by my project to demonstrate how I've decided to handle errors from Riot's API.

lolPy 1.0 still exists as a branch for those who'd like to use it. It is no longer supported by me though.

**The wiki is still WIP for this new version.**

=====

lolPy isn't endorsed by Riot Games and doesn't reflect the views or opinions of Riot Games or anyone officially involved
in producing or managing League of Legends. League of Legends and Riot Games are trademarks or registered trademarks of
Riot Games, Inc. League of Legends © Riot Games, Inc.
