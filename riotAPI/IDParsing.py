import  json

def getId(jsonFile):
    return jsonFile.get("id")

def getAccountID(jsonFile):
    return jsonFile.get("accountId")

def getMatchID(jsonFile):
    return jsonFile.get("gameid")