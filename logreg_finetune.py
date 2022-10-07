from random import random
import pandas as pd
import numpy as np
import os
import sklearn.metrics
from utils.dataframe_manip import *
from utils.logistic_regression import *
from utils.logistic_scores import *
from utils.array_manip import *
from utils.one_vs_all import *
import random

max_iter=1000

def getRandomHyperparameters():
	alpha = random.uniform(0.0001, 0.1)
	beta_1 = random.uniform(0.001, 0.1)
	possible_batch_size = [1, 16, 32, 64, 128, 256, 512, 1024]
	batch_size = random.choice(possible_batch_size)
	possible_lambda_ = np.linspace(0, 1, 5)
	lambda_ = float(np.random.choice(possible_lambda_))
	supported_optimization = ['momentum', 'rmsprop', 'adam', None]
	optimization = random.choice(supported_optimization)
	early_stopping = random.random() > 0.8
	decay = random.random() > 0.5
	return alpha, beta_1, batch_size, lambda_, optimization, early_stopping, decay

def saveHyperparametersAndResult(df, j, alpha, beta_1, batch_size, lambda_, optimization,
	early_stopping, decay, result):
	df.loc[len(df)] = [result, alpha, beta_1, batch_size, lambda_, early_stopping, \
		optimization, decay]

if __name__ == '__main__':

	file='experiments.csv'

	# Preprocess data
	df = get_dataframe('./datasets/dataset_train.csv')
	to_drop = ['Index', 'Arithmancy', 'Care of Magical Creatures', 'Defense Against the Dark Arts', 'Birthday', 'Best Hand', 'First Name', 'Last Name']
	df = df.drop(to_drop, axis=1)
	numerics_df = get_numerics(df)
	houses = get_houses_list(df)
	df['Hogwarts House'].replace(houses, [0, 1, 2, 3], inplace=True)
	for column in numerics_df.columns:
		if df[column].isnull().values.any():
			abs_z_score = df[column].abs()
			outliers =  abs_z_score > 3
			outliers = np.asarray(abs_z_score[outliers])
			if len(outliers) > 0:
				df[column].fillna(value=df[column].median(), inplace=True)
			else:
				df[column].fillna(value=df[column].mean(), inplace=True)

	# Creation of train and test/dev set
	array = np.asarray(df)
	x, y = array[:, 1:], array[:, 0].reshape(-1, 1)
	x_train, x_test, y_train, y_test = data_spliter(x, y, 0.8)

	# To open dataframe
	if os.path.isfile(file):
		df = pd.read_csv(file)
	else:
		df = pd.DataFrame(columns=['result', 'alpha', 'beta_1', \
		'batch_size', 'lambda', 'early_stopping', 'optimization', 'decay'])

	# Logistic regression
	x_train, fqrt, tqrt = scale(x_train, option='robust')
	x_test, _ , _ = scale(x_test, option='robust', lst1=fqrt, lst2=tqrt)
	x, _, _ = scale(x, option='robust', lst1=fqrt, lst2=tqrt)

	for j in range(100):
		alpha, beta_1, batch_size, lambda_, optimization, early_stopping, decay = getRandomHyperparameters()
		algo = OneVsAll(x_train.shape[1], max_y_val=4, alpha=alpha, max_iter=max_iter, \
		initialization='he', lambda_=lambda_, optimization=optimization, decay=decay, \
		early_stopping=early_stopping, beta_1=beta_1)
		algo.perform(x_train, y_train, x_test, y_test, batch_size)
		results = []
		y_hat = algo.predict(x_test)
		i = 0
		print("----")
		print("Got : {}".format(sklearn.metrics.accuracy_score(y_test, y_hat)))
		while i < 3:
			results.append(sklearn.metrics.accuracy_score(y_test, y_hat))
			if i != 0:
				print("Got : {}".format(sklearn.metrics.accuracy_score(y_test, y_hat)))
				algo = OneVsAll(x_train.shape[1], max_y_val=4, alpha=alpha, max_iter=max_iter, \
					initialization='he', lambda_=lambda_, optimization=optimization, decay=decay, \
					early_stopping=early_stopping, beta_1=beta_1)
			algo.perform(x_train, y_train, x_test, y_test, batch_size)
			y_hat = algo.predict(x_test)
			i += 1
		result = sum(results) / i
		saveHyperparametersAndResult(df, j, alpha, beta_1, batch_size, lambda_, optimization, early_stopping, decay, result)

	df.to_csv(file, mode='a', header=not os.path.exists(file))
