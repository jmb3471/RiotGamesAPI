import requests
from riotAPI.IDParsing import *

from riotAPI.auth import API_KEY
from riotAPI.check_status import check_status_summoner

URL = 'https://na1.api.riotgames.com/'
Header = '?api_key=' + API_KEY


def getSummonerbyName(name, URL):
	response = requests.get(URL + "/lol/summoner/v4/summoners/by-name/" + name + Header)
	check_status_summoner(response)
	return response.json()

def getSummonerInfo(name, region):
	URL = 'https://' + region + '.api.riotgames.com/'
	response = requests.get(URL + "/lol/league/v4/entries/by-summoner/" + getId(getSummonerbyName(name, URL)) + Header)
	check_status_summoner(response)
	return response.json()

def getSummonerMatches(name, region):
	URL = 'https://' + region + '.api.riotgames.com/'
	response = requests.get(URL + '/lol/match/v4/matchlists/by-account/' + getAccountID(getSummonerbyName(name, URL)) + Header)
	check_status_summoner(response)
	return response.json()

def main():
	matches = getSummonerMatches("elophantsoup", 'na1')
	print(getSummonerInfo("Bigjonathan13", 'na1'))
	return

if __name__ == '__main__':
	main()