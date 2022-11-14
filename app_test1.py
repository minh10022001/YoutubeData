# import pickle as pk
# a = [[1.        , 0.00615495, 0.00520615, 0.00282992, 0.02739726,
#        0.20512821, 0.15366188, 0.03147067, 0.00331995]]
# model=pk.load(open('rfrmodel.pkl','rb'))
# scaler=pk.load(open('scale.pkl','rb'))
# scaler.transform(a)
# ans=int(model.predict(a))
# print(ans)

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

def eval_regression(model, pred, xtrain, ytrain, xtest, ytest):
    print("MAE: %.2f" % mean_absolute_error(ytest, pred)) 
    print("MSE: %.2f" % mean_squared_error(ytest, pred, squared=False)) 
    print('R2 score: %.2f' % r2_score(ytest, pred)) 

df = pd.read_csv('data_model.csv')
print(df)

df_train, df_test = train_test_split(df,test_size=0.2, random_state= 43, shuffle= True)
X_train = df_train.copy()
y_train = X_train.pop("video_viewCount_mv_official")

X_test = df_test.copy()
y_test = X_test.pop("video_viewCount_mv_official")

model = RandomForestRegressor(max_depth =None, max_features='sqrt', n_estimators= 50)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
eval_regression(model, y_pred, X_train, y_train, X_test, y_test)

a = [[1.        , 0.00615495, 0.00520615, 0.00282992, 0.02739726,
       0.20512821, 0.15366188, 0.03147067, 0.00331995]]

y = model.predict(a)
print(y)