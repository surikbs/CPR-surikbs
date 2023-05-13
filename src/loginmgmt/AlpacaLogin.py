import logging

from config.Config import getSystemConfig
from loginmgmt.BaseLogin import BaseLogin
from alpaca.broker import BrokerClient

class AlpacaLogin(BaseLogin):
    def __init__(self, brokerAppDetails):
        BaseLogin.__init__(self, brokerAppDetails)

def login(self, args):
    logging.info('==> Alpaca Broker client initialization.args => %s', args);
    brokerClient = BrokerClient(api_key=self.brokerAppDetails.appKey,
                                secret_key=self.brokerAppDetails.appSecret)
    return brokerClient