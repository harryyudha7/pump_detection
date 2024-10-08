# Form implementation generated from reading ui file 'app_ui.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1824, 1026)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.process_flow_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.process_flow_btn.setGeometry(QtCore.QRect(0, 0, 51, 51))
        self.process_flow_btn.setDefault(False)
        self.process_flow_btn.setObjectName("process_flow_btn")
        self.summary_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.summary_btn.setGeometry(QtCore.QRect(0, 50, 51, 51))
        self.summary_btn.setObjectName("summary_btn")
        self.field_decline_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.field_decline_btn.setGeometry(QtCore.QRect(0, 100, 51, 51))
        self.field_decline_btn.setObjectName("field_decline_btn")
        self.main_frame = QtWidgets.QStackedWidget(parent=self.centralwidget)
        self.main_frame.setGeometry(QtCore.QRect(60, 10, 1741, 981))
        self.main_frame.setObjectName("main_frame")
        self.diagram_page = QtWidgets.QWidget()
        self.diagram_page.setObjectName("diagram_page")
        self.diagram_title_label = QtWidgets.QLabel(parent=self.diagram_page)
        self.diagram_title_label.setGeometry(QtCore.QRect(10, 10, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.diagram_title_label.setFont(font)
        self.diagram_title_label.setObjectName("diagram_title_label")
        self.main_frame.addWidget(self.diagram_page)
        self.field_decline_page = QtWidgets.QWidget()
        self.field_decline_page.setObjectName("field_decline_page")
        self.decline_analysis_title = QtWidgets.QLabel(parent=self.field_decline_page)
        self.decline_analysis_title.setGeometry(QtCore.QRect(10, 10, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.decline_analysis_title.setFont(font)
        self.decline_analysis_title.setObjectName("decline_analysis_title")
        self.get_data_btn = QtWidgets.QPushButton(parent=self.field_decline_page)
        self.get_data_btn.setGeometry(QtCore.QRect(10, 60, 91, 31))
        self.get_data_btn.setObjectName("get_data_btn")
        self.img_decline = QtWidgets.QGraphicsView(parent=self.field_decline_page)
        self.img_decline.setGeometry(QtCore.QRect(120, 60, 1461, 461))
        self.img_decline.setObjectName("img_decline")
        self.decline_calc_scroll = QtWidgets.QScrollArea(parent=self.field_decline_page)
        self.decline_calc_scroll.setGeometry(QtCore.QRect(30, 550, 381, 361))
        self.decline_calc_scroll.setWidgetResizable(True)
        self.decline_calc_scroll.setObjectName("decline_calc_scroll")
        self.decline_calc_widget = QtWidgets.QWidget()
        self.decline_calc_widget.setGeometry(QtCore.QRect(0, 0, 379, 359))
        self.decline_calc_widget.setObjectName("decline_calc_widget")
        self.decline_calc_label = QtWidgets.QLabel(parent=self.decline_calc_widget)
        self.decline_calc_label.setGeometry(QtCore.QRect(10, 10, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.decline_calc_label.setFont(font)
        self.decline_calc_label.setObjectName("decline_calc_label")
        self.add_case_btn = QtWidgets.QPushButton(parent=self.decline_calc_widget)
        self.add_case_btn.setGeometry(QtCore.QRect(10, 40, 91, 31))
        self.add_case_btn.setObjectName("add_case_btn")
        self.add_case_input = QtWidgets.QLineEdit(parent=self.decline_calc_widget)
        self.add_case_input.setGeometry(QtCore.QRect(120, 41, 221, 31))
        self.add_case_input.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        self.add_case_input.setInputMask("")
        self.add_case_input.setObjectName("add_case_input")
        self.decline_case = QtWidgets.QToolBox(parent=self.decline_calc_widget)
        self.decline_case.setGeometry(QtCore.QRect(20, 90, 321, 241))
        self.decline_case.setObjectName("decline_case")
        self.case_1 = QtWidgets.QWidget()
        self.case_1.setGeometry(QtCore.QRect(0, 0, 321, 181))
        self.case_1.setObjectName("case_1")
        self.label = QtWidgets.QLabel(parent=self.case_1)
        self.label.setGeometry(QtCore.QRect(10, 0, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.comboBox_2 = QtWidgets.QComboBox(parent=self.case_1)
        self.comboBox_2.setGeometry(QtCore.QRect(160, 0, 161, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.decline_case.addItem(self.case_1, "")
        self.case_2 = QtWidgets.QWidget()
        self.case_2.setGeometry(QtCore.QRect(0, 0, 321, 181))
        self.case_2.setObjectName("case_2")
        self.decline_case.addItem(self.case_2, "")
        self.decline_calc_scroll.setWidget(self.decline_calc_widget)
        self.main_frame.addWidget(self.field_decline_page)
        self.summary_page = QtWidgets.QWidget()
        self.summary_page.setObjectName("summary_page")
        self.summary_title = QtWidgets.QLabel(parent=self.summary_page)
        self.summary_title.setGeometry(QtCore.QRect(10, 10, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.summary_title.setFont(font)
        self.summary_title.setObjectName("summary_title")
        self.comboBox = QtWidgets.QComboBox(parent=self.summary_page)
        self.comboBox.setGeometry(QtCore.QRect(10, 50, 201, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.get_data_summary_btn = QtWidgets.QPushButton(parent=self.summary_page)
        self.get_data_summary_btn.setGeometry(QtCore.QRect(1630, 90, 75, 24))
        self.get_data_summary_btn.setObjectName("get_data_summary_btn")
        self.table_summary_btn = QtWidgets.QPushButton(parent=self.summary_page)
        self.table_summary_btn.setGeometry(QtCore.QRect(1524, 90, 101, 24))
        self.table_summary_btn.setObjectName("table_summary_btn")
        self.graphicsView = QtWidgets.QGraphicsView(parent=self.summary_page)
        self.graphicsView.setGeometry(QtCore.QRect(10, 140, 1691, 731))
        self.graphicsView.setObjectName("graphicsView")
        self.main_frame.addWidget(self.summary_page)
        self.table_summary = QtWidgets.QWidget()
        self.table_summary.setObjectName("table_summary")
        self.table_summary_title = QtWidgets.QLabel(parent=self.table_summary)
        self.table_summary_title.setGeometry(QtCore.QRect(10, 10, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.table_summary_title.setFont(font)
        self.table_summary_title.setObjectName("table_summary_title")
        self.table_summary_widget = QtWidgets.QTableWidget(parent=self.table_summary)
        self.table_summary_widget.setGeometry(QtCore.QRect(10, 50, 1711, 871))
        self.table_summary_widget.setObjectName("table_summary_widget")
        self.table_summary_widget.setColumnCount(0)
        self.table_summary_widget.setRowCount(0)
        self.main_frame.addWidget(self.table_summary)
        self.well_xx_properties = QtWidgets.QWidget()
        self.well_xx_properties.setObjectName("well_xx_properties")
        self.well_properties_title = QtWidgets.QLabel(parent=self.well_xx_properties)
        self.well_properties_title.setGeometry(QtCore.QRect(10, 10, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.well_properties_title.setFont(font)
        self.well_properties_title.setObjectName("well_properties_title")
        self.prod_data_group = QtWidgets.QGroupBox(parent=self.well_xx_properties)
        self.prod_data_group.setGeometry(QtCore.QRect(10, 60, 341, 871))
        self.prod_data_group.setObjectName("prod_data_group")
        self.table_prod_data = QtWidgets.QTableView(parent=self.prod_data_group)
        self.table_prod_data.setGeometry(QtCore.QRect(10, 20, 321, 841))
        self.table_prod_data.setObjectName("table_prod_data")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.well_xx_properties)
        self.groupBox_2.setGeometry(QtCore.QRect(360, 490, 1381, 441))
        self.groupBox_2.setObjectName("groupBox_2")
        self.graphicsView_3 = QtWidgets.QGraphicsView(parent=self.groupBox_2)
        self.graphicsView_3.setGeometry(QtCore.QRect(50, 60, 1281, 361))
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.normalize_btn = QtWidgets.QToolButton(parent=self.groupBox_2)
        self.normalize_btn.setGeometry(QtCore.QRect(1100, 30, 71, 22))
        self.normalize_btn.setObjectName("normalize_btn")
        self.table_result_btn = QtWidgets.QToolButton(parent=self.groupBox_2)
        self.table_result_btn.setGeometry(QtCore.QRect(1180, 30, 71, 22))
        self.table_result_btn.setObjectName("table_result_btn")
        self.calibrate_btn = QtWidgets.QToolButton(parent=self.groupBox_2)
        self.calibrate_btn.setGeometry(QtCore.QRect(1260, 30, 71, 22))
        self.calibrate_btn.setObjectName("calibrate_btn")
        self.tft_monitor_group = QtWidgets.QGroupBox(parent=self.well_xx_properties)
        self.tft_monitor_group.setGeometry(QtCore.QRect(359, 59, 681, 411))
        self.tft_monitor_group.setObjectName("tft_monitor_group")
        self.table_tft = QtWidgets.QTableView(parent=self.tft_monitor_group)
        self.table_tft.setGeometry(QtCore.QRect(10, 50, 661, 351))
        self.table_tft.setObjectName("table_tft")
        self.param_model_group = QtWidgets.QGroupBox(parent=self.well_xx_properties)
        self.param_model_group.setGeometry(QtCore.QRect(1050, 60, 691, 411))
        self.param_model_group.setObjectName("param_model_group")
        self.wellbore_tbl_btn = QtWidgets.QPushButton(parent=self.param_model_group)
        self.wellbore_tbl_btn.setGeometry(QtCore.QRect(570, 20, 101, 24))
        self.wellbore_tbl_btn.setObjectName("wellbore_tbl_btn")
        self.table_param_model = QtWidgets.QTableView(parent=self.param_model_group)
        self.table_param_model.setGeometry(QtCore.QRect(10, 50, 661, 351))
        self.table_param_model.setObjectName("table_param_model")
        self.main_frame.addWidget(self.well_xx_properties)
        self.separator_properties = QtWidgets.QWidget()
        self.separator_properties.setObjectName("separator_properties")
        self.separator_properties_title = QtWidgets.QLabel(parent=self.separator_properties)
        self.separator_properties_title.setGeometry(QtCore.QRect(10, 10, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.separator_properties_title.setFont(font)
        self.separator_properties_title.setObjectName("separator_properties_title")
        self.separator_data = QtWidgets.QGroupBox(parent=self.separator_properties)
        self.separator_data.setGeometry(QtCore.QRect(10, 50, 601, 881))
        self.separator_data.setObjectName("separator_data")
        self.table_separator_data = QtWidgets.QTableWidget(parent=self.separator_data)
        self.table_separator_data.setGeometry(QtCore.QRect(10, 30, 571, 841))
        self.table_separator_data.setObjectName("table_separator_data")
        self.table_separator_data.setColumnCount(0)
        self.table_separator_data.setRowCount(0)
        self.tft_monitoring = QtWidgets.QGroupBox(parent=self.separator_properties)
        self.tft_monitoring.setGeometry(QtCore.QRect(630, 50, 541, 441))
        self.tft_monitoring.setObjectName("tft_monitoring")
        self.table_tft_data = QtWidgets.QTableWidget(parent=self.tft_monitoring)
        self.table_tft_data.setGeometry(QtCore.QRect(20, 30, 501, 391))
        self.table_tft_data.setObjectName("table_tft_data")
        self.table_tft_data.setColumnCount(0)
        self.table_tft_data.setRowCount(0)
        self.main_frame.addWidget(self.separator_properties)
        self.injection_properties = QtWidgets.QWidget()
        self.injection_properties.setObjectName("injection_properties")
        self.injection_properties_title = QtWidgets.QLabel(parent=self.injection_properties)
        self.injection_properties_title.setGeometry(QtCore.QRect(20, 20, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.injection_properties_title.setFont(font)
        self.injection_properties_title.setObjectName("injection_properties_title")
        self.injection_data = QtWidgets.QGroupBox(parent=self.injection_properties)
        self.injection_data.setGeometry(QtCore.QRect(20, 70, 621, 891))
        self.injection_data.setObjectName("injection_data")
        self.table_injection_data = QtWidgets.QTableView(parent=self.injection_data)
        self.table_injection_data.setGeometry(QtCore.QRect(20, 30, 581, 841))
        self.table_injection_data.setObjectName("table_injection_data")
        self.main_frame.addWidget(self.injection_properties)
        self.steam_vessel_properties = QtWidgets.QWidget()
        self.steam_vessel_properties.setObjectName("steam_vessel_properties")
        self.steam_vessel_properties_title = QtWidgets.QLabel(parent=self.steam_vessel_properties)
        self.steam_vessel_properties_title.setGeometry(QtCore.QRect(20, 20, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.steam_vessel_properties_title.setFont(font)
        self.steam_vessel_properties_title.setObjectName("steam_vessel_properties_title")
        self.tft_monitoring_sv = QtWidgets.QGroupBox(parent=self.steam_vessel_properties)
        self.tft_monitoring_sv.setGeometry(QtCore.QRect(640, 60, 541, 441))
        self.tft_monitoring_sv.setObjectName("tft_monitoring_sv")
        self.table_tft_data_sv = QtWidgets.QTableWidget(parent=self.tft_monitoring_sv)
        self.table_tft_data_sv.setGeometry(QtCore.QRect(20, 30, 501, 391))
        self.table_tft_data_sv.setObjectName("table_tft_data_sv")
        self.table_tft_data_sv.setColumnCount(0)
        self.table_tft_data_sv.setRowCount(0)
        self.separator_data_2 = QtWidgets.QGroupBox(parent=self.steam_vessel_properties)
        self.separator_data_2.setGeometry(QtCore.QRect(20, 60, 601, 881))
        self.separator_data_2.setObjectName("separator_data_2")
        self.table_separator_data_2 = QtWidgets.QTableWidget(parent=self.separator_data_2)
        self.table_separator_data_2.setGeometry(QtCore.QRect(10, 30, 571, 841))
        self.table_separator_data_2.setObjectName("table_separator_data_2")
        self.table_separator_data_2.setColumnCount(0)
        self.table_separator_data_2.setRowCount(0)
        self.main_frame.addWidget(self.steam_vessel_properties)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1824, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.main_frame.setCurrentIndex(7)
        self.decline_case.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.process_flow_btn.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.process_flow_btn.setText(_translate("MainWindow", "Process Flow"))
        self.summary_btn.setText(_translate("MainWindow", "Summary"))
        self.field_decline_btn.setText(_translate("MainWindow", "Field Decline"))
        self.diagram_title_label.setText(_translate("MainWindow", "Process Flow Diagram"))
        self.decline_analysis_title.setText(_translate("MainWindow", "Field Decline Analysis"))
        self.get_data_btn.setText(_translate("MainWindow", "Get Data"))
        self.decline_calc_label.setText(_translate("MainWindow", "Decline Calculation"))
        self.add_case_btn.setText(_translate("MainWindow", "Add Case"))
        self.label.setText(_translate("MainWindow", "Decline Correlation"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Exponential"))
        self.decline_case.setItemText(self.decline_case.indexOf(self.case_1), _translate("MainWindow", "Page 1"))
        self.decline_case.setItemText(self.decline_case.indexOf(self.case_2), _translate("MainWindow", "Page 2"))
        self.summary_title.setText(_translate("MainWindow", "Summary"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Separator-1"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Separator-2"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Separator-3"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Vessel"))
        self.get_data_summary_btn.setText(_translate("MainWindow", "Get Data"))
        self.table_summary_btn.setText(_translate("MainWindow", "Table Summary"))
        self.table_summary_title.setText(_translate("MainWindow", "Table Summary"))
        self.well_properties_title.setText(_translate("MainWindow", "Well-XX Data Properties"))
        self.prod_data_group.setTitle(_translate("MainWindow", "Production Data"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Chart"))
        self.normalize_btn.setText(_translate("MainWindow", "Normalize"))
        self.table_result_btn.setText(_translate("MainWindow", "Table Result"))
        self.calibrate_btn.setText(_translate("MainWindow", "Calibrate"))
        self.tft_monitor_group.setTitle(_translate("MainWindow", "TFT Monitoring"))
        self.param_model_group.setTitle(_translate("MainWindow", "Parameters Model"))
        self.wellbore_tbl_btn.setText(_translate("MainWindow", "Wellbore Table"))
        self.separator_properties_title.setText(_translate("MainWindow", "Separator-X Properties"))
        self.separator_data.setTitle(_translate("MainWindow", "Separator Data"))
        self.tft_monitoring.setTitle(_translate("MainWindow", "TFT Monitoring"))
        self.injection_properties_title.setText(_translate("MainWindow", "Injector-X Data Properties"))
        self.injection_data.setTitle(_translate("MainWindow", "Injection Data"))
        self.steam_vessel_properties_title.setText(_translate("MainWindow", "Steam Vessel Data Properties"))
        self.tft_monitoring_sv.setTitle(_translate("MainWindow", "TFT Monitoring"))
        self.separator_data_2.setTitle(_translate("MainWindow", "Production Data"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
