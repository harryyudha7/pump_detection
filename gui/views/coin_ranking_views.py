import sys
from PyQt6.QtWidgets import QVBoxLayout, QHeaderView, QTableView, QMessageBox, QWidget, QGridLayout, QFrame, QComboBox, QPushButton, QSpacerItem, QRadioButton, QTableWidget
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QPixmap, QFont
import pandas as pd
import numpy as np
from datetime import datetime
from views.price_db_status_views import PandasModel
import joblib

class coin_ranking_ui(QWidget):
    def setup_ui(self, current_technical):
        self.current_technical = current_technical
        layout = QVBoxLayout()
        # layout.addWidget(self.text_place)
        self.setLayout(layout)
        df_data_pump = pd.read_csv('data_pump_not_ico.csv')
        df_data_not_pump = pd.read_csv('data_not_pump.csv')

        df_pump_cand = df_data_pump[['market','start','last_slope', 'last_slope_adi',
       'aroon_up', 'aroon_down', 'aroon_diff', 'macd_diff', 'macd_line',
       'macd_signal', 'stochastic', 'stochastic_signal', 'delta_stochastic',
       'rsi_val', 'coef_corr', 'last_slope_btc']]
        df_not_pump_cand = df_data_not_pump[['market','start','last_slope', 'last_slope_adi',
                                            'aroon_up', 'aroon_down', 'aroon_diff', 'macd_diff', 'macd_line',
                                            'macd_signal', 'stochastic', 'stochastic_signal', 'delta_stochastic',
                                            'rsi_val', 'coef_corr', 'last_slope_btc']]
        
        df_not_pump_cand['is_pump'] = np.zeros(len(df_not_pump_cand))
        df_pump_cand['is_pump'] = np.ones(len(df_pump_cand))

        df_combine = pd.concat([df_not_pump_cand,df_pump_cand])

        arr_prob_last_slope = []
        arr_prob_macd = []
        arr_prob_macd_diff = []
        arr_prob_stochastic = []
        arr_prob_rsi = []
        arr_prob_corr_btc = []

        weight_data_pump = len(df_data_not_pump)/len(df_data_pump)

        for i in range(len(current_technical)):
            var = current_technical.iloc[i]
            last_slope_val = var['last_slope']
            band = 0.1
            last_slope = {}
            num_pump = weight_data_pump*len(df_data_pump.loc[(df_data_pump['last_slope'] >= last_slope_val - band) & (df_data_pump['last_slope'] <= last_slope_val + band)])
            num_not_pump = len(df_data_not_pump.loc[(df_data_not_pump['last_slope'] >= last_slope_val - band) & (df_data_not_pump['last_slope'] <= last_slope_val + band)])
            if num_pump+num_not_pump == 0:
                last_slope['1'] = 0.5
                last_slope['0'] = 1 - last_slope['1']
            else:
                last_slope['1'] = num_pump/(num_pump+num_not_pump)
                last_slope['0'] = 1 - last_slope['1']
            
            macd_line_val = var['macd_line']
            macd_signal_val = var['macd_signal']
            band_line = 0.5
            band_signal = 0.5
            macd_line_signal = {}
            temp = df_combine.loc[(df_combine['macd_signal'] >= macd_signal_val - band_signal) &
                                (df_combine['macd_signal'] <= macd_signal_val + band_signal) &
                                (df_combine['macd_line'] >= macd_line_val - band_line) &
                                (df_combine['macd_line'] <= macd_line_val + band_line)]
            num_pump = weight_data_pump*sum(temp['is_pump'])
            num_not_pump = len(temp['is_pump'])-sum(temp['is_pump'])
            if num_pump+num_not_pump == 0:
                macd_line_signal['1'] = 0.5
                macd_line_signal['0'] = 1 - macd_line_signal['1']
            else:
                macd_line_signal['1'] = num_pump/(num_pump+num_not_pump)
                macd_line_signal['0'] = 1 - macd_line_signal['1']
            
            macd_diff_val = var['macd_diff']
            band = 0.1
            macd_diff = {}
            num_pump = weight_data_pump*len(df_data_pump.loc[(df_data_pump['macd_diff'] >= macd_diff_val - band) & (df_data_pump['macd_diff'] <= macd_diff_val + band)])
            num_not_pump = len(df_data_not_pump.loc[(df_data_not_pump['macd_diff'] >= macd_diff_val - band) & (df_data_not_pump['macd_diff'] <= macd_diff_val + band)])
            if num_pump+num_not_pump == 0:
                macd_diff['1'] = 0.5
                macd_diff['0'] = 1 - macd_diff['1']
            else:
                macd_diff['1'] = num_pump/(num_pump+num_not_pump)
                macd_diff['0'] = 1 - macd_diff['1']
            
            stochastic_val = var['stochastic']
            stochastic_signal_val = var['stochastic_signal']
            band_line = 2.5
            band_signal = 2.5
            stochastic_line_signal = {}
            temp = df_combine.loc[(df_combine['stochastic'] >= stochastic_val - band_line) &
                                (df_combine['stochastic'] <= stochastic_val + band_line) &
                                (df_combine['stochastic_signal'] >= stochastic_signal_val - band_signal) &
                                (df_combine['stochastic_signal'] <= stochastic_signal_val + band_signal)]
            num_pump = weight_data_pump*sum(temp['is_pump'])
            num_not_pump = len(temp['is_pump'])-sum(temp['is_pump'])
            if num_pump+num_not_pump == 0:
                stochastic_line_signal['1'] = 0.5
                stochastic_line_signal['0'] = 1 - stochastic_line_signal['1']
            else:
                stochastic_line_signal['1'] = num_pump/(num_pump+num_not_pump)
                stochastic_line_signal['0'] = 1 - stochastic_line_signal['1']
            
            rsi_val = var['rsi_val']
            band = 2.5
            rsi = {}
            num_pump = weight_data_pump*len(df_data_pump.loc[(df_data_pump['rsi_val'] >= rsi_val - band) & (df_data_pump['rsi_val'] <= rsi_val + band)])
            num_not_pump = len(df_data_not_pump.loc[(df_data_not_pump['rsi_val'] >= rsi_val - band) & (df_data_not_pump['rsi_val'] <= rsi_val + band)])
            if num_pump+num_not_pump == 0:
                rsi['1'] = 0.5
                rsi['0'] = 1 - rsi['1']
            else:
                rsi['1'] = num_pump/(num_pump+num_not_pump)
                rsi['0'] = 1 - rsi['1']
            
            coef_corr_val = var['coef_corr']
            slope_btc_val = var['last_slope_btc']
            band_corr = 0.05
            band_slope = 0.25
            corr_slope_btc = {}
            temp = df_combine.loc[(df_combine['coef_corr'] >= coef_corr_val - band_corr) &
                                (df_combine['coef_corr'] <= coef_corr_val + band_corr) &
                                (df_combine['last_slope_btc'] >= slope_btc_val - band_slope) &
                                (df_combine['last_slope_btc'] <= slope_btc_val + band_slope)]
            num_pump = weight_data_pump*sum(temp['is_pump'])
            num_not_pump = len(temp['is_pump'])-sum(temp['is_pump'])
            if num_pump+num_not_pump == 0:
                corr_slope_btc['1'] = 0.5
                corr_slope_btc['0'] = 0.5
            else:
                corr_slope_btc['1'] = num_pump/(num_pump+num_not_pump)
                corr_slope_btc['0'] = 1 - corr_slope_btc['1']
            
            arr_prob_last_slope.append(last_slope['1'])
            arr_prob_macd.append(macd_line_signal['1'])
            arr_prob_macd_diff.append(macd_diff['1'])
            arr_prob_stochastic.append(stochastic_line_signal['1'])
            arr_prob_rsi.append(rsi['1'])
            arr_prob_corr_btc.append(corr_slope_btc['1'])

        current_technical['prob_last_slope'] = arr_prob_last_slope
        current_technical['prob_macd'] = arr_prob_macd
        current_technical['prob_macd_diff'] = arr_prob_macd_diff
        current_technical['prob_stochastic'] = arr_prob_stochastic
        current_technical['prob_rsi'] = arr_prob_rsi
        current_technical['prob_corr_btc'] = arr_prob_corr_btc

        self.data_probability = pd.DataFrame({'last_calculation': current_technical['last_calculation'],
                                              'market': current_technical['market']})
        self.data_probability['prob_last_slope']  = current_technical['prob_last_slope'] 
        self.data_probability['prob_macd'] = current_technical['prob_macd']
        self.data_probability['prob_macd_diff']  = current_technical['prob_macd_diff'] 
        self.data_probability['prob_stochastic'] = current_technical['prob_stochastic']
        self.data_probability['prob_rsi']  = current_technical['prob_rsi'] 
        self.data_probability['prob_corr_btc'] = current_technical['prob_corr_btc']
        col = self.data_probability.loc[: , "prob_last_slope":"prob_corr_btc"]
        self.data_probability['avg'] = col.mean(axis=1)
        model = PandasModel(self.data_probability)
        self.tableView = QTableView()
        self.tableView.setModel(model)
        header = self.tableView.horizontalHeader()
        for i in range(len(self.data_probability.columns)):
            header.setSectionResizeMode(i, QHeaderView.ResizeMode.ResizeToContents)

        layout.addWidget(self.tableView)
        
        self.predict_btn = QPushButton()
        self.predict_btn.setText('Predict Ranking')
        layout.addWidget(self.predict_btn)
        self.predict_btn.clicked.connect(self.predict)

        self.retrain_btn = QPushButton()
        self.retrain_btn.setText('Retrain Model')
        layout.addWidget(self.retrain_btn)

        self.download_btn = QPushButton()
        self.download_btn.setText('Download Data')
        layout.addWidget(self.download_btn)
        self.download_btn.clicked.connect(self.download_data)


    def predict(self):
        logreg_model = joblib.load("logreg_model.joblib")
        X = self.data_probability[['prob_last_slope','prob_macd','prob_macd_diff','prob_stochastic','prob_rsi','prob_corr_btc']]
        logreg_pred = logreg_model.predict_proba(X)
        self.data_probability['logreg_proba'] = logreg_pred[:,1]
        rf_model = joblib.load("rf_model.joblib")
        rf_pred = rf_model.predict_proba(X)
        self.data_probability['rf_proba'] = rf_pred[:,1]
        self.data_probability['logreg_rf_combine'] = (self.data_probability['logreg_proba']+self.data_probability['rf_proba'])/2
        self.sorted_data_probability = self.data_probability.sort_values(by=['logreg_rf_combine'],ascending=False)
        model = PandasModel(self.sorted_data_probability)
        self.tableView.setModel(model)
        header = self.tableView.horizontalHeader()
        for i in range(len(self.data_probability.columns)):
            header.setSectionResizeMode(i, QHeaderView.ResizeMode.ResizeToContents)

    def download_data(self):
        try:
            now = datetime.now()
            str_now = now.strftime('%d_%m_%Y')
            filename = 'data_probability_' + str_now + '.csv'
            self.sorted_data_probability.to_csv(filename)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Information)
            # msg.setText("Success")
            msg.setInformativeText('Download Data Successful.')
            msg.setWindowTitle("Download Data")
            msg.exec()
        except AttributeError as ae:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Critical)
            # msg.setText("Success")
            msg.setInformativeText('Please predict coin ranking first.')
            msg.setWindowTitle("Download Data")
            msg.exec()