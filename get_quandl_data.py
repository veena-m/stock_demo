import datetime
import requests
import pandas as pd

def convert_month_string(month):
    if len(str(month)) == 1:
        return '0' + str(month)
    else:
        return str(month)


def get_time_period():

    current_month = datetime.datetime.now().month
    current_year = datetime.datetime.now().year

    if current_month != 1:
        last_month = current_month - 1
        start_year = current_year
    else:
        last_month = 12
        start_year = current_year - 1

    start_dt = str(start_year) + \
        convert_month_string(last_month) + '01'
    end_dt = str(current_year) + \
        convert_month_string(current_month) + '01'

    time_period = {
        'start_dt': start_dt,
        'end_dt': end_dt
    }
    return time_period


def get_data(
    ticker,
    url,
    params
):
    # get time period
    period = get_time_period()
    #print period
    params['ticker'] = ticker
    params['date.gte'] = period['start_dt']
    params['date.lt'] = period['end_dt']
    #print params

    response = requests.get(url, params)

    if response.status_code != 200:
        response.raise_for_status()
    return response.json()


def get_data_df(
    ticker
):
    quandl_url = 'https://www.quandl.com/api/v3/datatables/WIKI/PRICES.json'
    params_list = {
      'ticker': ticker,
      'api_key': 'C3_i-U-ohvkW6sKmvAdG',
      'qopts.columns': 'date,close'
    }
    #print ticker, quandl_url, params_list
    data = get_data(
        ticker,
        quandl_url,
        params_list
    )
    #data is in a dict, extract 
    data_req = data['datatable']['data']
    column_headings = [
        'date',
        'closing_price'
    ]

    data_df = pd.DataFrame(
        data=data_req,
        columns=column_headings
    )
    data_df['date'] = pd.to_datetime(data_df['date'])
    #data_df.set_index('date')
    #print data_df
    #return data_df.set_index('date')
    return data_df
       
