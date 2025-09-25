from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from variable_x_y import Data_x_y
from display_learning_curve import Learning_Rate
#from main_window import MainWindow

class Score_Table(QWidget):
    def __init__(self, stacked_widget, model_scores=None, model_trainer=None, main_window=None):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.model_scores = model_scores
        self.model_trainer = model_trainer
        self.main_window = main_window
        self.setWindowTitle('Model Score')
        self.setGeometry(150, 150, 350, 350)

        self.UI_table()
    
    def UI_table(self):
        # Initialize the table first
        self.table_1 = QTableWidget()
        main_layout = QVBoxLayout()
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()

        # Widgets
        self.High_Score_algo = QLabel('Waiting.....')
        self.High_Score_algo_cv = QLabel('Waiting.....')

        # Button to check the learning rate
        self.learning_rate_btn = QPushButton('Learning Rate')
        self.learning_rate_btn.setStyleSheet('''
            QPushButton {
                background-color: #FFD700;
                color: white;
                font-size: 21px;
                font-weight: bold;
                padding: 10px 20px;
                border-radius: 18px;
                border: 2px solid #FFD700;
            }
            QPushButton:hover {
                background-color: white;
                color: black;
                border: 2px solid #FFD700;
            }
        ''')
        self.learning_rate_btn.setFixedSize(280, 50)
        self.learning_rate_btn.clicked.connect(self.clicked_learning_btn)

        if self.model_scores:
            self.table_1.setRowCount(len(self.model_scores))
            self.table_1.setColumnCount(3)
            self.table_1.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
            self.table_1.setHorizontalHeaderLabels(['Model', 'train_test_split', 'Cross-Validation'])

            for row_index, (model_name, score) in enumerate(self.model_scores.items()):
                tts_score, cv_score = score
                try:
                    self.table_1.setItem(row_index, 0, QTableWidgetItem(model_name))
                    self.table_1.setItem(row_index, 1, QTableWidgetItem(str(round(tts_score, 3))))
                    self.table_1.setItem(row_index, 2, QTableWidgetItem(str(round(cv_score, 3))))
                    
                    self.best_model_name = max(self.model_scores.items(), key=lambda item: item[1][0])[0]
                    best_train_score = max(self.model_scores.items(), key=lambda item: item[1][0])[1][0]
                    self.High_Score_algo.setText(f"Model: {str(self.best_model_name)}| train_test_split: {round(best_train_score, 3)}")
                    best_model_cv = max(self.model_scores.items(), key=lambda item: item[0][1])[0]
                    best_cv_score = max(self.model_scores.items(), key=lambda item: item[0][1])[1][1]
                    self.High_Score_algo_cv.setText(f"Model: {str(best_model_cv)}| cross_val_score: {round(best_cv_score, 3)}")
                except Exception as e:
                    print(f"Error at row {row_index}: {e}")
        else:
            self.table_1.setRowCount(1)
            self.table_1.setColumnCount(1)
            self.table_1.setHorizontalHeaderLabels(['Info'])
            self.table_1.setItem(0, 0, QTableWidgetItem("No models trained yet."))

        main_layout.addWidget(self.table_1, alignment=Qt.AlignTop | Qt.AlignCenter)
        hbox1.addWidget(self.High_Score_algo)
        hbox1.addWidget(self.High_Score_algo_cv)
        hbox2.addWidget(self.learning_rate_btn)
        main_layout.addLayout(hbox1)
        main_layout.addLayout(hbox2)
        self.setLayout(main_layout)

    def clicked_learning_btn(self):
        best_model_name = getattr(self, 'best_model_name', None)
        print(f"Clicked Learning Rate button. best_model_name: {best_model_name}")
        print(f"Model Trainer stored in Score_Table: {self.model_trainer is not None}")
        if self.model_trainer:
            print(f"Classi Models in Model Trainer: {hasattr(self.model_trainer, 'classi_models')}")
            if hasattr(self.model_trainer, 'classi_models'):
                print(f"Keys in classi_models: {self.model_trainer.classi_models.keys()}")

        selected_model = None
        if best_model_name and self.model_trainer and hasattr(self.model_trainer, 'classi_models') and best_model_name in self.model_trainer.classi_models:
            selected_model = self.model_trainer.classi_models[best_model_name]
            print(f"Found model in model_trainer: {selected_model}")
        else:
            QMessageBox.warning(self, "Error", "Could not retrieve the selected model for learning curve.")
            return

        # Create Learning_Rate widget and pass main_window
        self.page_3 = Learning_Rate(self.stacked_widget, Data_x_y.x, Data_x_y.y, model=selected_model, get_main_window=self.main_window)
        self.stacked_widget.addWidget(self.page_3)
        self.stacked_widget.setCurrentWidget(self.page_3)