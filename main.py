# TODO: Support more Minigames

import time
import random
import sys
from pypresence import Presence
import requests
from mojang import MojangAPI
from configparser import ConfigParser
import os
import atexit

@atexit.register
def NoClose():
    input()

def getInfo(call):
    r = requests.get(call)
    return r.json()

version = '0.3'

clear = lambda: os.system('cls')

config = ConfigParser()
res = config.read('config.ini')

clear()
logo = f'''
-----------Version  {version} -----------
 _   _                ____   ____   ____  
| | | | _   _        |  _ \ |  _ \ |  _ \ 
| |_| || | | | _____ | | | || |_) || |_) |
|  _  || |_| ||_____|| |_| ||  _ < |  __/ 
|_| |_| \__, |       |____/ |_| \_\|_|    
        |___/                             
---------Made by TubYoub---------
-------Please Report Bugs--------
'''
print(logo)

if config.get('main','check_for_updates') == 'True':
    update = getInfo(f"https://api.github.com/repos/TubYoub/HyDRP/releases/latest")
    new_release = update['name']

    if new_release != "Version "+ version:
        print('There is a Update from HyDRP available')
    else:
        print('There is no new Update')


FirstTime = config.get('main', 'firsttime')

if FirstTime == 'False':
    name = str(input('Please enter your Minecraft username: '))
    print('Tipp:You can find your API key if you type "/api new" in the Hypixel Chat')
    APIKey = str(input('Please Type your API Key here: '))
    uuid = MojangAPI.get_uuid(name)

    status = getInfo(f'https://api.hypixel.net/status?key={APIKey}&uuid={uuid}')
    success = (status['success'])

    if success == True:
        print("Your API Key and Name is Valid")
        config.set('main', 'FirstTime', 'True')
        config.set('main', 'uuid', uuid)
        config.set('main', 'name', name)
        config.set('main', 'APIKey', APIKey)
        with open('config.ini', 'w') as f:
            config.write(f)

else:
    #print('You already gave your API key and your Minecraft username')
    APIKey = str(config.get('main','apikey'))
    uuid = str(config.get('main','uuid'))
    name = str(config.get('main','name'))


rpc_connected = False
APPLICATION_ID = '878328867968917534'
old_APPLICATION_ID = APPLICATION_ID
time_record = 0

url_1 = f'https://api.hypixel.net/status?key={APIKey}&uuid={uuid}'
url_2 = f'https://api.hypixel.net/recentGames?key={APIKey}&uuid={uuid}'
url_3 = f'https://api.hypixel.net/player?key={APIKey}&uuid={uuid}'


status = getInfo(url_1)
success = (status['success'])

if success == True:
    print("Your API key and your Minecraft username are still Valid.")
else:
    print('Please Update your API key or ur Username in the config.ini')
    input('Press ENTER to exit...')
    sys.exit()
time.sleep(5)

clear()
print(logo)

while True:
    clear()
    print(logo)

    if time_record == 120:
        print('You are not on the Hypixel Server')
        print('Press ENTER to exit...')
        sys.exit()
    if time_record != 120 or online != True:
        status = getInfo(url_1)
        online = (status['session']['online'])
        time_record = time_record + 5
        time.sleep(5)
    if online == True:
        time_record = 0
        data2 = getInfo(url_2)

        if data2['games'][0]['gameType'] == []:
            print('No Recent Game found ')

        data = getInfo(url_3)
        gameType = data2['games'][0]['gameType']
        try:
            data2['games'][0]['ended']
            starttime = 32514888426
            lobby = ' lobby'
        except:
            starttime = data2['games'][0]['date']
            drptime = True
            lobby = ''

        if gameType == 'BEDWARS':
            old_APPLICATION_ID = APPLICATION_ID
            APPLICATION_ID = '876505801047556097'

            if config.get('BedWars', 'PlayedGames') == 'True':
                stat1 = 'Played Games: ' + str(data['player']['stats']['Bedwars']['games_played_bedwars_1'])
            else:
                stat1 = 'mc.hypixel.net'

            if config.get('BedWars', 'Coins') == 'True':
                stat2 = 'Coins: ' + str(data['player']['stats']['Bedwars']['coins'])
            else:
                stat2 = 'mc.hypixel.net'

            if config.get('BedWars', 'RecourcesCollected') == 'True':
                stat3 = 'Recources collected: ' + str(data['player']['stats']['Bedwars']['resources_collected_bedwars'])#
            else:
                stat3: 'mc.hypixel.net'

            if config.get('BedWars', 'PurchasedItems') == 'True':
                stat4 = 'Purchased Items: ' + str(data['player']['stats']['Bedwars']['_items_purchased_bedwars'])
            else:
                stat4 = 'mc.hypixel.net'

            if config.get('BedWars', 'Kills') == 'True':
                stat5 = 'Kills: ' + str(data['player']['stats']['Bedwars']['kills_bedwars'])
            else:
                stat5 = 'mc.hypixel.net'

            if config.get('BedWars', 'FinalKills') == 'True':
                stat6 = 'Final Kills: ' + str(data['player']['stats']['Bedwars']['final_kills_bedwars'])
            else:
                stat6 = 'mc.hypixel.net'

            if config.get('BedWars', 'Wins') == 'True':
                stat7 = 'Wins: ' + str(data['player']['stats']['Bedwars']['wins_bedwars'])
            else:
                stat7 = 'mc.hypixel.net'

            if config.get('BedWars', 'Coins') == 'True':
                stat8 = 'Coins:' + str(data['player']['stats']['Bedwars']['coins'])
            else:
                stat8 = 'mc.hypixel.net'

            currentGame = 'Bedwars' + lobby

        elif gameType == 'SKYWARS':
            old_APPLICATION_ID = APPLICATION_ID
            APPLICATION_ID = '878328645813407837'

            if config.get('SkyWars', 'PlayedGames') == 'True':
                stat1 = 'Played Games: ' + str(data['player']['stats']['SkyWars']['games_played_skywars'])
            else:
                stat1 = 'mc.hypixel.net'

            if config.get('SkyWars', 'Kills') == 'True':
                stat2 = 'Kills: ' + str(data['player']['stats']['SkyWars']['kills'])
            else:
                stat2 = 'mc.hypixel.net'

            if config.get('SkyWars', 'Coins') == 'True':
                stat3 = 'Coins: ' + str(data['player']['stats']['SkyWars']['coins'])
            else:
                stat3 = 'mc.hypixel.net'

            if config.get('SkyWars', 'Tokens') == 'True':
                stat4 = 'Tokens: ' + str(data['player']['stats']['SkyWars']['cosmetic_tokens'])
            else:
                stat4 = 'mc.hypixel.net'

            if config.get('SkyWars', 'Wins') == 'True':
                stat5 = 'Wins: ' + str(data['player']['stats']['SkyWars']['wins'])
            else:
                stat5 = 'mc.hypixel.net'

            if config.get('SkyWars', 'PlayedGames') == 'True':
                stat6 = 'Played Games: ' + str(data['player']['stats']['SkyWars']['games_played_skywars'])
            else:
                stat6 = 'mc.hypixel.net'

            if config.get('SkyWars', 'Kills') == 'True':
                stat7 = 'Kills: ' + str(data['player']['stats']['SkyWars']['kills'])
            else:
                stat7 = 'mc.hypixel.net'

            if config.get('SkyWars', 'Coins') == 'True':
                stat8 = 'Coins: ' + str(data['player']['stats']['SkyWars']['coins'])
            else:
                stat8 = 'mc.hypixel.net'

            currentGame = 'Skywars' + lobby

        elif gameType == 'MURDERMYSTERY':
            old_APPLICATION_ID = APPLICATION_ID
            APPLICATION_ID = '878328439520759828'

            if config.get('MurderMystery', 'PlayedGames') == 'True':
                stat1 = 'Played Games: ' + str(data['player']['stats']['MurderMystery']['games'])
            else:
                stat1 = 'mc.hypixel.net'

            if config.get('MurderMystery', 'Kills') == 'True':
                stat2 = 'Kills: ' + str(data['player']['stats']['MurderMystery']['kills'])
            else:
                stat2 = 'mc.hypixel.net'

            if config.get('MurderMystery', 'Coins') == 'True':
                stat3 = 'Coins: ' + str(data['player']['stats']['MurderMystery']['coins'])
            else:
                stat3 = 'mc.hypixel.net'

            if config.get('MurderMystery', 'Wins') == 'True':
                stat4 = 'Wins: ' + str(data['player']['stats']['MurderMystery']['wins'])
            else:
                stat4 = 'mc.hypixel.net'

            if config.get('MurderMystery', 'MurderChance') == 'True':
                stat5 = 'Murder chance: ' + str(data['player']['stats']['MurderMystery']['murderer_chance'])
            else:
                stat5 = 'mc.hypixel.net'

            if config.get('MurderMystery', 'PlayedGames') == 'True':
                stat6 = 'Played Games: ' + str(data['player']['stats']['MurderMystery']['games'])
            else:
                stat6 = 'mc.hypixel.net'

            if config.get('MurderMystery', 'Kills') == 'True':
                stat7 = 'Kills: ' + str(data['player']['stats']['MurderMystery']['kills'])
            else:
                stat7 = 'mc.hypixel.net'

            if config.get('MurderMystery', 'Coins') == 'True':
                stat8 = 'Coins: ' + str(data['player']['stats']['MurderMystery']['coins'])
            else:
                'mc.hypixel.net'
            currentGame = 'Murder Mystery' + lobby

        elif gameType == 'GINGERBREAD':
            old_APPLICATION_ID = APPLICATION_ID
            APPLICATION_ID = '878328439520759828'
            stat1 = "normal"
            stat2 = "normal"
            stat3 = "normal"
            stat4 = "normal"
            stat5 = "normal"
            stat6 = "normal"
            stat7 = "normal"
            stat8 = "normal"
            currentGame = 'Turbo Kart Racer' + lobby

        elif gameType == 'DUELS':
            old_APPLICATION_ID = APPLICATION_ID
            APPLICATION_ID = '884049580642160652'

            if config.get('Duels', 'PlayedGames') == 'True':
                stat1 = 'Played Games: ' + str(data['player']['stats']['Duels']['games_played_duels'])
            else:
                stat1 = 'mc.hypixel.net'

            if config.get('Duels', 'BowShots') == 'True':
                stat2 = 'Bow shots: ' + str(data['player']['stats']['Duels']['bow_shots'])
            else:
                stat2 = 'mc.hypixel.net'

            if config.get('Duels', 'DamagDealt') == 'True':
                stat3 = 'Damage dealt: ' + str(data['player']['stats']['Duels']['damage_dealt'])
            else:
                stat3 = 'mc.hypixel.net'

            if config.get('Duels', 'Coins') == 'True':
                stat4 = 'Coins: ' + str(data['player']['stats']['Duels']['coins'])
            else:
                stat4 = 'mc.hypixel.net'

            if config.get('Duels', 'Wins') == 'True':
                stat5 = 'Wins: ' + str(data['player']['stats']['Duels']['wins'])
            else:
                stat5 = 'mc.hypixel.net'

            if config.get('Duels', 'BlocksPlaced') == 'True':
                stat6 = 'Blocks placed: ' + str(data['player']['stats']['Duels']['blocks_placed'])
            else:
                stat6 = 'mc.hypixel.net'

            if config.get('Duels', 'PlayedGames') == 'True':
                stat7 = 'Played Games: ' + str(data['player']['stats']['Duels']['games_played_duels'])
            else:
                stat7 = 'mc.hypixel.net'

            if config.get('Duels', 'BowShots') == 'True':
                stat8 = 'Bow shots: ' + str(data['player']['stats']['Duels']['bow_shots'])
            else:
                stat8 = 'mc.hypixel.net'
            currentGame = 'Duels' + lobby

        elif gameType == 'PIT':
            old_APPLICATION_ID = APPLICATION_ID
            APPLICATION_ID = '884052292591034378'

            if config.get('Pit', 'BowShots') == 'True':
                stat1 = 'Bow shots: ' + str(data['player']['stats']['Pit']['pit_stats_ptl']['arrows_fired'])
            else:
                stat1 = 'mc.hypixel.net'

            if config.get('Pit', 'Kills') == 'True':
                stat2 = 'Kills: ' + str(data['player']['stats']['Pit']['pit_stats_ptl']['kills'])
            else:
                stat2 = 'mc.hypixel.net'

            if config.get('Pit', 'Gold') == 'True':
                stat3 = 'Gold: ' + str(data['player']['stats']['Pit']['pit_stats_ptl']['ingots_cash'])
            else:
                stat3 = 'mc.hypixel.net'

            if config.get('Pit', 'Playtime') == 'True':
                stat4 = 'Playtime: ' + str(data['player']['stats']['Pit']['pit_stats_ptl']['playtime_minutes']) + ' minutes'
            else:
                stat4 = 'mc.hypixel.net'

            if config.get('Pit', 'BowShots') == 'True':
                stat5 = 'Bow shots: ' + str(data['player']['stats']['Pit']['pit_stats_ptl']['arrows_fired'])
            else:
                stat5 = 'mc.hypixel.net'

            if config.get('Pit', 'Kills') == 'True':
                stat6 = 'Kills: ' + str(data['player']['stats']['Pit']['pit_stats_ptl']['kills'])
            else:
                stat6 = 'mc.hypixel.net'

            if config.get('Pit', 'Gold') == 'True':
                stat7 = 'Gold: ' + str(data['player']['stats']['Pit']['pit_stats_ptl']['ingots_cash'])
            else:
                stat7 = 'mc.hypixel.net'

            if config.get('Pit', 'Playtime') == 'True':
                stat8 = 'Playtime: ' + str(data['player']['stats']['Pit']['pit_stats_ptl']['playtime_minutes']) + ' minutes'
            else:
                stat8 = 'mc.hypixel.net'

            currentGame = 'The Pit'

        else:
            APPLICATION_ID = '878328867968917534'
            old_APPLICATION_ID = APPLICATION_ID
            stat1 = 'mc.hypixel.net'
            stat2 = 'mc.hypixel.net'
            stat3 = 'mc.hypixel.net'
            stat4 = 'mc.hypixel.net'
            stat5 = 'mc.hypixel.net'
            stat6 = 'mc.hypixel.net'
            stat7 = 'mc.hypixel.net'
            stat8 = 'mc.hypixel.net'
            currentGame = 'playing on:'

        status = [
            stat1,
            stat2,
            stat3,
            stat4,
            stat5,
            stat6,
            stat7,
            stat8
        ]

        if not rpc_connected:
            client_id = APPLICATION_ID
            RPC = Presence(client_id)
            RPC.connect()
            rpc_connected = True

        if APPLICATION_ID != old_APPLICATION_ID and rpc_connected == True:
            RPC.close()
            client_id = APPLICATION_ID
            RPC = Presence(client_id)
            RPC.connect()

        state = random.choice(status)

        print(f'|----------------------|')
        print(f'| Skywars              |')
        print(f'| Skywars {lobby}')
        print(f'| {state}')
        print(f'|----------------------|')

        if config.get('main', 'button') == 'True':
            RPC.update(details=currentGame, state=state, large_image='large', large_text='Gamemode',small_image='small', small_text='mc.hypixel.net', start=starttime,buttons=[{"label": "/f add " + name, "url": "https://plancke.io/hypixel/player/stats/" + uuid}])

        elif config.get('main', 'button') == 'False':
            RPC.update(details=currentGame, state=state, large_image='large', large_text='Gamemode',small_image='small', small_text='mc.hypixel.net', start=starttime)

        else:
            RPC.update(details=currentGame, state=state, large_image='large', large_text='Gamemode',small_image='small', small_text='mc.hypixel.net', start=starttime,buttons=[{"label": "/f add " + name, "url": "https://plancke.io/hypixel/player/stats/" + uuid}])
        time.sleep(15)