#to get to work pip install requests
import requests


#change to actual errors later, add comments
def check_status_summoner(response):
	if response.status_code == 200:
		return
	elif response.status_code == 400:
		print("bad request")
	elif response.status_code == 401:
		print("not authorized")
	else:
		print("lame")

	return