import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import json
import copy
import numpy as np
from sklearn.linear_model import LinearRegression

st.set_page_config(layout="wide")

df_data_pump = pd.read_csv('pump_lessthan30.csv')


def plot_candlestick(coin, start_date, final_date, base_date=0):
    temp_df = copy.deepcopy(df_checked[coin]).dropna()
    close_price = temp_df['price'].iloc[1:].values
    temp_df = temp_df[:-1]
    temp_df['close_price'] = close_price
    temp_df = temp_df[temp_df['snapped_at'] >= start_date]
    temp_df = temp_df[temp_df['snapped_at'] <= final_date]
    high_price = np.maximum(temp_df['price'], temp_df['close_price'])
    low_price = np.minimum(temp_df['price'], temp_df['close_price'])
    fig = go.Figure(data=[go.Candlestick(x=temp_df['snapped_at'],
                open=temp_df['price'],
                high=high_price,
                low=low_price,
                close=temp_df['close_price'])])
    if base_date != 0:
        fig.update_layout(title=coin,
            shapes = [dict(
            x0=base_date, x1=base_date, y0=0, y1=1, xref='x', yref='paper',
            line_width=2)])
    return fig

f = open('df_checked_dict.json')
data = json.load(f)

df_checked = {}
for i in data.keys():
    df_checked[i] = pd.DataFrame.from_dict(data[i])
    df_checked[i]['snapped_at'] = pd.to_datetime(df_checked[i]['snapped_at'], format='%Y-%m-%d %H:%M:%S UTC')

df_data_pump['base_date'] = pd.to_datetime(df_data_pump['base_date'], format='%Y-%m-%d')
df_data_pump['max_date'] = pd.to_datetime(df_data_pump['max_date'], format='%Y-%m-%d')
df_data_pump['pump_length'] = df_data_pump['max_date'] - df_data_pump['base_date']

PCT_THRESHOLD = 0.25
# base_date_new = df_data_pump['base_date']
for i in df_data_pump.index:
    coin = df_data_pump.iloc[i]['coin']
    base_date = df_data_pump.iloc[i]['base_date']
    temp_df = df_checked[coin]
    temp_df['ma'] = temp_df['price'].rolling(window=7).mean()
    temp_df = temp_df.dropna()
    temp_df = temp_df[temp_df['snapped_at'] >= base_date]
    temp_df['pct_to_ma'] = (temp_df['price'] - temp_df['ma'])/temp_df['ma']
    temp_df = temp_df[temp_df['pct_to_ma'] >= PCT_THRESHOLD]
    try:
        df_data_pump['base_date'][i] = temp_df['snapped_at'][0] - pd.Timedelta(1,'d')
    except: print(df_data_pump.iloc[i])


arr_listing = []
for i in df_data_pump['coin']:
    date_listing = df_checked[i]['snapped_at'][0]
    arr_listing.append(date_listing)
df_data_pump['date_listing'] = arr_listing

df_data_pump['pump_to_listing'] = df_data_pump['base_date'] - df_data_pump['date_listing']

pump_length_threshold = st.number_input('PUMP LENGTH THRESHOLD: ',step=1,value=30)
listing_threshold = st.number_input('LISTING THRESHOLD: ',step=1,value=90)
df_data_pump = df_data_pump[df_data_pump['pump_to_listing'] > pd.Timedelta(listing_threshold,'d')]
df_data_pump = df_data_pump[df_data_pump['pump_length'] <= pd.Timedelta(pump_length_threshold,'d')]

number_of_regression = st.number_input('DATA FOR REGRESSION: ',step=1,value=30)
arr_state = []
for i in df_data_pump.index:
    coin = df_data_pump['coin'][i]
    base_date = df_data_pump['base_date'][i]
    temp_df = df_checked[coin]
    temp_df = temp_df[temp_df['snapped_at'] > base_date-pd.Timedelta(number_of_regression,'d')]
    temp_df = temp_df[temp_df['snapped_at'] <= base_date]
    x = (temp_df['snapped_at'] - temp_df['snapped_at'][0]).dt.days.values.reshape(-1, 1)
    y = temp_df['price']
    lr = LinearRegression()
    lr.fit(x,y)
    if lr.coef_ <= 0:
        arr_state.append('bearish')
    else:
        arr_state.append('bullish')
df_data_pump['state'] = arr_state

state = st.selectbox(
     'Select state',
     ['all','bearish','bullish'])

if state != 'all':
    df_data_pump = df_data_pump[df_data_pump['state'] == state]

df_data_pump_disp = copy.deepcopy(df_data_pump)
df_data_pump_disp['base_date'] = df_data_pump_disp['base_date'].dt.strftime('%d-%m-%Y')
df_data_pump_disp['max_date'] = df_data_pump_disp['max_date'].dt.strftime('%d-%m-%Y')
df_data_pump_disp['pump_length'] = df_data_pump_disp['pump_length'].dt.days
df_data_pump_disp['date_listing'] = df_data_pump_disp['date_listing'].dt.strftime('%d-%m-%Y')
df_data_pump_disp['pump_to_listing'] = df_data_pump_disp['pump_to_listing'].dt.days

st.dataframe(df_data_pump_disp, 2000, 1000)
btn_download = st.button('Download')
if btn_download:
    df_data_pump_disp.to_csv('data.csv')

idx = st.selectbox(
     'Select data pump',
     list(df_data_pump_disp.index))
days_before = st.number_input('Days before: ',step=1,value=listing_threshold)
days_after = st.number_input('Days after: ',step=1,value=pump_length_threshold)
fig = plot_candlestick(df_data_pump['coin'][idx],df_data_pump['base_date'][idx] - pd.Timedelta(days_before, 'd'), 
                        df_data_pump['base_date'][idx]+pd.Timedelta(days_after, 'd'), base_date=df_data_pump['base_date'][idx])
fig.update_yaxes(fixedrange=False)
# option = st.selectbox(
#      'Select data pump',
#      list(df_data_pump.index))
st.plotly_chart(fig, use_container_width=True)