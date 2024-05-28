from import_library import *

class add_case(QWidget):
    # def __init__(self,case_name):
    #     self.case_name = case_name

    def new_case(self):
        self.h_layout = QHBoxLayout(self)
        self.v1_layout = QVBoxLayout()
        self.v2_layout = QVBoxLayout()

        self.decline_corr_label = QLabel()
        self.decline_corr_label.setText('Decline Correlation')
        self.date_selection_label = QLabel()
        self.date_selection_label.setText('Date Selection')

        self.v1_layout.addWidget(self.decline_corr_label)
        self.v1_layout.addWidget(self.date_selection_label)

        self.decline_corr_combobox = QComboBox()
        self.decline_corr_combobox.addItem('Exponential')
        self.decline_corr_combobox.setEnabled(False)

        self.date_selection_combobox = QComboBox()
        self.date_selection_combobox.addItem('Range Date')
        self.date_selection_combobox.addItem('Last days')
        self.date_selection_combobox.addItem('Random data')

        self.v2_layout.addWidget(self.decline_corr_combobox)
        self.v2_layout.addWidget(self.date_selection_combobox)

        self.h_layout.addLayout(self.v1_layout)
        self.h_layout.addLayout(self.v2_layout)

        self.v1_widget = QWidget()
        self.v1_layout_0 = QVBoxLayout(self.v1_widget)
        self.initial_date_label = QLabel()
        self.initial_date_label.setText('Initial date')
        self.final_date_label = QLabel()
        self.final_date_label.setText('Final date')
        self.v1_layout_0.addWidget(self.initial_date_label)
        self.v1_layout_0.addWidget(self.final_date_label)

        self.v2_widget = QWidget()
        self.v2_layout_0 = QVBoxLayout(self.v2_widget)
        self.data_type = QComboBox()
        self.data_type.addItem('Number of days')
        # self.initial_date_label = QLabel()
        # self.initial_date_label.setText('Initial date')
        # self.final_date_label = QLabel()
        # self.final_date_label.setText('Final date')
        self.last_days_label = QLabel()
        self.last_days_label.setText('Last (days)')
        self.v2_layout_0.addWidget(self.initial_date_label)
        self.v2_layout_0.addWidget(self.final_date_label)
        self.v2_layout_0.addWidget(self.last_days_label)

        self.v1_layout.addWidget(self.v1_widget)
        self.v1_layout.addWidget(self.v2_widget)
        # self.initial_date_label = QLabel()
        # self.initial_date_label.setText('Initial date')
        # self.last_date_label = QLabel()
        # self.last_date_label.setText('Final date')
        
