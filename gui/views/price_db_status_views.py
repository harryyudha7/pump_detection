import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QVBoxLayout, QWidget, QHeaderView, QTableView, QProgressBar, QPushButton, QMessageBox, QRadioButton, QTextEdit
from PyQt6.QtCore import Qt, QSize, QPoint
from PyQt6.QtGui import QIcon, QPixmap, QFont, QPolygon
from PyQt6 import QtCore
import numpy as np
import pandas as pd
from datetime import datetime
import ccxt
from tqdm import tqdm

from views.sql_function import SQL_function
    
class PandasModel(QtCore.QAbstractTableModel): 
    def __init__(self, df = pd.DataFrame(), parent=None): 
        QtCore.QAbstractTableModel.__init__(self, parent=parent)
        self._df = df

    def headerData(self, section, orientation, role=QtCore.Qt.ItemDataRole.DisplayRole):
        if role != QtCore.Qt.ItemDataRole.DisplayRole:
            return QtCore.QVariant()

        if orientation == QtCore.Qt.Orientation.Horizontal:
            try:
                return self._df.columns.tolist()[section]
            except (IndexError, ):
                return QtCore.QVariant()
        elif orientation == QtCore.Qt.Orientation.Vertical:
            try:
                # return self.df.index.tolist()
                return self._df.index.tolist()[section]
            except (IndexError, ):
                return QtCore.QVariant()

    def data(self, index, role=QtCore.Qt.ItemDataRole.DisplayRole):
        if role != QtCore.Qt.ItemDataRole.DisplayRole:
            return QtCore.QVariant()

        if not index.isValid():
            return QtCore.QVariant()

        return QtCore.QVariant(str(self._df.iloc[index.row(), index.column()]))

    def setData(self, index, value, role):
        row = self._df.index[index.row()]
        col = self._df.columns[index.column()]
        if hasattr(value, 'toPyObject'):
            # PyQt4 gets a QVariant
            value = value.toPyObject()
        else:
            # PySide gets an unicode
            dtype = self._df[col].dtype
            if dtype != object:
                value = None if value == '' else dtype.type(value)
        self._df.set_value(row, col, value)
        return True

    def rowCount(self, parent=QtCore.QModelIndex()): 
        return len(self._df.index)

    def columnCount(self, parent=QtCore.QModelIndex()): 
        return len(self._df.columns)

    def sort(self, column, order):
        colname = self._df.columns.tolist()[column]
        self.layoutAboutToBeChanged.emit()
        self._df.sort_values(colname, ascending= order == QtCore.Qt.AscendingOrder, inplace=True)
        self._df.reset_index(inplace=True, drop=True)
        self.layoutChanged.emit()

class price_db_ui(QWidget):
    def setup_ui(self):

        layout = QVBoxLayout()
        # layout.addWidget(self.text_place)
        self.setLayout(layout)

        db = 'crypto_db'
        pw = '27111998'
        self.connection = SQL_function.create_db_connection("localhost", "root", pw, db)

        query = 'SHOW TABLES'
        cur = SQL_function.execute_query(self.connection,query)
        res = cur.fetchall()
        list_tbl = [i[0] for i in res]
        # list_tbl = list_tbl[:20]

        self.last_update = []
        self.remarks = []
        self.cur_ts = datetime.timestamp(datetime.today())
        for i in tqdm(list_tbl):
            query = "select * from %s order by timestamp desc limit 2;" % i
            cur = SQL_function.execute_query(self.connection,query)
            res = cur.fetchall()
            ts = [i[0] for i in res]
            if len(ts) == 0:
                last_ts = datetime.timestamp(datetime(1980, 1, 1, 7, 0, 0))*1000
            else: 
                last_ts = max(ts)
            # print(last_ts/1000, cur_ts)
            if self.cur_ts - last_ts/1000 > 7*24*3600:
                self.remarks.append('Database not up to date.')
            else:
                self.remarks.append('Database is up to date.')
            self.last_update.append(datetime.fromtimestamp(last_ts/1000))

        self.df_table = pd.DataFrame({"table": list_tbl,
                                 "last_update": self.last_update,
                                 "remarks": self.remarks})
        
        self.df_table_sorted = self.df_table.sort_values(by=['last_update','table'])

        model = PandasModel(self.df_table_sorted)
        self.tableView = QTableView()
        self.tableView.setModel(model)
        header = self.tableView.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)
        # header.setSectionResizeMode(3, QHeaderView.ResizeMode.ResizeToContents)
        layout.addWidget(self.tableView)

        self.update_btn = QPushButton()
        self.update_btn.setText('Update Database')
        layout.addWidget(self.update_btn)

        self.progress = QProgressBar()
        layout.addWidget(self.progress)
        
        exchange_id = 'tokocrypto'
        exchange_class = getattr(ccxt, exchange_id)
        self.exchange = exchange_class({
            'apiKey': 'YOUR_API_KEY',
            'secret': 'YOUR_SECRET',
        })

        markets = self.exchange.load_markets()
        market_list = list(markets.keys())

        considered_market = []
        for i in market_list:
            if '/USDT' in i or '/BTC' in i:
                considered_market.append(i)

        self.existing_market = self.df_table['table']

        self.update_btn.clicked.connect(self.update_db)

    def update_db(self):
        for i in range(0,len(self.existing_market)):
            try:
                self.progress.setValue(int((i+1)/len(self.existing_market)*100))
                market = self.existing_market[i]
                # market = market.replace('/', '')
                # print(market)
                # query = 'SELECT * FROM %s ORDER BY timestamp ASC' % market
                # cur = execute_query(self.connection,query)
                # res = cur.fetchall()
                # df = pd.DataFrame(res,columns=['timestamp', 'open','high', 'low','close','volume'])
                # df = df.drop_duplicates()
                # if not df.empty:
                # init_time0 = 0
                init_time_dt = self.df_table['last_update'].iloc[i]
                init_time = datetime.timestamp(init_time_dt)*1000
                init_time0 = 0
                final_time = self.cur_ts*1000
                print(market)
                # iter = 0
                # print(init_time, init_time0, final_time)
                while init_time < final_time and init_time0 != init_time:
                    if 'usdt' in market:
                        market_slash = market.replace('usdt','/usdt')
                    elif market[-3:] == 'btc':
                        market_slash = market.replace('btc','/btc')
                    test = self.exchange.fetch_ohlcv (market_slash.upper(), '1h',since=int(init_time),limit=1000)
                    init_time0 = init_time
                    init_time = test[-1][0]
                    test = [tuple(j) for j in test]
                    query_string = 'INSERT INTO ' + market + ' (timestamp, open, high, low, close, volume) VALUES (%s,%s,%s,%s,%s,%s)'
                    SQL_function.executemany_query(self.connection,query_string,test)
                self.last_update[i] = datetime.fromtimestamp(init_time/1000)
                if abs(final_time - init_time) < 3*24*3600*1000:
                    self.remarks[i] = 'Database is up to date.'
                else:
                    self.remarks[i] = 'Database is not up to date.'
                # print(self.remarks[i])
                    # connection.commit()

            except ccxt.NetworkError as ne:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Icon.Critical)
                msg.setText("Error")
                msg.setInformativeText('Please activate your VPN.')
                msg.setWindowTitle("Error")
                msg.exec()
                break
            except KeyError as ke:
                self.remarks[i] = 'Cannot update database.'
            except Exception as e:
                print(e)
                self.remarks[i] = e
        self.df_table['remarks'] = self.remarks
        self.df_table['last_update'] = self.last_update
        self.df_table_sorted = self.df_table.sort_values(by=['last_update','table'])
        model = PandasModel(self.df_table_sorted)
        self.tableView.setModel(model)