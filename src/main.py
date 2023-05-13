import logging,os
from config.Config import getBrokerAppConfig, getServerConfig

def initLoggingConfg(filepath):
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(filename=filepath, format=format, level=logging.INFO, datefmt="%Y-%m-%d %H:%M:%S")

serverConfig = getServerConfig()
deployDir = serverConfig['deployDir']
if os.path.exists(deployDir) == False:
    print("Deploy Directory " + deployDir + " does not exist. Exiting the app.")
    exit(-1)

logFileDir = serverConfig['logFileDir']
if os.path.exists(logFileDir) == False:
    print("LogFile Directory " + logFileDir + " does not exist. Exiting the app.")
    exit(-1)

print("Deploy  Directory = " + deployDir)
print("LogFile Directory = " + logFileDir)
initLoggingConfg(logFileDir + "/app.log")

logging.info('serverConfig => %s', serverConfig)
brokerAppConfig = getBrokerAppConfig()
logging.info('brokerAppConfig => %s', brokerAppConfig)
