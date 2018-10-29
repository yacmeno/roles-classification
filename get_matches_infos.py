#!/usr/bin/python3
"""
script to extract the relevant features from each player's match
"""
import requests
import json
import glob
import os


# opendota api
url = 'https://api.opendota.com/api/matches/' # will append match id

# files paths
supports_files = './support_matches/*.txt'
cores_files = './core_matches/*.txt'

# request
# request = requests.get(url)
# players = request.json()['players']

# feature extraction
# final features: (player total_gold / team total_gold),
#                 (player gold_per_min / team gold_per_min),
#                 (player last_hits / team last_hits),
#                 (player xp_per_min / team xp_per_min)
#                 (observer_uses + sentry_uses)
# team totals have to be calculated manually (not in the api response)

def fetch_match_info(match_id, account_id):
    request = requests.get(url + match_id)
    players = request.json()['players']

    for player in players:
        print(player['total_gold'])
        if player['account_id'] == account_id:
            print(player['account_id'])

# fetch matches iteratively
for filename in glob.glob(supports_files):
    player_id = os.path.basename(filename).split('_')[0] # id is in file name
    with open(filename, 'r') as player_matches:
        line = player_matches.readline()
        while line:
            fetch_match_info(line, player_id) 
        



# for player in players:
#     if player['account_id'] == 25907144:
#         match_file = open('test.txt', 'w')
#         match_file.write((json.dumps(request.json(), indent=2)))
