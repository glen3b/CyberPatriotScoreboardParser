# CyberPatriot Scoreboard Parsing

Quick and dirty Python scripts to return CyberPatriot scoreboard data in an AWK-friendly format. Everything is separated by tabs.

## Documentation

`scoreparser.py`: returns individual image scores and times for all open platinum teams, ordered by total score of team

`scoreparser.py -a`: returns total scores and times for all open platinum teams, ordered

`scoreovertime.py <teamID>`: returns a list of times and image scores (one image score per column in the same order as the CP scoreboard) for the given team
