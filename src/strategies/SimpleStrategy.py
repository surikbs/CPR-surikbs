import logging
from datetime import datetime

from instruments.Instruments import Instruments
from models.Direction import Direction
from models.ProductType import ProductType
from strategies.BaseStrategy import BaseStrategy
from utils.Utils import Utils
from trademgmt.Trade import Trade
from trademgmt.TradeManager import TradeManager

# Each strategy has to be derived from BaseStrategy
class SimpleStrategy(BaseStrategy):
    __instance = None

    @staticmethod
    def getInstance(): # singleton class
        if SimpleStrategy.__instance == None:
            SimpleStrategy()
        return SimpleStrategy.__instance

    def __init__(self):
        if SimpleStrategy.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            SimpleStrategy.__instance = self
        # Call Base class constructor
        super().__init__("SimpleStrategy")
        # Initialize all the properties specific to this strategy
        self.productType = ProductType.MIS
        self.symbols = []
        self.slPercentage = 30
        self.targetPercentage = 0
        self.startTimestamp = Utils.getTimeOfToDay(11, 0, 0) # When to start the strategy. Default is Market start time
        self.stopTimestamp = Utils.getTimeOfToDay(14, 0, 0) # This is not square off timestamp. This is the timestamp after which no new trades will be placed under this strategy but existing trades continue to be active.
        self.squareOffTimestamp = Utils.getTimeOfToDay(14, 30, 0) # Square off time
        self.capital = 100000 # Capital to trade (This is the margin you allocate from your broker account for this strategy)
        self.leverage = 0
        self.maxTradesPerDay = 2 # (1 CE + 1 PE) Max number of trades per day under this strategy
        self.isFnO = True # Does this strategy trade in FnO or not
        self.capitalPerSet = 100000 # Applicable if isFnO is True (1 set means 1CE/1PE or 2CE/2PE etc based on your strategy logic)

    def canTradeToday(self):
        # Even if you remove this function canTradeToday() completely its same as allowing trade every day
        return True

    def process(self):
        now = datetime.now()
        if now < self.startTimestamp:
            return
        if len(self.trades) >= self.maxTradesPerDay:
            return

        # Get current market price of Nifty Future
        futureSymbol = Utils.prepareMonthlyExpiryFuturesSymbol('BANKNIFTY')
        quote = self.getQuote(futureSymbol)
        if quote == None:
            logging.error('%s: Could not get quote for %s', self.getName(), futureSymbol)
            return
