from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from sklearn.model_selection import learning_curve
import numpy as np
from matplotlib.figure import Figure
import matplotlib.pyplot as plt  # Import the pyplot module

class Learning_Rate(QWidget):
    def __init__(self, stacked_widget, x=None, y=None, model=None, get_main_window=None):
        super().__init__()
        self.x_data = x
        self.y_data = y
        self.model = model
        self.stacked_widget = stacked_widget
        self.main_window = get_main_window

        # Hide the MainWindow
        if self.main_window:
            print("Hiding MainWindow:", self.main_window)
            self.main_window.hide()
        else:
            print("Warning: MainWindow is None")

        self.setup_ui()
        self.show()  # Ensure the widget is shown

    def setup_ui(self):
        main_layout = QVBoxLayout()

        # Back button
        self.back_btn = QPushButton('Back')
        self.back_btn.setStyleSheet('''
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
        self.back_btn.setFixedSize(280, 50)
        self.back_btn.clicked.connect(self.go_back)

        # Compute learning curve
        self.train_sizes = self.train_score_mean = self.train_score_std = []
        self.test_score_mean = self.test_score_std = []
        if self.model and self.x_data is not None and self.y_data is not None:
            try:
                self.train_sizes, self.train_scores, self.test_scores = learning_curve(
                    self.model, self.x_data, self.y_data, scoring='accuracy', cv=5,
                    train_sizes=np.linspace(0.1, 1.0, 10), random_state=42
                )
                self.train_score_mean = np.mean(self.train_scores, axis=1)
                self.train_score_std = np.std(self.train_scores, axis=1)
                self.test_score_mean = np.mean(self.test_scores, axis=1)
                self.test_score_std = np.std(self.test_scores, axis=1)
                self.plot_learning_curve_separate_window()
            except Exception as e:
                print(f"Error computing learning curve: {e}")
                QMessageBox.critical(self, "Learning Curve Error", f"An error occurred during learning curve calculation: {str(e)}")
        else:
            print("Model or data missing, skipping learning curve")
            self.plot_learning_curve_separate_window() # Still call to display 'No data' message

        self.setLayout(main_layout)


    def plot_learning_curve_separate_window(self):
        plt.figure(figsize=(6, 4), dpi=100)
        if self.train_sizes.size > 0:
            plt.plot(self.train_sizes, self.train_score_mean, label='Training Score', color='blue', marker='o')
            plt.fill_between(
                self.train_sizes,
                self.train_score_mean - self.train_score_std,
                self.train_score_mean + self.train_score_std,
                color='blue', alpha=0.1
            )
            plt.plot(self.train_sizes, self.test_score_mean, label='Validation Score', color='green', marker='o')
            plt.fill_between(
                self.train_sizes,
                self.test_score_mean - self.test_score_std,
                self.test_score_mean + self.test_score_std,
                color='green', alpha=0.1
            )
            plt.title('Learning Curve')
            plt.xlabel('Training Set Size')
            plt.ylabel('Accuracy')
            plt.legend(loc='best')
            plt.grid()
            plt.show()  # This will open the plot in a new Matplotlib window

            # Close the PyQt5 main window after the plot is shown
            if self.main_window:
                self.main_window.close()
        else:
            plt.title('No Data for Learning Curve')
            plt.xlabel('Training Set Size')
            plt.ylabel('Accuracy')
            plt.grid()
            plt.show()
            if self.main_window:
                self.main_window.close()

    def go_back(self):
        if self.main_window:
            print("Showing MainWindow:", self.main_window)
            self.main_window.show()
        self.stacked_widget.setCurrentIndex(self.stacked_widget.currentIndex() - 1)