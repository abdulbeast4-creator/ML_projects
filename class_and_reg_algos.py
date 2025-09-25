# Basic Classification Algorithm
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import  DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import BernoulliNB

# Basic Regression Algorithm 
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor



class Algorithms:
    def __init__(self,model_trainer):
        self.model_trainer = model_trainer
        print(self.model_trainer)
        self.Classification_Algos()

    def Classification_Algos(self):
        self.basic_class_models={
        'Logistic Regression' : LogisticRegression(max_iter=3500),
        'Support Vector Machine' : SVC(),
        'Random Forest Classifier ': RandomForestClassifier(),
        'Decision Tree Classifier' : DecisionTreeClassifier(),
        'K-Nearest Neighbors' : KNeighborsClassifier(),
        'GaussianNB' : GaussianNB(),
        'MultiNominalNB' : MultinomialNB(),
        'BernoulliNB' : BernoulliNB()
                    }
       
        self.model_trainer.getting_model_from_page_2(basic_class_model=self.basic_class_models)

        

    """def for_check_algorithm_in_models(self):
        for index,(i,j) in enumerate(self.basic_class_models.items()):
            if self.show_learning_rate  == i:
                print(self.basic_class_models[i,j])"""
