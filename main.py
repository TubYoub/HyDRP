# TODO: Support more Minigames
# TODO: Disable stats in config.ini
# TODO: Better display of the stats in the console

import time
import random
import sys
from pypresence import Presence
import requests
from mojang import MojangAPI
from configparser import ConfigParser
from art import *
import os
import atexit

@atexit.register
def NoClose():
    input()

version = '0.2.1'

def getInfo(call):
    r = requests.get(call)
    return r.json()

clear = lambda: os.system('cls')

config = ConfigParser()
res = config.read('config.ini')

print('-----------Version '+ version +'-----------')
tprint("Hy-DRP")
print('---------Made by TubYoub---------')
print('-------Please Report Bugs--------')

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

print('-----------Version '+ version +'-----------')
tprint("Hy-DRP")
print('---------Made by TubYoub---------')
print('-------Please Report Bugs--------')

while True:
    clear()

    print('-----------Version ' + version + '-----------')
    tprint("Hy-DRP")
    print('---------Made by TubYoub---------')
    print('-------Please Report Bugs--------')

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
            stat1 = 'Played Games: ' + str(data['player']['stats']['Bedwars']['games_played_bedwars_1'])
            stat2 = 'Coins: ' + str(data['player']['stats']['Bedwars']['coins'])
            stat3 = 'Recources collected: ' + str(data['player']['stats']['Bedwars']['resources_collected_bedwars'])
            stat4 = 'Purchased Items: ' + str(data['player']['stats']['Bedwars']['_items_purchased_bedwars'])
            stat5 = 'Kills: ' + str(data['player']['stats']['Bedwars']['kills_bedwars'])
            stat6 = 'Final Kills: ' + str(data['player']['stats']['Bedwars']['final_kills_bedwars'])
            stat7 = 'Wins: ' + str(data['player']['stats']['Bedwars']['wins_bedwars'])
            stat8 = 'Coins:' + str(data['player']['stats']['Bedwars']['coins'])
            currentGame = 'Bedwars' + lobby

        elif gameType == 'SKYWARS':
            old_APPLICATION_ID = APPLICATION_ID
            APPLICATION_ID = '878328645813407837'
            stat1 = 'Played Games: ' + str(data['player']['stats']['SkyWars']['games_played_skywars'])
            stat2 = 'Kills: ' + str(data['player']['stats']['SkyWars']['kills'])
            stat3 = 'Coins: ' + str(data['player']['stats']['SkyWars']['coins'])
            stat4 = 'Tokens: ' + str(data['player']['stats']['SkyWars']['cosmetic_tokens'])
            stat5 = 'Wins: ' + str(data['player']['stats']['SkyWars']['wins'])
            stat6 = 'Played Games: ' + str(data['player']['stats']['SkyWars']['games_played_skywars'])
            stat7 = 'Kills: ' + str(data['player']['stats']['SkyWars']['kills'])
            stat8 = 'Coins: ' + str(data['player']['stats']['SkyWars']['coins'])
            currentGame = 'Skywars' + lobby

        elif gameType == 'MURDERMYSTERY':
            old_APPLICATION_ID = APPLICATION_ID
            APPLICATION_ID = '878328439520759828'
            stat1 = 'Played Games: ' + str(data['player']['stats']['MurderMystery']['games'])
            stat2 = 'Kills: ' + str(data['player']['stats']['MurderMystery']['kills'])
            stat3 = 'Coins: ' + str(data['player']['stats']['MurderMystery']['coins'])
            stat4 = 'Wins: ' + str(data['player']['stats']['MurderMystery']['wins'])
            stat5 = 'Murder chance: ' + str(data['player']['stats']['MurderMystery']['murderer_chance'])
            stat6 = 'Played Games: ' + str(data['player']['stats']['MurderMystery']['games'])
            stat7 = 'Kills: ' + str(data['player']['stats']['MurderMystery']['kills'])
            stat8 = 'Coins: ' + str(data['player']['stats']['MurderMystery']['coins'])
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
            stat1 = 'Played Games: ' + str(data['player']['stats']['Duels']['games_played_duels'])
            stat2 = 'Bow shots: ' + str(data['player']['stats']['Duels']['bow_shots'])
            stat3 = 'Damage dealt: ' + str(data['player']['stats']['Duels']['damage_dealt'])
            stat4 = 'Coins: ' + str(data['player']['stats']['Duels']['coins'])
            stat5 = 'Wins: ' + str(data['player']['stats']['Duels']['wins'])
            stat6 = 'Blocks placed: ' + str(data['player']['stats']['Duels']['blocks_placed'])
            stat7 = 'Played Games: ' + str(data['player']['stats']['Duels']['games_played_duels'])
            stat8 = 'Bow shots: ' + str(data['player']['stats']['Duels']['bow_shots'])
            currentGame = 'Duels' + lobby

        elif gameType == 'PIT':
            old_APPLICATION_ID = APPLICATION_ID
            APPLICATION_ID = '884052292591034378'
            stat1 = 'Bow shots: ' + str(data['player']['stats']['Pit']['pit_stats_ptl']['arrows_fired'])
            stat2 = 'Kills: ' + str(data['player']['stats']['Pit']['pit_stats_ptl']['kills'])
            stat3 = 'Gold: ' + str(data['player']['stats']['Pit']['pit_stats_ptl']['ingots_cash'])
            stat4 = 'Playtime: ' + str(data['player']['stats']['Pit']['pit_stats_ptl']['playtime_minutes']) + ' minutes'
            stat5 = 'Bow shots: ' + str(data['player']['stats']['Pit']['pit_stats_ptl']['arrows_fired'])
            stat6 = 'Kills: ' + str(data['player']['stats']['Pit']['pit_stats_ptl']['kills'])
            stat7 = 'Gold: ' + str(data['player']['stats']['Pit']['pit_stats_ptl']['ingots_cash'])
            stat8 = 'Playtime: ' + str(data['player']['stats']['Pit']['pit_stats_ptl']['playtime_minutes']) + ' minutes'
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
        print(status)
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

        if config.get('main','button') == 'False' and config.get('main','print_to_console') == 'False':
            RPC.update(details=currentGame, state=state, large_image='large', large_text='Gamemode',small_image='small', small_text='mc.hypixel.net', start=starttime)

        elif config.get('main', 'button') == 'False' and config.get('main', 'print_to_console') == 'True':
            print(RPC.update(details=currentGame, state=state, large_image='large', large_text='Gamemode',small_image='small', small_text='mc.hypixel.net', start=starttime))

        elif config.get('main', 'button') == 'True' and config.get('main', 'print_to_console') == 'False':
            RPC.update(details=currentGame, state=state, large_image='large', large_text='Gamemode',small_image='small', small_text='mc.hypixel.net', start=starttime,buttons=[{"label": "/f add " + name, "url": "https://plancke.io/hypixel/player/stats/" + uuid}])

        elif config.get('main', 'button') == 'True' and config.get('main', 'print_to_console') == 'True':
            print(RPC.update(details=currentGame, state=state, large_image='large', large_text='Gamemode',small_image='small', small_text='mc.hypixel.net', start=starttime,buttons=[{"label": "/f add " + name, "url": "https://plancke.io/hypixel/player/stats/" + uuid}]))

        else:
            RPC.update(details=currentGame, state=state, large_image='large', large_text='Gamemode',small_image='small', small_text='mc.hypixel.net', start=starttime,buttons=[{"label": "/f add " + name, "url": "https://plancke.io/hypixel/player/stats/" + uuid}])
        time.sleep(15)