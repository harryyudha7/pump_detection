from PyQt6.QtWidgets import QTableView, QHeaderView, QProgressBar, QMessageBox, QWidget, QGridLayout, QFrame, QComboBox, QPushButton, QSpacerItem, QRadioButton, QScrollArea
from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout, QLineEdit, QToolBox
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QPixmap, QFont

import pandas as pd
import numpy as np
from views.price_db_status_views import PandasModel
from datetime import datetime
import re
import ta
from  pyearth import Earth
from sklearn import preprocessing

from views.sql_function import SQL_function

import warnings
warnings.filterwarnings('ignore')

def get_node_mars(model):
    list_summary = model.summary().split('\n')
    new_list_summary = []
                
    for j in list_summary:
        if 'Yes' not in j:
            new_list_summary.append(j)

    basis_function_numbers = []

    for line in new_list_summary:
        match = re.search(r'h\(x0-([\d.]+)\)|h\(([\d.]+)-x0\)|h\(([\d.]+)\)\s+No', line)
        if match:
            basis_function_numbers.extend(match.group(1, 2, 3))

    basis_number = []
    for i in basis_function_numbers:
        if not i is None:
            basis_number.append(float(i))
    basis_number.sort()
    return basis_number

class technical_statistics_ui(QWidget):
    # def __init__(self, db_status):
    #     # super(technical_statistics_ui, self).__init__(arguments to parent class)
    #     self.db_status = db_status

    def setup_ui(self, db_status):
        layout = QVBoxLayout()
        # layout.addWidget(self.text_place)
        self.setLayout(layout)

        self.df_technical = pd.read_csv('technical_statistics.csv')
        self.df_technical = self.df_technical.drop(columns=['Unnamed: 0'])

        model = PandasModel(self.df_technical)
        self.tableView = QTableView()
        self.tableView.setModel(model)
        header = self.tableView.horizontalHeader()
        for i in range(len(self.df_technical.columns)):
            header.setSectionResizeMode(i, QHeaderView.ResizeMode.ResizeToContents)
        layout.addWidget(self.tableView)

        self.download_btn = QPushButton()
        self.download_btn.setText('Download')
        layout.addWidget(self.download_btn)
        self.download_btn.clicked.connect(self.download_data)

        self.update_btn = QPushButton()
        self.update_btn.setText('Update Data')
        layout.addWidget(self.update_btn)
        self.update_btn.clicked.connect(self.update_data)

        self.progress = QProgressBar()
        layout.addWidget(self.progress)

        self.db_status = db_status

    def download_data(self):
        now = datetime.now()
        str_now = now.strftime('%d_%m_%Y')
        filename = 'technical_statistics_' + str_now + '.csv'
        self.df_technical.to_csv(filename)
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Information)
        # msg.setText("Success")
        msg.setInformativeText('Download Data Successful.')
        msg.setWindowTitle("Download Data")
        msg.exec()

    def update_data(self):
        arr_last_slope = []
        arr_last_slope_adi = []
        arr_aroon_up = []
        arr_aroon_down = []
        arr_aroon_diff = []
        arr_macd_diff = []
        arr_macd_line = []
        arr_macd_signal = []
        arr_stochastic = []
        arr_stochastic_signal = []
        arr_delta_stochastic = []
        arr_rsi_val = []
        arr_coef_corr = []
        arr_last_slope_btc = []
        arr_market = []
        pw = '27111998'
        db = 'crypto_db'
        connection = SQL_function.create_db_connection("localhost", "root", pw, db)
        for i in range(len(self.db_status)):
            try:
                self.progress.setValue(int((i+1)/len(self.db_status)*100))
                market = self.db_status['table'].iloc[i]
                print(market)
                if self.db_status['remarks'].iloc[i] == 'Database is up to date.':
                    query = 'SELECT * FROM %s ORDER BY timestamp ASC' % market
                    cur = SQL_function.execute_query(connection,query)
                    res = cur.fetchall()
                    df = pd.DataFrame(res,columns=['timestamp', 'open','high', 'low','close','volume'])
                    df = df.drop_duplicates()
                    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
                    day_df = (df.resample('D', on='timestamp').agg({'open': 'first', 'high': 'max', 'low': 'min', 'close': 'last','volume': 'mean'}))
                    day_df['timestamp'] = day_df.index

                    num_idx = min([365, len(day_df)])
                    
                    model_price = Earth()
                    scaler = preprocessing.MinMaxScaler(feature_range=(0,100))
                    scaled_price = scaler.fit_transform(day_df['close'].iloc[-num_idx:].values.reshape(-1,1))

                    arr_x = np.arange(num_idx)
                    model_price.fit(arr_x,scaled_price.flatten())
                    y_pred = model_price.predict(arr_x)
                    basis_node = get_node_mars(model_price)
                    last_node = int(basis_node[-1])
                    last_slope = (y_pred[-1] - y_pred[last_node])/(arr_x[-1] - arr_x[last_node])

                    adi = ta.volume.AccDistIndexIndicator(high=df['high'],low=df['low'],close=df['close'],volume=df['volume']).acc_dist_index()
                    model_adi = Earth()
                    scaler_adi = preprocessing.MinMaxScaler(feature_range=(0,1000))
                    data_num_adi = min([2000,len(df)])
                    scaled_adi = scaler_adi.fit_transform(df['close'].iloc[-data_num_adi:].values.reshape(-1,1))
                    arr_x_adi = np.arange(data_num_adi)/24
                    model_adi.fit(arr_x_adi,scaled_adi.flatten())

                    y_pred_adi = model_adi.predict(arr_x_adi)
                    basis_node = get_node_mars(model_adi)
                    last_node = basis_node[-1]
                    last_slope_adi = (y_pred_adi[-1] - model_adi.predict([last_node]))[0]/(arr_x[-1] - last_node)
                    aroon = ta.trend.AroonIndicator(low=day_df['low'],high=day_df['high'])
                    aroon_up = aroon.aroon_up()[-1]
                    aroon_down = aroon.aroon_down()[-1]
                    aroon_diff = aroon.aroon_indicator()[-1]

                    macd = ta.trend.MACD(close=pd.Series(scaled_price.flatten()))
                    macd_diff = macd.macd_diff().values[-1]
                    macd_line = macd.macd().values[-1]
                    macd_signal = macd.macd_signal().values[-1]

                    stoch_oscillator = ta.momentum.StochasticOscillator(high=day_df['high'], low=day_df['low'], close=day_df['close'])
                    stochastic = stoch_oscillator.stoch().values[-1]
                    stochastic_signal = stoch_oscillator.stoch_signal().values[-1]
                    delta_stochastic = stochastic - stochastic_signal

                    rsi_indicator = ta.momentum.RSIIndicator(close=pd.Series(scaled_price.flatten()))
                    rsi_val = rsi_indicator.rsi().values[-1]

                    query = 'SELECT * FROM btcusdt ORDER BY timestamp ASC'
                    cur = SQL_function.execute_query(connection,query)
                    res = cur.fetchall()
                    df_btc = pd.DataFrame(res,columns=['timestamp', 'open','high', 'low','close','volume'])
                    df_btc = df_btc.drop_duplicates()
                    df_btc['timestamp'] = pd.to_datetime(df_btc['timestamp'], unit='ms')
                    # df_btc = df_btc[df_btc['timestamp'] <= start_point]
                    
                    day_df_btc = (df_btc.resample('D', on='timestamp').agg({'open': 'first', 'high': 'max', 'low': 'min', 'close': 'last','volume': 'mean'}))
                    day_df_btc['timestamp'] = day_df_btc.index

                    alt_vs_btc = pd.DataFrame({'alt': day_df['close'].iloc[-num_idx:], 'btc': day_df_btc['close'].iloc[-num_idx:]})
                    df_corr = alt_vs_btc.corr()
                    coef_corr = df_corr['alt']['btc']

                    model_btc = Earth()
                    scaler_btc = preprocessing.MinMaxScaler(feature_range=(0,100))
                    scaled_price_btc = scaler_btc.fit_transform(day_df_btc['close'].iloc[-num_idx:].values.reshape(-1,1))

                    arr_x = np.arange(num_idx)
                    model_btc.fit(arr_x,scaled_price_btc.flatten())

                    y_pred_btc = model_btc.predict(arr_x)
                    basis_node_btc = get_node_mars(model_btc)
                    last_node_btc = int(basis_node_btc[-1])
                    last_slope_btc = (y_pred_btc[-1] - y_pred_btc[last_node_btc])/(arr_x[-1] - arr_x[last_node_btc])

                    arr_last_slope.append(last_slope)
                    arr_last_slope_adi.append(last_slope_adi)
                    arr_aroon_up.append(aroon_up)
                    arr_aroon_down.append(aroon_down)
                    arr_aroon_diff.append(aroon_diff)
                    arr_macd_diff.append(macd_diff)
                    arr_macd_line.append(macd_line)
                    arr_macd_signal.append(macd_signal)
                    arr_stochastic.append(stochastic)
                    arr_stochastic_signal.append(stochastic_signal)
                    arr_delta_stochastic.append(delta_stochastic)
                    arr_rsi_val.append(rsi_val)
                    arr_coef_corr.append(coef_corr)
                    arr_last_slope_btc.append(last_slope_btc)
                    arr_market.append(market)
            except Exception as e:
                print(market, e)
                arr_last_slope.append(np.nan)
                arr_last_slope_adi.append(np.nan)
                arr_aroon_up.append(np.nan)
                arr_aroon_down.append(np.nan)
                arr_aroon_diff.append(np.nan)
                arr_macd_diff.append(np.nan)
                arr_macd_line.append(np.nan)
                arr_macd_signal.append(np.nan)
                arr_stochastic.append(np.nan)
                arr_stochastic_signal.append(np.nan)
                arr_delta_stochastic.append(np.nan)
                arr_rsi_val.append(np.nan)
                arr_coef_corr.append(np.nan)
                arr_last_slope_btc.append(np.nan)
                arr_market.append(market)
        self.current_data = pd.DataFrame({'last_calculation': [datetime.today() for i in arr_market],
                                     'market': arr_market,
                         })
        self.current_data['last_slope'] = arr_last_slope
        self.current_data['last_slope_adi'] = arr_last_slope_adi
        self.current_data['aroon_up'] = arr_aroon_up
        self.current_data['aroon_down'] = arr_aroon_down
        self.current_data['aroon_diff'] = arr_aroon_diff
        self.current_data['macd_diff'] = arr_macd_diff
        self.current_data['macd_line'] = arr_macd_line
        self.current_data['macd_signal'] = arr_macd_signal
        self.current_data['stochastic'] = arr_stochastic
        self.current_data['stochastic_signal'] = arr_stochastic_signal
        self.current_data['delta_stochastic'] = arr_delta_stochastic
        self.current_data['rsi_val'] = arr_rsi_val
        self.current_data['coef_corr'] = arr_coef_corr
        self.current_data['last_slope_btc'] = arr_last_slope_btc
        self.current_data = self.current_data.dropna()
        try:
            self.current_data.to_csv('technical_statistics.csv')
        except PermissionError as pe:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Critical)
            # msg.setText("Success")
            msg.setInformativeText('Permission denied. Please close file technical_statistics.csv')
            msg.setWindowTitle("Updating data")
            msg.exec()
        model = PandasModel(self.current_data)
        self.tableView.setModel(model)