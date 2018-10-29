#!/usr/bin/env bash

# use get_player_matches.py to save files in given folders

support_players="82262664 86727555 94155156 101695162 87278757 101356886 25907144 89117038 26771994 134556694"
core_players="86745912 105248644 132851371 106573901 72312627 111620041 92423451 87276347 34505203 41231571"

cd ./support_matches
for support_player in $support_players
do
    python3 /home/yacine/Desktop/code/opendota/data/get_player_matches.py $support_player
done

cd ../core_matches
for core_player in $core_players
do
    python3 /home/yacine/Desktop/code/opendota/data/get_player_matches.py $core_player
done
