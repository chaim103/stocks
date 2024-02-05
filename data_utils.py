import os
from datetime import time
import Yfinance as yf
import pandas as pd



def all_tickers(start, end):
    # # yf.nasdaq_traded() the list of all nasdaq traded stocks vs yf.Tickers('nasdaq') which is a list of all nasdaq stocks
    # # print a simple test to see the difference
    # a= (yf.nasdaq_traded())  # list of all nasdaq traded stocks
    # b = (yf.Tickers('nasdaq'))  # list of all nasdaq stocks
    # # compare the two with if statement
    # if a == b:
    #     print('The two lists are the same')
    # else:
    #     print('The two lists are different')
    #
    #
    #
    # yf.other_options()
# nasdaq_tickers = yf.Tickers('nasdaq')
    ticker_list_names = []
    nasdaq_ticker_list = yf.Tickers('nasdaq').tickers
    for ticker in nasdaq_ticker_list:
        # print(ticker.info)
        try:
            ticker_list_names.append(ticker.info['symbol'])
            date = load_data(ticker, start, end)
            save_data(date, f'./data/{ticker}_{start}_{end}.csv')
            print(f'{ticker} data has been saved')

        except:
            print(f'{ticker} data could not be saved')
            continue
    return ticker_list_names

def update_csv_dates(ticker, start, end):
    try:
        data = load_data(ticker, start, end)
        save_data(data, f'./data/{ticker}_{start}_{end}.csv')
        print(f'{ticker} data has been updated')
    except:
        print(f'{ticker} data could not be updated')
        return None


def all_file_names():
    files = os.listdir('./data')
    return files

def read_data(path):
    data = pd.read_csv(path)
    return data

def save_data(data, filename):
    with open (filename, 'w') as f:
        for d in data:
            f.write(str(d) + '\n')




def load_data(ticker, start, end):
    data = yf.download(ticker, start=start, end=end)
    # add delay so server doesn't get mad
    time.sleep(1)



    return data


if __name__ == '__main__':
    start , end = '2020-01-01', '2020-12-31'





