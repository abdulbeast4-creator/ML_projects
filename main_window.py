from PyQt5.QtWidgets import *
import sys
import upload_your_data 
import train_your_model
import display_scores_in_table 
import display_learning_curve 


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(150,150,450,450)
        self.setWindowTitle('AutoML')

        #stack widget
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.model_trainer = train_your_model.train_the_model(x=None,y=None,stacked_widget=self.stacked_widget)

        # Pages
        self.page_1 = upload_your_data.Upload_page(self.stacked_widget,main_window=self)
        self.stacked_widget.addWidget(self.page_1)
        self.page_2 = display_scores_in_table.Score_Table(self.stacked_widget,main_window=self)
        self.stacked_widget.addWidget(self.page_2)
        #self.page_3 = Learning_Rate(self.stacked_widget,self.page_1)
        #self.stacked_widget.addWidget(self.page_3)

         # Ensure the first page is visible
        self.stacked_widget.setCurrentWidget(self.page_1)
        self.setStyleSheet("background-color:white;color:black;")
    
        self.show()




def main():
    app = QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
