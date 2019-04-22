# League-of-Legends-API-stats-analysis
Analysis of combinations of champions to maximise chances of winning

Step 1. Use collectIDs script to get the IDs of the highest rated players in the game.

Step 2. Use SummID to AccID to convert the Summoner ID to Account ID necessary to collect further data.

Step 3. Use AccID append match list.py to collect the Match IDs of all the games played by the highest rated players

Step 4. Use GameIDs to non-dup gameIDs.py to remove all duplicated game IDs. Since all of these players play at the same level, they are often in the same games as each other. Each game must only be counted once. 

Step 5. Use gameIDs to match data.py to end up with the final data which is [Team 1 Champions][Team 2 Champions][Team 1 win/loss][Team 2 win/loss]



Step 6. TO DO - Currently getting rate limited with step 5. 2% complete after ~30 mins on 22/04/2019. Once this is complete, the analysis of which Champions are statistically better/worse with each champion can be conducted.
