import numpy as np
import pandas as pd
from datetime import datetime
import sklearn
from sklearn.linear_model import LogisticRegression
import pandas_datareader.data as web
from sklearn.svm import LinearSVC, SVC
from sklearn.metrics import confusion_matrix

def create_dataset(stock_symbol, start_date, end_date, lags=5):

    # fetch the stock data from yahoo finance
    df = web.DataReader(stock_symbol, 'yahoo', start_date, end_date)

    # create a new dataframe
    # we want to use additional features: lagged returns ... today's returns, yesterday's returns etc
    tslag = pd.DataFrame(index=df.index)
    tslag['Today'] = df['Adj Close']
    tslag['Volume'] = df['Volume']

    # create the shifted lag series of prior trading period close values
    for i in range(0, lags):
        tslag['Lag%s' % str(i+1)] = df['Adj Close'].shift(i+1)

    # create the returns DataFrame
    dfret = pd.DataFrame(index=tslag.index)
    dfret['Volume'] = tslag['Volume']
    dfret['Today'] = tslag['Today'].pct_change()*100.0

    # create the lagged percentage returns columns
    for i in range(0, lags):
        dfret['Lag%s' % str(i + 1)] = tslag['Lag%s' % str(i + 1)].pct_change() * 100.00

    # 'Direction' column (+1 or -1) indicating an up/down
    dfret['Direction'] = np.sign(dfret['Today'])

    # because of the shifts there are NaN values .. we want to get rid of these NaNs
    dfret.drop(dfret.index[:5], inplace=True)

    return dfret


if __name__ == "__main__":
    # create a lagged series of the S&P500 US Stock index
    data = create_dataset('AAPL', datetime(2012, 1, 1), datetime(2017, 5, 31), lags=5)

    # Use the prior two days of returns as predictor
    # values, with direction as the response
    X = data[["Lag1", "Lag2", "Lag3", "Lag4"]]
    Y = data['Direction']

    # The test data is split into two parts: Before and after 1st Jan, 2005.
    start_test = datetime(2017, 1, 1)

    # Create training and test sets
    X_train = X[X.index < start_test]
    X_test = X[X.index >= start_test]
    Y_train = Y[Y.index < start_test]
    Y_test = Y[Y.index >= start_test]

    # we use Logistic Regression as the machine learning model
    model = SVC(C=1000000, cache_size=200, class_weight=None, coef0=0.0, degree=3, gamma=0.0001, kernel='rbf',
                max_iter=-1, probability=False)
    # model = LinearSVC()

    # train the model on the training set
    model.fit(X_train, Y_train)

    # make an array of predictions on the test set.
    pred = model.predict(X_test)

    # ouput the hit-rate and the confusion matrix for the model
    print("Accuracy of SVM model:", model.score(X_test, Y_test))
    print("Confusion matrix", confusion_matrix(pred, Y_test))