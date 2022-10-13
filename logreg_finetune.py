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

MAX_ITER = 100

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

def saveHyperparametersAndResult(df, alpha, beta_1, batch_size, lambda_, optimization,
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

	# To open dataframe
	if os.path.isfile(file):
		os.remove(file)
	df = pd.DataFrame(columns=['result', 'alpha', 'beta_1', \
	'batch_size', 'lambda', 'early_stopping', 'optimization', 'decay'])

	# Logistic regression

	x_train, x_test, y_train, y_test = data_spliter(x, y, 0.8)
	x_train, fqrt, tqrt = scale(x_train, option='robust')
	x_test, _, _ = scale(x_test, option='robust', lst1=fqrt, lst2=tqrt)
	x, _, _ = scale(x, option='robust', lst1=fqrt, lst2=tqrt)

	for j in range(100):
		print("Experiment with random hyperparameters number {}".format(j + 1))
		alpha, beta_1, batch_size, lambda_, optimization, early_stopping, decay = getRandomHyperparameters()
		print("alpha ", alpha, "| beta1 ", beta_1, "| batch_size ", batch_size, "| lambda ", lambda_, "| opt ", optimization, "| early stop ", early_stopping, "| decay ", decay)
		algo = OneVsAll(x_train.shape[1], max_y_val=4, alpha=alpha, max_iter=MAX_ITER, \
		initialization='he', lambda_=lambda_, optimization=optimization, decay=decay, \
		early_stopping=early_stopping, beta_1=beta_1)
		algo.perform(x_train, y_train, x_test, y_test, batch_size)
		results = []
		y_hat = algo.predict(x_test)
		i = 0
		while i < 10:
			results.append(sklearn.metrics.accuracy_score(y_test, y_hat))
			if i != 0:
				algo = OneVsAll(x_train.shape[1], max_y_val=4, alpha=alpha, max_iter=MAX_ITER, \
					initialization='he', lambda_=lambda_, optimization=optimization, decay=decay, \
					early_stopping=early_stopping, beta_1=beta_1)
			algo.perform(x_train, y_train, x_test, y_test, batch_size)
			y_hat = algo.predict(x_test)
			i += 1
		result = sum(results) / i
		saveHyperparametersAndResult(df, alpha, beta_1, batch_size, lambda_, optimization, early_stopping, decay, result)

	df.to_csv(file)

	max_accuracy = df['result'].max()
	print('\nMax accuracy :', max_accuracy)

	best_hyperparameters = df.loc[df['result'] == max_accuracy]
	print('Corresponding hyperparameters:\n', best_hyperparameters)

	min_accuracy = df['result'].min()
	print('\nMin accuracy :', max_accuracy)

	worst_hyperparameters = df.loc[df['result'] == min_accuracy]
	print('Corresponding hyperparameters:\n', worst_hyperparameters)

	alphas = best_hyperparameters['alpha'].values
	selected_alpha = np.median(alphas)
	print('\nALPHA', selected_alpha)

	beta_1s = best_hyperparameters['beta_1'].values
	selected_beta_1 = np.median(beta_1s)
	print('\nBETA 1', selected_beta_1)

	selected_batch_size = (best_hyperparameters['batch_size'].mode())[0]
	print('\nBATCH SIZE', selected_batch_size)

	selected_lambda_ = (best_hyperparameters['lambda'].mode())[0]
	print('\nLAMBDA', selected_lambda_)

	selected_early_stopping = (best_hyperparameters['early_stopping'].mode())[0]
	print('\nEARLY STOPPING', selected_early_stopping)

	selected_optimization = (best_hyperparameters['optimization'].mode())[0]
	print('\nOPTIMIZATION', selected_optimization)

	selected_decay = (best_hyperparameters['decay'].mode())[0]
	print('\nDECAY', selected_decay)
