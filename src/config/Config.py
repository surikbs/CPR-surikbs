import json
def getBrokerAppConfig():
    with open('../config/brokerapp.json', 'r') as brokerapp:
        jsonUserData = json.load(brokerapp)
        return jsonUserData

def getSystemConfig():
    with open('../config/system.json', 'r') as system:
        jsonSystemData = json.load(system)
        return jsonSystemData


def getServerConfig():
    with open('../config/server.json', 'r') as server:
        jsonServerData = json.load(server)
        return jsonServerData