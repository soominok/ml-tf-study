import os

from com_titanic_com.util.file_handler import FileReader
import pandas as pd
import numpy as np
from sklearn.ensemble import ReandomForestClassifier # rforest
from sklearn.tree import DecisionTreeClassifier # dtree
from sklearn.naive_bayes import GaussianNB # nb
from sklearn.neighbors import KNeighborsClassifier # knn
from sklearn.svm import SVC # svm
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold # k value is understood as count
from sklearn.model_selection import cross_val_score

from pathlib import pathlib
# dtree, rforest, nb, knn, svm

"""
context: /usr/proj/kaggle
fname: 
PassengerId
Survived: The answer that a machine learning model should match 
Pclass: Boarding Pass 1 = 1st-class seat, 2 = 2nd, 3 = 3rd,
Name,
Sex,
Age,
SibSp accompanying brothers, sisters, spouses
Parch accompanying parents, children,
Ticket : Ticket Number
Fare : Boarding Charges
Cabin : Room number
Embarked : a Port Name on Board C = Cherbourg, Q = Queenstown, S = Southhampton
"""

class UserService:
    def __init__(self):
        self.fileReader = FileReader()
        self.data = os.path.abspath("data") # 특정 경로에 대해 절대 경로 얻기

        self.odf = None

    def hook(self):
        train = 'train.csv'
        test = 'test.csv'
        this = self.fileReader
        this.train = self.new_model(train) # payload
        this.test = self.new_model(test) # payload

        self.odf = pd.DataFrame(
            {
                'userid' : this.train.PassengerId,
                'password' : '1',
                'name' : this.train.Name
            }
        )

        this.id = this.test['PassengerId']
        print(f'Preprocessing Train Variable : {this.train.columns}')
