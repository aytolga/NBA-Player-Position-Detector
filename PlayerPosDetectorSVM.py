import pandas as pd
import numpy as np

"""
The model can predict NBA Players Position
Which is based on ML algorithm SVM.


Author: Tolga AY
aytolga@outlook.com

"""

def clean_dataset(df):
    #In this function the NaN values is preprocessing.
    assert isinstance(df, pd.DataFrame)
    df.dropna(inplace=True)
    indices_to_keep = ~df.isin([np.nan, np.inf, -np.inf]).any(1)
    return df[indices_to_keep].astype(np.float64)

data = pd.read_csv("players_stats.csv")

data = data[['Pos','FG%','FT%','3P%','REB','AST','BLK','Height','Weight']]

data = data.replace(to_replace='C',value = '5')
data = data.replace(to_replace='PF',value = '4')
data = data.replace(to_replace='SF',value = '3')    #Data operations for SVM
data = data.replace(to_replace='SG',value = '2')
data = data.replace(to_replace='PG',value = '1')

clean_dataset(data)

print(data)

target = data['Pos']

del data['Pos']


from sklearn import metrics
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=0.3, random_state=42)  #Model Test Split

from sklearn import svm
from sklearn.model_selection import cross_val_score

clf = svm.SVC(kernel='linear')
clf.fit(X_train, y_train)

scores = cross_val_score(clf, X_train, y_train, cv=5)
y_pred = clf.predict(X_test)

print("Accuracy: {}".format(metrics.accuracy_score(y_test, y_pred)))  #Applying SVM and testing the metric score and cross val score
print("Accuracy mean {}".format(scores.mean()*100))
print(scores)

name = input("Player's name:")

fg = input("FG:")
ft = input("FT:")
tp = input("3P:")
trb = input("The Number Of Rebaunds that Player made in Season:")
ast = input("The Number Of Assists that Player made in Season:")   #Creating an array with fully of players stats
blk = input("The Number Of Blocks that Player made in Season:")
height = input("Height in cm:")
weigth = input("Weight in kg:")

player = np.array([[fg, ft, tp, trb, ast, blk,height,weigth]])

clf_player = clf.predict(player)

print("Player: {}".format(name))      #Result

print("Position: {}".format(clf_player))

"""
import pickle

with open("model_pickle","wb") as f:        #Saving the model
    pickle.dump(clf,f)
"""






