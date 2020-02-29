import requests

from riotAPI.auth import API_KEY
from riotAPI.check_status import check_status_summoner

URL = 'https://na1.api.riotgames.com/'
Header = '?api_key=' + API_KEY


def getSummonerbyName(name):
	response = requests.get(URL + "/lol/summoner/v4/summoners/by-name/" + name + Header)
	check_status_summoner(response)
	return response.json()

def main():
	print(getSummonerbyName("BigJonathan13"))
	return

if __name__ == '__main__':
	main()