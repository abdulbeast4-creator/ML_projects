from sklearn.model_selection import train_test_split,cross_val_score
from display_scores_in_table import Score_Table

class train_the_model:
    def __init__(self,x,y,stacked_widget,main_window=None):
        self.x = x
        self.y = y
        self.stacked_widget = stacked_widget
        self.main_window = main_window
        
    def getting_model_from_page_2(self,basic_class_model):
        self.classi_models = basic_class_model

    def train_test_split_data(self):
        self.model_scores = {}
        x_train,x_test,y_train,y_test = train_test_split(self.x,self.y,test_size=0.3,random_state=42)
        for self.i,self.j in self.classi_models.items():
            #train_test_split
            self.j.fit(x_train,y_train)
            score_model = self.j.score(x_test,y_test)
            #cross validation score
            model_score_cross_val = cross_val_score(self.j,self.x,self.y,cv=5)
            self.model_scores[self.i] = (score_model,model_score_cross_val.mean())

        #Score_Table(self.stacked_widget,self.model_scores)
        self.page_2 = Score_Table(self.stacked_widget, self.model_scores,model_trainer=self,main_window=self.main_window)
        self.stacked_widget.addWidget(self.page_2)
        self.stacked_widget.setCurrentWidget(self.page_2)
