from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://data.nba.net"
ALL_JSON = "/prod/v1/today/json"

viewdata = PrettyPrinter()

def get_uris():
    nbadata = get(BASE_URL + ALL_JSON).json()
    uris = nbadata['uris']
    return uris

def get_scoreboard():
    scoreboard = get_uris()['currentScoreboard']
    nbadata = get(BASE_URL + scoreboard).json()['games']
    

    for game in games:
        home_team = game['hTeam']
        away_team = game['vTeam']
        clock = game['clock']
        period = game['period']
        
        print('--------------Stats-----------------')  
        print(f"{home_team['triCode']} vs {away_team['triCode']}")
        print(f"{home_team['score']} vs {away_team['score']}")  
        print(f"{clock} - {period['current']}")  

def get_stats():
    stats = get_uris()['leagueTeamStatsLeaders']
    nbadata = get(BASE_URL + stats).json()['league']['standart']['regularSeason']['teams']
    
    for team in teams:
        name = team['name']
        nickname = team['nickname']
        ppg = team['ppg']
        print(f"{name} - {nickname} - {ppg}")
    
    
    
    
    viewdata.pprinter(nbadata)
    
get_stats()