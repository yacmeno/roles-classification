#!/usr/bin/python3

"""
Script to retrieve the 100 latest captain's draft matches (IDs) from specific players
"""

import sys
import requests

# api request for specific player
# use from terminal as "./get_player_matches player_id" (see get_matches_files.sh)
player_id = sys.argv[1]
url = 'https://api.opendota.com/api/players/' + str(player_id) + '/matches'

def get_match_ids(player_id=player_id):
    #game_mode: Captain's draft, limit: 100 games
    request = requests.get(url, params={'game_mode':2, 'limit':100}) 

    matches_file = open(str(player_id) + '_matches.txt', 'w')
    for match in request.json():
        matches_file.write(str(match['match_id']) + '\n') # written as 'integer\n'

if __name__ == '__main__':
    get_match_ids()