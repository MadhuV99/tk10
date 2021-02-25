# cryptocap using API from www.coinmarketcap.com
'''
Command to create .exe file with other files in dist/filename folder:
        pyinstaller filname.py
    Copy favicon.ico file to the dist/filename folder

Command to create SINGLE .exe file in dist folder:
        pyinstaller filename.py --onefile --noconsole --icon=favicon.ico
    Keep favicon.ico file along with the .exe file in the same folder
'''
import requests, json
from tkinter import *


def font_color(amount):
    if amount >= 0:
        return 'green'
    else:
        return 'red'



def my_portfolio():
    # api_requests = requests.get("https://api.coinmarketcap.com/v1/ticker/") 
    api_requests = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=300&convert=USD&CMC_PRO_API_KEY=SECRET-KEY") 
    api = json.loads(api_requests.content)
    # print(api)
    '''
    {
    'status': {
            'timestamp': '2021-02-24T03:04:42.213Z', 
            'error_code': 0, 'error_message': None, 
            'elapsed': 11, 'credit_count': 1,
            'notice': None, 'total_count': 4160
            }, 
    'data': [
        {
        'id': 1, 
        'name': 'Bitcoin', 
        'symbol': 'BTC', 
        'slug': 'bitcoin', 
        'num_market_pairs': 9733, 
        'date_added': '2013-04-28T00:00:00.000Z', 
        'tags': ['mineable', 'pow', 'sha-256', 'store-of-value', 'state-channels', 'coinbase-ventures-portfolio', 'three-arrows-capital-portfolio', 'polychain-capital-portfolio'], 
        'max_supply': 21000000, 
        'circulating_supply': 18636862, 
        'total_supply': 18636862, 
        'platform': None, 
        'cmc_rank': 1, 
        'last_updated': '2021-02-24T03:03:02.000Z', 
        'quote': {
            'USD':{
                'price': 50270.5288431758, 
                'volume_24h': 109699558618.71075, 
                'percent_change_1h': 3.64591774, 
                'percent_change_24h': -4.36881374, 
                'percent_change_7d': 1.50412444, 
                'percent_change_30d': 52.49682522, 
                'market_cap': 936884908717.2871, 
                'last_updated': '2021-02-24T03:03:02.000Z'
                }
            }
        }, 
        {
        'id': 1027, 'name': 'Ethereum', 'symbol': 'ETH', 'slug': 'ethereum', 'num_market_pairs': 6016, 'date_added': '2015-08-07T00:00:00.000Z', 'tags': ['mineable', 'pow', 'smart-contracts', 'coinbase-ventures-portfolio', 'three-arrows-capital-portfolio', 'polychain-capital-portfolio'], 'max_supply': None, 'circulating_supply': 114796830.374, 'total_supply': 114796830.374, 'platform': None, 'cmc_rank': 2, 'last_updated': '2021-02-24T03:03:02.000Z', 
        'quote': {'USD': {'price': 1620.905064853543, 'volume_24h': 53437984689.85633, 'percent_change_1h': 3.38641335, 'percent_change_24h': -5.48481193, 'percent_change_7d': -8.46622042, 'percent_change_30d': 13.25221493, 'market_cap': 186074763782.34964, 'last_updated': '2021-02-24T03:03:02.000Z'}}
        }
        ]
    }
    '''
    coins = [
        {
            'symbol': 'BTC',
            'amount_owned': 2,
            'price_per_coin': 3200
        }, 
        {
            'symbol': 'EOS',
            'amount_owned': 100,
            'price_per_coin': 12.05
        },
        {
            'symbol': 'LTC',
            'amount_owned': 75,
            'price_per_coin': 25
        },
        {
            'symbol': 'XMR',
            'amount_owned': 10,
            'price_per_coin': 140.05
        },
    ]
    print('-'*10)
    print('-'*10)
    total_pl = 0.0
    total_current_value = 0
    coin_row = 1
    for i in range(0, 300):
        for coin in coins:
            if api['data'][i]['symbol'] == coin['symbol']:
                total_paid = coin['amount_owned'] * coin['price_per_coin']
                current_value = coin['amount_owned'] * api['data'][i]['quote']['USD']['price']
                pl_percoin = api['data'][i]['quote']['USD']['price'] - coin['price_per_coin']
                total_pl_coin = pl_percoin * coin['amount_owned']
                total_current_value += current_value
                total_pl += total_pl_coin

                # print(api['data'][i]['name'] + ' - ' + api['data'][i]['symbol'])
                # print("Price - ${0:.2f}".format(api['data'][i]['quote']['USD']['price']))
                # print('Number of Coin:', coin['amount_owned'])
                # print('Total Amount Paid: ${0:.2f}'.format(total_paid))
                # print('Current Value: ${0:.2f}'.format(current_value))
                # print('P/L Per Coin: ${0:.2f}'.format(pl_percoin))
                # print('Total P/L with Coin: ${0:.2f}'.format(total_pl_coin))
                # print('-'*10)
                
                name = Label(pycrypto, text=api['data'][i]['symbol'], bg='#F3F4F6', fg='black', font=('Lato', 10, 'normal'), padx=2, pady=2, borderwidth=2, relief='groove')
                name.grid(row=coin_row, column=0, sticky=N+S+E+W)
                
                price = Label(pycrypto, text="${0:,.2f}".format(api['data'][i]['quote']['USD']['price']), bg='#F3F4F6', fg='black', font=('Lato', 10, 'normal'), padx=2, pady=2, borderwidth=2, relief='groove')
                price.grid(row=coin_row, column=1, sticky=N+S+E+W)
                
                no_coins = Label(pycrypto, text=coin['amount_owned'], bg='#F3F4F6', fg='black', font=('Lato', 10, 'normal'), padx=2, pady=2, borderwidth=2, relief='groove')
                no_coins.grid(row=coin_row, column=2, sticky=N+S+E+W)
                
                amount_paid = Label(pycrypto, text="${0:,.2f}".format(total_paid), bg='#F3F4F6', fg='black', font=('Lato', 10, 'normal'), padx=2, pady=2, borderwidth=2, relief='groove')
                amount_paid.grid(row=coin_row, column=3, sticky=N+S+E+W)
                
                current_val = Label(pycrypto, text="${0:,.2f}".format(current_value), bg='#F3F4F6', fg='black', font=('Lato', 10, 'normal'), padx=2, pady=2, borderwidth=2, relief='groove')
                current_val.grid(row=coin_row, column=4, sticky=N+S+E+W)
                
                pl_coin = Label(pycrypto, text="${0:,.2f}".format(pl_percoin), bg='#F3F4F6', fg=font_color(pl_percoin), font=('Lato', 10, 'normal'), padx=2, pady=2, borderwidth=2, relief='groove')
                pl_coin.grid(row=coin_row, column=5, sticky=N+S+E+W)
                
                totalpl = Label(pycrypto, text="${0:,.2f}".format(total_pl_coin), bg='#F3F4F6', fg=font_color(total_pl_coin), font=('Lato', 10, 'normal'), padx=2, pady=2, borderwidth=2, relief='groove')
                totalpl.grid(row=coin_row, column=6, sticky=N+S+E+W)
                
                coin_row += 1
                break

    totalcv = Label(pycrypto, text="${0:,.2f}".format(total_current_value), bg='#F3F4F6', fg='black', font=('Lato', 10, 'normal'), padx=2, pady=2, borderwidth=2, relief='groove')
    totalcv.grid(row=coin_row, column=4, sticky=N+S+E+W)

    # print('Total P/L for Portfoli: ${0:.2f}'.format(total_pl))
    totalpl = Label(pycrypto, text="${0:,.2f}".format(total_pl), bg='#F3F4F6', fg=font_color(total_pl), font=('Lato', 10, 'normal'), padx=2, pady=2, borderwidth=2, relief='groove')
    totalpl.grid(row=coin_row, column=6, sticky=N+S+E+W)

    api = ""
    update = Button(pycrypto, text="Update", bg='#142E54', fg='white', font=('Lato', 10, 'normal'), padx=2, pady=2, borderwidth=2, relief='groove', command=my_portfolio)
    update.grid(row=coin_row + 1, column=6, sticky=N+S+E+W)

pycrypto = Tk()
pycrypto.title('My Crypto Portfolio')
pycrypto.iconbitmap('favicon.ico')

name = Label(pycrypto, text='Coin Name', bg='#142E54', fg='white', font=('Lato', 12, 'bold'), padx=5, pady=5, borderwidth=2, relief='groove')
name.grid(row=0, column=0, sticky=N+S+E+W)

price = Label(pycrypto, text='Price', bg='#142E54', fg='white', font=('Lato', 12, 'bold'), padx=5, pady=5, borderwidth=2, relief='groove')
price.grid(row=0, column=1, sticky=N+S+E+W)

no_coins = Label(pycrypto, text='Coin Owned', bg='#142E54', fg='white', font=('Lato', 12, 'bold'), padx=5, pady=5, borderwidth=2, relief='groove')
no_coins.grid(row=0, column=2, sticky=N+S+E+W)

amount_paid = Label(pycrypto, text='Total Amount Paid', bg='#142E54', fg='white', font=('Lato', 12, 'bold'), padx=5, pady=5, borderwidth=2, relief='groove')
amount_paid.grid(row=0, column=3, sticky=N+S+E+W)

current_val = Label(pycrypto, text='Current Value', bg='#142E54', fg='white', font=('Lato', 12, 'bold'), padx=5, pady=5, borderwidth=2, relief='groove')
current_val.grid(row=0, column=4, sticky=N+S+E+W)

pl_coin = Label(pycrypto, text='P/L Per Coin', bg='#142E54', fg='white', font=('Lato', 12, 'bold'), padx=5, pady=5, borderwidth=2, relief='groove')
pl_coin.grid(row=0, column=5, sticky=N+S+E+W)

totalpl = Label(pycrypto, text='Total P/L with Coin', bg='#142E54', fg='white', font=('Lato', 12, 'bold'), padx=5, pady=5, borderwidth=2, relief='groove')
totalpl.grid(row=0, column=6, sticky=N+S+E+W)

my_portfolio()
pycrypto.mainloop()
# print('Program Completed')

