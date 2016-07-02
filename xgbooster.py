import xgboost as xgb
import numpy as np

from prepare_data import Clean

cleaned = Clean("train.csv")
train_X = np.array(cleaned.x[:18])
train_y = np.array(cleaned.y_[:18])
test_X = np.array(cleaned.x[180:220])
text_y = np.array(cleaned.y_[180:220])

dtrain = xgb.DMatrix(train_X, label=train_y)

dtest = xgb.DMatrix(test_X, label=text_y)

# gbm = xgb.XGBClassifier(max_depth=3, n_estimators=300, learning_rate=0.05).fit(dtrain_x, train_y)
# predictions = gbm.predict(dtest_x)
#
# print(predictions[:6])
print(text_y[:6])


param = {'bst:max_depth':2, 'bst:eta':1, 'silent':1, 'objective':'binary:logistic' }
evallist  = [(dtest,'eval'), (dtrain,'train')]
num_round = 10
bst = xgb.train( param, dtrain, num_round, evallist )

# print(dtrain_x)