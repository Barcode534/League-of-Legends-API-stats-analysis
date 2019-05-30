# League-of-Legends-API-stats-analysis
Analysis of combinations of champions to maximise chances of winning

The goal of the project is to collect match data of the highest rated players in the game, see which champions they pick, find mean winrate of each champion, then see how these winrates change when partnered with certain champions. The result should be that when you are choosing your champion in the pre-game lobby, you can see some of your teams picks, some of the opponents picks, and from this information you can make a better decision than just random.

The end product does work, and as a recreational player, I have benefited from this big data analysis.

Product demonstration: https://www.youtube.com/watch?v=Imy_IyydMMY&t=7s

How to run the scripts:

Step 1. Use collectIDs script to get the IDs of the highest rated players in the game.

Step 2. Use SummID to AccID to convert the Summoner ID to Account ID necessary to collect further data.

Step 3. Use AccID append match list.py to collect the Match IDs of all the games played by the highest rated players

Step 4. Use GameIDs to non-dup gameIDs.py to remove all duplicated game IDs. Since all of these players play at the same level, they are often in the same games as each other. Each game must only be counted once. 

Step 5. Use gameIDs to match data.py to end up with the final data which is [Team 1 Champions][Team 2 Champions][Team 1 win/loss][Team 2 win/loss]



Step 6. convert-functions.py and champID-to-name are used to convert the numeric ID of each champion to their Name, and back.

Step 7. Use Data-analysis.py while entering a champion name that will be on your team to create a new winrate file. The winrate files contains the dictionaries of data that you can check for statistics.

Step 8. Use best-champs.py to find the highest winrate champions when you know you will have 'X' champion on your team.

Notes for future: 1. Set up config file with API key and import it each time from there. 2. Do an enemy team has 'Y', what do I pick solution.
