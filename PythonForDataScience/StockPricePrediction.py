import numpy as np
import csv as csv
import matplotlib.pyplot as plt
from sklearn.svm import SVR

dates = []
prices = []

def get_data(filename):
	with open(filename,'r') as csvfile:
		csvFileReader = csv.reader(csvfile)
		next(csvFileReader)
		for row in csvFileReader :
			dates.append(int(row[0].split('-')[0]))
			prices.append(float(row[1]))
	print(dates)
	return
	
def predict_prices(dates,prices,x):
	dates = np.reshape(dates,(len(dates),1))

	svr_len = SVR(kernel='linear',C=1e3)
	svr_poly = SVR(kernel='poly',C=1e3,degree=2)
	svr_rbf = SVR(kernel='rbf',C=1e3,gamma=0.1)
	svr_len.fit(dates,prices)
	svr_poly.fit(dates,prices)
	svr_rbf.fit(dates,prices)

	plt.scatter(dates,prices,color='black', label='Data')
	plt.plot(dates, svr_len.predict(dates),color='red',label='Linear')
	plt.plot(dates, svr_poly.predict(dates),color='green',label='Poly')
	plt.plot(dates, svr_rbf.predict(dates),color='blue',label='RBF')
	plt.xlabel('Dates')
	plt.ylabel('Prices')
	plt.title('SVM Regression')
	plt.legend()
	plt.show()
	return svr_len.predict(x)[0],svr_poly.predict(x)[0],svr_rbf.predict(x)[0]

get_data('AAPL.csv')
predicted_prices = predict_prices(dates,prices,29)
print(predicted_prices)






