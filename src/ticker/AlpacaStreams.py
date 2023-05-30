from alpaca_trade_api.stream import Stream

ALPACA_API_KEY = '********************'
ALPACA_SECRET_KEY = '****************************************'


brokerAppDetails = self.brokerLogin.getBrokerAppDetails()
accessToken = self.brokerLogin.getAccessToken()
async def print_quote(q):
    print('quote', q)

async def print_trade(t):
    print('trade', t)

def main():
    stream = Stream(ALPACA_API_KEY,ALPACA_SECRET_KEY, raw_data=True)
    stream.subscribe_crypto_quotes(print_quote, 'BTCUSD')
    stream.subscribe_crypto_trades(print_trade, 'BTCUSD')

    @stream.on_bar('BTCUSD')
    async def _(bar):
        print('bar', bar)

    stream.run()

if __name__ == "__main__":
    main()