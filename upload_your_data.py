from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import pandas as pd
from train_your_model import *
from class_and_reg_algos import Algorithms
from display_scores_in_table import Score_Table
from variable_x_y import Data_x_y


class Upload_page(QWidget):
    def __init__(self,stacked_widget,main_window=None):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.main_window = main_window

        self.UI()

    def UI(self):
        '''layout'''
        vbox = QVBoxLayout()
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()

        '''Label for location'''
        self.label_location = QLabel('File Not Choosen')
        self.label_location.setStyleSheet('''QLabel{
                                          color:white;
                                          font-size:16px;
                                          }''')

        '''Button upload csv'''
        upload_csv = QPushButton('upload csv')
        upload_csv.setStyleSheet('''
            QPushButton {
                background-color: #FFD700;  /* Yellow */
                color: white;
                font-size: 21px;
                font-weight: bold;
                padding: 10px 20px;  /* More space */
                border-radius: 18px;  /* Curved edges */
                border: 2px solid #FFD700;  /* Border matching button color */
            }
            QPushButton:hover {
                background-color: white;
                color: black;
                border: 2px solid #FFD700;
            }
        ''')
        upload_csv.clicked.connect(self.user_data_file)
        upload_csv.setFixedSize(280,50)
        upload_csv.move(150,50)

        #table widget
        self.table = QTableWidget()
        self.table.setColumnCount(0)
        self.table.setRowCount(0)
        #self.table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        #Select output variable button
        self.outvar = QPushButton('Output Variable')
        self.outvar.clicked.connect(self.enable_combo_for_choose_output_variable)
        self.outvar.setStyleSheet('''
            QPushButton {
                background-color: #FFD700;  /* Yellow */
                color: white;
                font-size: 21px;
                font-weight: bold;
                padding: 10px 20px;  /* More space */
                border-radius: 18px;  /* Curved edges */
                                  
                border: 2px solid black;
                                  }
                                  
            QPushButton:hover {
                background-color: white;
                color: black;
                border: 2px solid #FFD700;
            }
        ''')
        self.outvar.setFixedSize(280,50)
        self.outvar.move(150,50)
        self.outvar.hide()

        #select output variable combo -box
        self.select_output_var_cb = QComboBox()
        self.select_output_var_cb.hide()

        #train your model button
        self.train_your_model = QPushButton('Train Your Model')
        self.train_your_model.setStyleSheet('''
            QPushButton {
                background-color: #FFD700;  /* Yellow */
                color: white;
                font-size: 21px;
                font-weight: bold;
                padding: 10px 20px;  /* More space */
                border-radius: 18px;  /* Curved edges */
                border: 2px solid #FFD700;  /* Border matching button color */
            }
            QPushButton:hover {
                background-color: white;
                color: black;
                border: 2px solid #FFD700;
            }
        ''')
        self.train_your_model.setFixedSize(280,50)
        self.train_your_model.hide()

        hbox1.addWidget(self.label_location)
        vbox.addLayout(hbox1)
        vbox.addStretch(1)  # Push the button down
        vbox.addWidget(upload_csv, alignment=Qt.AlignCenter)
        vbox.addStretch(2)  # Push further down
        vbox.addWidget(self.table, stretch=14)

        vbox.addWidget(self.outvar,alignment=Qt.AlignCenter)
        vbox.addWidget(self.select_output_var_cb)
        vbox.addWidget(self.train_your_model,alignment=Qt.AlignCenter)

        self.setLayout(vbox)

    def user_data_file(self):
        file_dialog_result= QFileDialog.getOpenFileName(self,'open your dataset', "", "CSV Files (*.csv);;All Files (*)")
        file_path= file_dialog_result[0]
        if not file_path:
            return
        
        self.label_location.setText(file_path)
        try:
            #df = pd.read_csv(file_path)
            if file_path:
                self.label_location.setText(f'File :{file_path}')
                print("File selected: ",file_path)
                self.data = pd.read_csv(file_path)
                self.show_table()

        except Exception as e:
            QMessageBox.warning(self,'Error',f"failed to upload csv :{str(e)}")

    def show_table(self):
        self.table.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

        if self.data is not None:
            row,columns = self.data.shape
            self.table.setRowCount(row)
            self.table.setColumnCount(columns)
            self.table.setHorizontalHeaderLabels(self.data.columns)

            for rows in range(row):
                for cols in range(columns):
                    item = QTableWidgetItem(str(self.data.iloc[rows,cols]))
                    self.table.setItem(rows,cols,item)


            self.outvar.show()


    def enable_combo_for_choose_output_variable(self):
        #combo box add and show
        self.select_output_var_cb.addItems(self.data.columns)
        self.select_output_var_cb.show()


        #Train your model button
        self.train_your_model.show()
        self.train_your_model.clicked.connect(self.spliting_data_output_var)

    def spliting_data_output_var(self):
        self.x_var = self.data.drop(self.select_output_var_cb.currentText(),axis=1)
        self.y_var = self.data[self.select_output_var_cb.currentText()]

        #storing the x and y variable in another specific class
        Data_x_y(self.x_var,self.y_var)
        

        self.model_trainer = train_the_model(self.x_var,self.y_var,self.stacked_widget,main_window=self.main_window)
        Algorithms(self.model_trainer)
        self.model_trainer.train_test_split_data()
        